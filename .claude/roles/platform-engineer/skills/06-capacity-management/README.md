# pe-06: Capacity Management

## Overview

Capacity planning, resource forecasting, cluster autoscaling, cost-capacity optimization, and quota management.

## Key Capabilities

- **Capacity Planning**: Forecast resource needs
- **Resource Forecasting**: Predict growth trends
- **Cluster Autoscaling**: Auto-scale infrastructure
- **Cost-Capacity Optimization**: Balance cost vs. capacity
- **Quota Management**: Team-level quotas

## Implementation

```python
# Capacity forecasting
import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_capacity(historical_usage_df, days_ahead=90):
    """Forecast future resource needs"""
    df = historical_usage_df.copy()
    df['days'] = (df['date'] - df['date'].min()).dt.days

    model = LinearRegression()
    model.fit(df[['days']], df['cpu_cores'])

    future_days = df['days'].max() + days_ahead
    forecast = model.predict([[future_days]])

    return {
        'current_usage': df['cpu_cores'].iloc[-1],
        'forecasted_usage': forecast[0],
        'growth_rate': model.coef_[0],
        'recommendation': 'scale_up' if forecast[0] > df['cpu_cores'].max() else 'maintain'
    }
```

```yaml
# Cluster autoscaler config
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: customer-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: customer-api
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

## Integration

**Connects with:** fo-01 (Cost Visibility), do-02 (Kubernetes), pe-03 (SLO)
