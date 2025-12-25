-- Medallion Architecture SQL Patterns
-- Bronze → Silver → Gold transformations for Data Lakehouse

-- ================================================================
-- BRONZE LAYER - Raw Data Ingestion
-- ================================================================

-- View bronze layer with metadata
SELECT
    *,
    _bronze_ingestion_timestamp,
    _bronze_source_path,
    _bronze_table_name
FROM bronze.crm_leads
WHERE _bronze_ingestion_date >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY _bronze_ingestion_timestamp DESC;

-- Check for duplicate records in bronze
SELECT
    lead_id,
    COUNT(*) as duplicate_count,
    MIN(_bronze_ingestion_timestamp) as first_seen,
    MAX(_bronze_ingestion_timestamp) as last_seen
FROM bronze.crm_leads
GROUP BY lead_id
HAVING COUNT(*) > 1;

-- Bronze layer data quality check
SELECT
    _bronze_ingestion_date,
    COUNT(*) as total_records,
    COUNT(DISTINCT lead_id) as unique_leads,
    COUNT(*) - COUNT(DISTINCT lead_id) as duplicates,
    COUNT(CASE WHEN email IS NULL THEN 1 END) as missing_email,
    COUNT(CASE WHEN company IS NULL THEN 1 END) as missing_company
FROM bronze.crm_leads
GROUP BY _bronze_ingestion_date
ORDER BY _bronze_ingestion_date DESC;

-- ================================================================
-- SILVER LAYER - Cleaned & Standardized
-- ================================================================

-- Transform Bronze → Silver (Deduplication & Cleaning)
CREATE OR REPLACE TABLE silver.crm_leads_clean AS
WITH deduplicated AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY lead_id
            ORDER BY _bronze_ingestion_timestamp DESC
        ) as rn
    FROM bronze.crm_leads
),
cleaned AS (
    SELECT
        lead_id,
        LOWER(TRIM(email)) as email,
        TRIM(company) as company,
        UPPER(industry) as industry,
        company_size,
        job_title,
        lead_source,
        created_date,
        COALESCE(lead_score, 0) as lead_score,
        UPPER(status) as status,
        -- Silver metadata
        CURRENT_TIMESTAMP() as _silver_processed_timestamp,
        _bronze_ingestion_timestamp as _bronze_ingestion_timestamp
    FROM deduplicated
    WHERE rn = 1  -- Keep only most recent version
        AND email IS NOT NULL  -- Basic validation
        AND email LIKE '%@%'  -- Email format check
)
SELECT * FROM cleaned;

-- Silver layer quality metrics
SELECT
    COUNT(*) as total_records,
    COUNT(DISTINCT email) as unique_emails,
    COUNT(CASE WHEN lead_score >= 80 THEN 1 END) as high_score_leads,
    AVG(lead_score) as avg_lead_score,
    COUNT(DISTINCT industry) as unique_industries,
    COUNT(DISTINCT company) as unique_companies,
    MAX(_silver_processed_timestamp) as last_processed
FROM silver.crm_leads_clean;

-- Schema drift detection (Silver)
SELECT
    column_name,
    data_type,
    is_nullable,
    COUNT(*) OVER () as total_columns
FROM information_schema.columns
WHERE table_schema = 'silver'
  AND table_name = 'crm_leads_clean'
ORDER BY ordinal_position;

-- ================================================================
-- GOLD LAYER - Business Logic & Aggregations
-- ================================================================

-- Transform Silver → Gold (Lead Segmentation)
CREATE OR REPLACE TABLE gold.lead_segments AS
SELECT
    lead_id,
    email,
    company,
    industry,
    company_size,
    job_title,
    lead_source,
    created_date,
    lead_score,
    status,
    -- Business logic: Lead segment
    CASE
        WHEN lead_score >= 90 THEN 'HOT'
        WHEN lead_score >= 70 THEN 'WARM'
        WHEN lead_score >= 50 THEN 'QUALIFIED'
        ELSE 'COLD'
    END as lead_segment,
    -- Seniority level from job title
    CASE
        WHEN UPPER(job_title) LIKE '%VP%' OR UPPER(job_title) LIKE '%VICE PRESIDENT%' THEN 'VP+'
        WHEN UPPER(job_title) LIKE '%DIRECTOR%' THEN 'Director'
        WHEN UPPER(job_title) LIKE '%MANAGER%' THEN 'Manager'
        WHEN UPPER(job_title) LIKE '%SENIOR%' OR UPPER(job_title) LIKE '%SR%' THEN 'Senior IC'
        ELSE 'IC'
    END as seniority_level,
    -- Company size category
    CASE
        WHEN company_size IN ('1000+', '500-1000') THEN 'Enterprise'
        WHEN company_size IN ('100-500', '50-100') THEN 'Mid-Market'
        ELSE 'SMB'
    END as company_category,
    -- Days since creation
    DATEDIFF(CURRENT_DATE, created_date) as days_since_created,
    -- Gold metadata
    CURRENT_TIMESTAMP() as _gold_created_timestamp
FROM silver.crm_leads_clean;

-- Gold Layer: Daily Lead Metrics
CREATE OR REPLACE TABLE gold.daily_lead_metrics AS
SELECT
    DATE(created_date) as metric_date,
    lead_source,
    lead_segment,
    company_category,
    COUNT(*) as lead_count,
    AVG(lead_score) as avg_lead_score,
    COUNT(CASE WHEN lead_segment = 'HOT' THEN 1 END) as hot_leads,
    COUNT(CASE WHEN status = 'QUALIFIED' THEN 1 END) as qualified_leads,
    COUNT(DISTINCT company) as unique_companies,
    COUNT(DISTINCT industry) as unique_industries
