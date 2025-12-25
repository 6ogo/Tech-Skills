# dg-04: Access Control & Policies

## Overview

Implement role-based access control, column/row-level security, dynamic data masking, and access audit logging.

## Key Capabilities

- **RBAC**: Role-based access control
- **Column-Level Security**: Restrict sensitive columns
- **Row-Level Security**: Filter data by user context
- **Dynamic Data Masking**: Auto-mask sensitive data
- **Access Audit Logging**: Track all data access

## Implementation

```sql
-- Column-level security
CREATE VIEW customer_secure AS
SELECT
    customer_id,
    CASE
        WHEN CURRENT_USER() IN (SELECT user FROM admin_users)
        THEN email  -- Show full email to admins
        ELSE CONCAT(LEFT(email, 3), '***@', SPLIT_PART(email, '@', 2))  -- Mask for others
    END as email,
    first_name,
    last_name
FROM customers;

-- Row-level security
CREATE POLICY customer_region_policy ON customers
FOR SELECT
USING (region = current_setting('app.user_region'));
```

## Integration

**Connects with:** sa-01 (PII Detection), sa-04 (IAM), dg-01 (Catalog)
