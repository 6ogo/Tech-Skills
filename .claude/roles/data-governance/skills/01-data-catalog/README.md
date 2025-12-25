# dg-01: Data Catalog

## Overview

Build enterprise data catalogs for asset discovery, metadata management, and data classification.

## Key Capabilities

- **Asset Registration**: Automated discovery and registration of data assets
- **Metadata Management**: Technical, business, and operational metadata
- **Data Classification**: Automatic classification (PII, confidential, public)
- **Search & Discovery**: Powerful search capabilities for data consumers
- **Business Glossary**: Standardized business terminology

## Tools & Technologies

- **Azure Purview**: Enterprise data catalog
- **DataHub**: Open-source metadata platform
- **Amundsen**: Lyft's data discovery platform
- **Collibra**: Data governance platform

## Implementation

### 1. Asset Registration

```python
# Automated asset registration
from azure.purview.catalog import PurviewCatalogClient

def register_data_asset(asset_name, asset_type, location):
    """Register data asset in catalog"""
    client = PurviewCatalogClient()

    asset = {
        "typeName": asset_type,
        "attributes": {
            "name": asset_name,
            "qualifiedName": f"{location}/{asset_name}",
            "location": location
        }
    }

    return client.entity.create_or_update(entity=asset)
```

### 2. Metadata Management

```python
# Add business metadata
def add_business_metadata(asset_id, owner, description, tags):
    """Enrich asset with business context"""
    metadata = {
        "businessOwner": owner,
        "description": description,
        "tags": tags,
        "certification": "certified"
    }

    return client.entity.add_business_metadata(
        guid=asset_id,
        business_metadata=metadata
    )
```

### 3. Data Classification

```python
# Automatic classification
def classify_data(asset_id):
    """Apply automatic classification based on content"""
    classifications = []

    # Scan for PII
    if contains_pii(asset_id):
        classifications.append("PII")

    # Scan for confidential data
    if contains_confidential(asset_id):
        classifications.append("Confidential")

    return client.entity.add_classifications(
        guid=asset_id,
        classifications=classifications
    )
```

## Best Practices

1. **Automate Discovery** - Use scanners to auto-discover assets
2. **Enrich Metadata** - Add business context, not just technical
3. **Clear Ownership** - Every asset needs a business owner
4. **Regular Updates** - Keep metadata fresh and relevant
5. **User Training** - Train users on search capabilities

## Cost Optimization

- Use Azure Purview Standard tier for < 100k assets
- Schedule scans during off-peak hours
- Use incremental scans instead of full scans
- Archive unused asset metadata

## Integration

**Connects with:**
- de-01 (Lakehouse): Catalog lakehouse tables
- sa-01 (PII Detection): Auto-classify PII data
- dg-02 (Lineage): Link to lineage tracking
- dg-03 (Quality): Link quality scores

## Quick Win

Start with top 10 critical datasets, manually catalog them with rich metadata, then expand automated discovery.