FROM gold.lead_segments
GROUP BY
    DATE(created_date),
    lead_source,
    lead_segment,
    company_category;

-- Gold Layer: Lead Source Performance
CREATE OR REPLACE VIEW gold.lead_source_performance AS
SELECT
    lead_source,
    COUNT(*) as total_leads,
    AVG(lead_score) as avg_score,
    COUNT(CASE WHEN lead_segment = 'HOT' THEN 1 END) as hot_leads,
    COUNT(CASE WHEN lead_segment IN ('HOT', 'WARM') THEN 1 END) as quality_leads,
    ROUND(100.0 * COUNT(CASE WHEN lead_segment IN ('HOT', 'WARM') THEN 1 END) / COUNT(*), 2) as quality_rate,
    COUNT(DISTINCT company) as unique_companies,
    MAX(created_date) as latest_lead_date,
    DATEDIFF(CURRENT_DATE, MAX(created_date)) as days_since_last_lead
FROM gold.lead_segments
GROUP BY lead_source
ORDER BY quality_rate DESC;

-- Gold Layer: Industry Analysis
CREATE OR REPLACE VIEW gold.industry_analysis AS
SELECT
    industry,
    company_category,
    COUNT(*) as lead_count,
    AVG(lead_score) as avg_lead_score,
    COUNT(CASE WHEN lead_segment = 'HOT' THEN 1 END) as hot_leads,
    COUNT(CASE WHEN seniority_level IN ('VP+', 'Director') THEN 1 END) as senior_decision_makers,
    COUNT(DISTINCT company) as unique_companies,
    ROUND(AVG(days_since_created), 1) as avg_age_days
FROM gold.lead_segments
GROUP BY industry, company_category
HAVING COUNT(*) >= 10
ORDER BY hot_leads DESC, avg_lead_score DESC;

-- ================================================================
-- INCREMENTAL PROCESSING PATTERNS
-- ================================================================

-- Incremental load: Bronze to Silver (only new/updated records)
MERGE INTO silver.crm_leads_clean AS target
USING (
    SELECT
        lead_id,
        LOWER(TRIM(email)) as email,
        TRIM(company) as company,
        UPPER(industry) as industry,
        company_size,
        job_title,
        lead_source,
        created_date,
        COALESCE(lead_score, 0) as lead_score,
        UPPER(status) as status,
        _bronze_ingestion_timestamp
    FROM (
        SELECT *,
            ROW_NUMBER() OVER (
                PARTITION BY lead_id
                ORDER BY _bronze_ingestion_timestamp DESC
            ) as rn
        FROM bronze.crm_leads
        WHERE _bronze_ingestion_timestamp > (
            SELECT COALESCE(MAX(_bronze_ingestion_timestamp), '1900-01-01')
            FROM silver.crm_leads_clean
        )
    )
    WHERE rn = 1
        AND email IS NOT NULL
        AND email LIKE '%@%'
) AS source
ON target.lead_id = source.lead_id
WHEN MATCHED THEN
    UPDATE SET
        email = source.email,
        company = source.company,
        industry = source.industry,
        company_size = source.company_size,
        job_title = source.job_title,
        lead_source = source.lead_source,
        created_date = source.created_date,
        lead_score = source.lead_score,
        status = source.status,
        _silver_processed_timestamp = CURRENT_TIMESTAMP(),
        _bronze_ingestion_timestamp = source._bronze_ingestion_timestamp
WHEN NOT MATCHED THEN
    INSERT (
        lead_id, email, company, industry, company_size,
        job_title, lead_source, created_date, lead_score, status,
        _silver_processed_timestamp, _bronze_ingestion_timestamp
    )
    VALUES (
        source.lead_id, source.email, source.company, source.industry,
        source.company_size, source.job_title, source.lead_source,
        source.created_date, source.lead_score, source.status,
        CURRENT_TIMESTAMP(), source._bronze_ingestion_timestamp
    );

-- ================================================================
-- DATA QUALITY MONITORING
-- ================================================================

-- Cross-layer data quality dashboard
SELECT
    'Bronze' as layer,
    COUNT(*) as record_count,
    COUNT(DISTINCT lead_id) as unique_ids,
    MAX(_bronze_ingestion_timestamp) as last_update
FROM bronze.crm_leads

UNION ALL

SELECT
    'Silver' as layer,
    COUNT(*) as record_count,
    COUNT(DISTINCT lead_id) as unique_ids,
    MAX(_silver_processed_timestamp) as last_update
FROM silver.crm_leads_clean

UNION ALL

SELECT
    'Gold' as layer,
    COUNT(*) as record_count,
    COUNT(DISTINCT lead_id) as unique_ids,
    MAX(_gold_created_timestamp) as last_update
FROM gold.lead_segments;

-- ================================================================
-- PERFORMANCE OPTIMIZATION
-- ================================================================

-- Optimize Silver table (Vacuum + Optimize)
-- OPTIMIZE silver.crm_leads_clean ZORDER BY (lead_id, created_date);
-- VACUUM silver.crm_leads_clean RETAIN 168 HOURS;  -- 7 days

-- Optimize Gold table
-- OPTIMIZE gold.lead_segments ZORDER BY (lead_segment, created_date, company_category);
-- VACUUM gold.lead_segments RETAIN 168 HOURS;

-- Table statistics for query optimization
-- ANALYZE TABLE silver.crm_leads_clean COMPUTE STATISTICS;
-- ANALYZE TABLE gold.lead_segments COMPUTE STATISTICS FOR ALL COLUMNS;
