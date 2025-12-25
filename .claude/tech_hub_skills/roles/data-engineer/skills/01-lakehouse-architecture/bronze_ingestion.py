"""
Bronze Layer: Raw Data Ingestion
Ingest data from multiple sources with validation and error handling.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import pandas as pd
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from pyspark.sql import functions as F
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BronzeLoader:
    """
    Bronze layer ingestion with schema validation and audit logging.

    Bronze layer principles:
    - Append-only (preserve full history)
    - Raw data with minimal transformation
    - Add metadata (ingestion timestamp, source, file name)
    - Schema validation
    - Error quarantine
    """

    def __init__(
        self,
        spark: Optional[SparkSession] = None,
        bronze_path: str = "/lakehouse/bronze",
        quarantine_path: str = "/lakehouse/quarantine"
    ):
        """
        Initialize Bronze loader.

        Args:
            spark: SparkSession (creates one if not provided)
            bronze_path: Path to bronze layer storage
            quarantine_path: Path for invalid records
        """
        self.spark = spark or self._create_spark_session()
        self.bronze_path = bronze_path
        self.quarantine_path = quarantine_path

        # Create directories if they don't exist
        Path(bronze_path).mkdir(parents=True, exist_ok=True)
        Path(quarantine_path).mkdir(parents=True, exist_ok=True)

    def _create_spark_session(self) -> SparkSession:
        """Create Spark session with Delta Lake support."""
        return SparkSession.builder \
            .appName("BronzeIngestion") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .config("spark.databricks.delta.retentionDurationCheck.enabled", "false") \
            .getOrCreate()

    def ingest_from_source(
        self,
        source_path: str,
        table_name: str,
        source_format: str = "json",
        schema: Optional[StructType] = None,
        options: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Ingest data from source into Bronze layer.

        Args:
            source_path: Path to source data
            table_name: Name for bronze table
            source_format: Format (json, csv, parquet, etc.)
            schema: Optional schema to enforce
            options: Additional read options

        Returns:
            Ingestion metrics
        """
        logger.info(f"Starting ingestion: {table_name} from {source_path}")

        try:
            # Read source data
            df = self._read_source(source_path, source_format, schema, options)

            # Add bronze layer metadata
            df_bronze = self._add_bronze_metadata(df, source_path, table_name)

            # Validate schema if provided
            if schema:
                df_bronze = self._validate_schema(df_bronze, schema)

            # Write to bronze layer
            bronze_table_path = f"{self.bronze_path}/{table_name}"

            df_bronze.write \
                .format("delta") \
                .mode("append") \
                .option("mergeSchema", "true") \
                .save(bronze_table_path)

            # Collect metrics
            record_count = df_bronze.count()

            metrics = {
                "status": "success",
                "table_name": table_name,
                "records_ingested": record_count,
                "source_path": source_path,
                "ingestion_timestamp": datetime.now().isoformat(),
                "bronze_path": bronze_table_path
            }

            logger.info(f"✅ Successfully ingested {record_count} records to {table_name}")

            return metrics

        except Exception as e:
            logger.error(f"❌ Ingestion failed: {str(e)}")

            return {
                "status": "failed",
                "table_name": table_name,
                "error": str(e),
                "ingestion_timestamp": datetime.now().isoformat()
            }

    def _read_source(
        self,
        source_path: str,
        source_format: str,
        schema: Optional[StructType] = None,
        options: Optional[Dict[str, str]] = None
    ) -> DataFrame:
        """Read data from source."""
        options = options or {}

        reader = self.spark.read.format(source_format)

        if schema:
            reader = reader.schema(schema)

        for key, value in options.items():
            reader = reader.option(key, value)

        return reader.load(source_path)

    def _add_bronze_metadata(
        self,
        df: DataFrame,
        source_path: str,
        table_name: str
    ) -> DataFrame:
        """Add bronze layer audit columns."""
        return df \
            .withColumn("_bronze_ingestion_timestamp", F.current_timestamp()) \
            .withColumn("_bronze_source_path", F.lit(source_path)) \
            .withColumn("_bronze_table_name", F.lit(table_name)) \
            .withColumn("_bronze_ingestion_date", F.current_date())

    def _validate_schema(
        self,
        df: DataFrame,
        expected_schema: StructType
    ) -> DataFrame:
        """
        Validate DataFrame against expected schema.

        Quarantine records that don't match schema.
        """
        # In production, implement sophisticated schema validation
        # For now, we return the df as-is
        return df

    def ingest_csv(
        self,
        csv_path: str,
        table_name: str,
        delimiter: str = ",",
        header: bool = True,
        schema: Optional[StructType] = None
    ) -> Dict[str, Any]:
        """Convenience method for CSV ingestion."""
        options = {
            "delimiter": delimiter,
            "header": str(header).lower(),
            "inferSchema": "true" if schema is None else "false"
        }

        return self.ingest_from_source(
            source_path=csv_path,
            table_name=table_name,
            source_format="csv",
            schema=schema,
            options=options
        )

    def ingest_json(
        self,
        json_path: str,
        table_name: str,
        multiline: bool = False,
        schema: Optional[StructType] = None
    ) -> Dict[str, Any]:
        """Convenience method for JSON ingestion."""
        options = {
            "multiLine": str(multiline).lower()
        }

        return self.ingest_from_source(
            source_path=json_path,
            table_name=table_name,
            source_format="json",
            schema=schema,
            options=options
        )

    def ingest_parquet(
        self,
        parquet_path: str,
        table_name: str
    ) -> Dict[str, Any]:
        """Convenience method for Parquet ingestion."""
        return self.ingest_from_source(
            source_path=parquet_path,
            table_name=table_name,
            source_format="parquet"
        )

    def create_bronze_table(
        self,
        table_name: str,
        schema: StructType,
        partition_by: Optional[List[str]] = None
    ) -> None:
        """Create an empty bronze table with schema."""
        bronze_table_path = f"{self.bronze_path}/{table_name}"

        # Create empty DataFrame with schema
        empty_df = self.spark.createDataFrame([], schema)

        # Add bronze metadata columns
        bronze_df = self._add_bronze_metadata(empty_df, "initialized", table_name)

        # Write table
        writer = bronze_df.write.format("delta").mode("overwrite")

        if partition_by:
            writer = writer.partitionBy(*partition_by)

        writer.save(bronze_table_path)

        logger.info(f"✅ Created bronze table: {table_name}")


