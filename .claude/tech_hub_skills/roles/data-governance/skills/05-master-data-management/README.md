# dg-05: Master Data Management

## Overview

Entity resolution, golden record creation, data stewardship, and hierarchy management for critical business entities.

## Key Capabilities

- **Entity Resolution**: Match and merge duplicate entities
- **Golden Record**: Single source of truth
- **Data Stewardship**: Workflows for data quality
- **Cross-Reference**: Link entities across systems
- **Hierarchy Management**: Organizational structures

## Implementation

```python
# Entity resolution
from recordlinkage import Index, Compare

def match_customers(df1, df2):
    """Match customer records across systems"""
    indexer = Index()
    indexer.block('last_name')
    candidate_pairs = indexer.index(df1, df2)

    compare = Compare()
    compare.exact('first_name', 'first_name')
    compare.string('email', 'email', method='jarowinkler', threshold=0.85)
    compare.numeric('age', 'age', method='linear', offset=2)

    features = compare.compute(candidate_pairs, df1, df2)
    matches = features[features.sum(axis=1) > 2.5]

    return matches
```

## Integration

**Connects with:** dg-01 (Catalog), dg-03 (Quality), de-02 (ETL)