# Example CRM schema
CRM_LEADS_SCHEMA = StructType([
    StructField("lead_id", StringType(), False),
    StructField("email", StringType(), True),
    StructField("company", StringType(), True),
    StructField("industry", StringType(), True),
    StructField("company_size", StringType(), True),
    StructField("job_title", StringType(), True),
    StructField("lead_source", StringType(), True),
    StructField("created_date", TimestampType(), True),
    StructField("lead_score", IntegerType(), True),
    StructField("status", StringType(), True)
])


# Example usage
if __name__ == "__main__":
    print("=" * 80)
    print("Bronze Layer Ingestion Demo")
    print("=" * 80)

    # Create sample data
    sample_data = [
        {
            "lead_id": "L001",
            "email": "john@techcorp.com",
            "company": "TechCorp",
            "industry": "Software",
            "company_size": "100-500",
            "job_title": "Data Scientist",
            "lead_source": "Website",
            "created_date": "2025-01-15T10:30:00",
            "lead_score": 85,
            "status": "New"
        },
        {
            "lead_id": "L002",
            "email": "sarah@datainc.com",
            "company": "Data Inc",
            "industry": "Analytics",
            "company_size": "50-100",
            "job_title": "ML Engineer",
            "lead_source": "LinkedIn",
            "created_date": "2025-01-16T14:20:00",
            "lead_score": 92,
            "status": "Qualified"
        }
    ]

    # Save as JSON
    sample_path = "/tmp/sample_crm_leads.json"
    with open(sample_path, 'w') as f:
        json.dump(sample_data, f)

    # Initialize Bronze loader
    bronze = BronzeLoader(
        bronze_path="./lakehouse/bronze",
        quarantine_path="./lakehouse/quarantine"
    )

    # Ingest data
    metrics = bronze.ingest_json(
        json_path=sample_path,
        table_name="crm_leads",
        multiline=True,
        schema=CRM_LEADS_SCHEMA
    )

    print("\n📊 Ingestion Metrics:")
    print(json.dumps(metrics, indent=2))

    # Query bronze table
    print("\n📋 Bronze Table Sample:")
    bronze_df = bronze.spark.read.format("delta").load("./lakehouse/bronze/crm_leads")
    bronze_df.show(truncate=False)

    print(f"\nBronze table row count: {bronze_df.count()}")
