"""
Automated Exploratory Data Analysis (EDA) Generator
Generate comprehensive EDA reports with minimal code.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


@dataclass
class DataProfileSummary:
    """Summary statistics for a dataset."""
    n_rows: int
    n_columns: int
    n_numeric: int
    n_categorical: int
    n_datetime: int
    missing_cells: int
    missing_percentage: float
    duplicate_rows: int
    memory_usage_mb: float


class EDAGenerator:
    """Automated EDA report generator."""

    def __init__(self, figsize: Tuple[int, int] = (12, 6)):
        """
        Initialize EDA generator.

        Args:
            figsize: Default figure size for plots
        """
        self.figsize = figsize
        self.report_sections = []

    def generate_profile(self, df: pd.DataFrame) -> DataProfileSummary:
        """
        Generate data profile summary.

        Args:
            df: Input DataFrame

        Returns:
            DataProfileSummary object
        """
        # Count column types
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        datetime_cols = df.select_dtypes(include=['datetime64']).columns

        # Calculate statistics
        missing_cells = df.isna().sum().sum()
        total_cells = df.shape[0] * df.shape[1]
        missing_pct = (missing_cells / total_cells * 100) if total_cells > 0 else 0

        return DataProfileSummary(
            n_rows=len(df),
            n_columns=len(df.columns),
            n_numeric=len(numeric_cols),
            n_categorical=len(categorical_cols),
            n_datetime=len(datetime_cols),
            missing_cells=missing_cells,
            missing_percentage=round(missing_pct, 2),
            duplicate_rows=df.duplicated().sum(),
            memory_usage_mb=round(df.memory_usage(deep=True).sum() / 1024**2, 2)
        )

    def analyze_missing_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Analyze missing data patterns."""
        missing_stats = pd.DataFrame({
            'Column': df.columns,
            'Missing_Count': df.isna().sum().values,
            'Missing_Percentage': (df.isna().sum() / len(df) * 100).values,
            'Data_Type': df.dtypes.values
        })

        missing_stats = missing_stats[missing_stats['Missing_Count'] > 0].sort_values(
            'Missing_Percentage', ascending=False
        )

        return missing_stats

    def analyze_numeric_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Comprehensive analysis of numeric columns."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) == 0:
            return pd.DataFrame()

        stats_list = []

        for col in numeric_cols:
            col_data = df[col].dropna()

            if len(col_data) == 0:
                continue

            stats_dict = {
                'Column': col,
                'Count': len(col_data),
                'Mean': col_data.mean(),
                'Median': col_data.median(),
                'Std': col_data.std(),
                'Min': col_data.min(),
                'Max': col_data.max(),
                'Q25': col_data.quantile(0.25),
                'Q75': col_data.quantile(0.75),
                'IQR': col_data.quantile(0.75) - col_data.quantile(0.25),
                'Skewness': col_data.skew(),
                'Kurtosis': col_data.kurtosis(),
                'Zeros': (col_data == 0).sum(),
                'Zeros_Pct': (col_data == 0).sum() / len(col_data) * 100
            }

            stats_list.append(stats_dict)

        return pd.DataFrame(stats_list).round(3)

    def analyze_categorical_columns(self, df: pd.DataFrame, max_categories: int = 20) -> Dict[str, pd.DataFrame]:
        """Analyze categorical columns."""
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns

        results = {}

        for col in categorical_cols:
            value_counts = df[col].value_counts()

            if len(value_counts) <= max_categories:
                stats_df = pd.DataFrame({
                    'Value': value_counts.index,
                    'Count': value_counts.values,
                    'Percentage': (value_counts / len(df) * 100).values
                }).round(2)

                results[col] = stats_df

        return results

    def detect_outliers(self, df: pd.DataFrame, method: str = 'iqr', threshold: float = 1.5) -> Dict[str, Dict[str, Any]]:
        """
        Detect outliers in numeric columns.

        Args:
            df: Input DataFrame
            method: Detection method ('iqr' or 'zscore')
            threshold: Threshold value (1.5 for IQR, 3 for z-score)

        Returns:
            Dictionary with outlier information per column
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outliers = {}

        for col in numeric_cols:
            col_data = df[col].dropna()

            if len(col_data) == 0:
                continue

            if method == 'iqr':
                Q1 = col_data.quantile(0.25)
                Q3 = col_data.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR

                outlier_mask = (col_data < lower_bound) | (col_data > upper_bound)

            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(col_data))
                outlier_mask = z_scores > threshold

            else:
                continue

            outlier_count = outlier_mask.sum()
            outlier_pct = (outlier_count / len(col_data) * 100)

            if outlier_count > 0:
                outliers[col] = {
                    'count': outlier_count,
                    'percentage': round(outlier_pct, 2),
                    'method': method,
                    'threshold': threshold,
                    'lower_bound': lower_bound if method == 'iqr' else None,
                    'upper_bound': upper_bound if method == 'iqr' else None
                }

        return outliers

    def calculate_correlations(self, df: pd.DataFrame, method: str = 'pearson', threshold: float = 0.7) -> pd.DataFrame:
        """
        Calculate correlations between numeric columns.

        Args:
            df: Input DataFrame
            method: Correlation method ('pearson', 'spearman', 'kendall')
            threshold: Only show correlations above this threshold

        Returns:
            DataFrame with high correlations
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) < 2:
            return pd.DataFrame()

        corr_matrix = df[numeric_cols].corr(method=method)

        # Extract high correlations
        high_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) >= threshold:
                    high_corr.append({
                        'Variable_1': corr_matrix.columns[i],
                        'Variable_2': corr_matrix.columns[j],
                        'Correlation': round(corr_value, 3),
                        'Abs_Correlation': round(abs(corr_value), 3)
                    })

        if high_corr:
            return pd.DataFrame(high_corr).sort_values('Abs_Correlation', ascending=False)
        else:
            return pd.DataFrame()

    def generate_insights(self, df: pd.DataFrame) -> List[str]:
        """Generate automated insights from the data."""
        insights = []

        # Data size insight
        profile = self.generate_profile(df)
        insights.append(f" Dataset contains {profile.n_rows:,} rows and {profile.n_columns} columns")

        # Missing data insights
        if profile.missing_percentage > 10:
            insights.append(f" High missing data: {profile.missing_percentage:.1f}% of cells are missing")
        elif profile.missing_percentage > 0:
            insights.append(f"ℹ Missing data: {profile.missing_percentage:.1f}% of cells are missing")

        # Duplicate insights
        if profile.duplicate_rows > 0:
            dup_pct = profile.duplicate_rows / profile.n_rows * 100
            insights.append(f" Found {profile.duplicate_rows:,} duplicate rows ({dup_pct:.1f}%)")

        # Numeric columns insights
        numeric_stats = self.analyze_numeric_columns(df)
        if not numeric_stats.empty:
            # Check for skewed distributions
            highly_skewed = numeric_stats[abs(numeric_stats['Skewness']) > 2]
            if not highly_skewed.empty:
                insights.append(f" {len(highly_skewed)} highly skewed numeric columns detected")

            # Check for columns with many zeros
            zero_heavy = numeric_stats[numeric_stats['Zeros_Pct'] > 50]
            if not zero_heavy.empty:
                insights.append(f"0⃣ {len(zero_heavy)} columns have >50% zeros")

        # Outlier insights
        outliers = self.detect_outliers(df)
        if outliers:
            total_outliers = sum(o['count'] for o in outliers.values())
            insights.append(f" Detected {total_outliers:,} outliers across {len(outliers)} columns")

        # Correlation insights
        high_corr = self.calculate_correlations(df, threshold=0.8)
        if not high_corr.empty:
            insights.append(f" Found {len(high_corr)} high correlations (>0.8)")

        # Categorical insights
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        if len(cat_cols) > 0:
            high_cardinality = [col for col in cat_cols if df[col].nunique() > 50]
            if high_cardinality:
                insights.append(f" {len(high_cardinality)} categorical columns with high cardinality (>50 unique values)")

        return insights

    def generate_report(
        self,
        df: pd.DataFrame,
        title: str = "Exploratory Data Analysis Report",
        output_file: Optional[str] = None
    ) -> str:
        """
        Generate comprehensive EDA report.

        Args:
            df: Input DataFrame
            title: Report title
            output_file: Optional file path to save report

        Returns:
            Report as string
        """
        report = []

        # Header
        report.append("=" * 80)
        report.append(title.center(80))
        report.append("=" * 80)
        report.append("")

        # 1. Data Profile
        report.append("## 1. DATA PROFILE")
        report.append("-" * 80)
        profile = self.generate_profile(df)
        for key, value in profile.__dict__.items():
            report.append(f"  {key.replace('_', ' ').title()}: {value}")
        report.append("")

        # 2. Automated Insights
        report.append("## 2. KEY INSIGHTS")
        report.append("-" * 80)
        insights = self.generate_insights(df)
        for insight in insights:
            report.append(f"  {insight}")
        report.append("")

        # 3. Missing Data Analysis
        missing = self.analyze_missing_data(df)
        if not missing.empty:
            report.append("## 3. MISSING DATA")
            report.append("-" * 80)
            report.append(missing.to_string(index=False))
            report.append("")

        # 4. Numeric Columns
        numeric_stats = self.analyze_numeric_columns(df)
        if not numeric_stats.empty:
            report.append("## 4. NUMERIC COLUMNS STATISTICS")
            report.append("-" * 80)
            report.append(numeric_stats.to_string(index=False))
            report.append("")

        # 5. Outliers
        outliers = self.detect_outliers(df)
        if outliers:
            report.append("## 5. OUTLIER DETECTION")
            report.append("-" * 80)
            for col, stats in outliers.items():
                report.append(f"  {col}: {stats['count']} outliers ({stats['percentage']:.2f}%)")
            report.append("")

        # 6. Correlations
        high_corr = self.calculate_correlations(df, threshold=0.7)
        if not high_corr.empty:
            report.append("## 6. HIGH CORRELATIONS (>0.7)")
            report.append("-" * 80)
            report.append(high_corr.to_string(index=False))
            report.append("")

        # 7. Categorical Analysis
        cat_analysis = self.analyze_categorical_columns(df)
        if cat_analysis:
            report.append("## 7. CATEGORICAL COLUMNS")
            report.append("-" * 80)
            for col, stats in cat_analysis.items():
                report.append(f"\n  {col}:")
                report.append(stats.to_string(index=False, max_rows=10))
            report.append("")

        report_text = "\n".join(report)

        # Save to file if specified
        if output_file:
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f" Report saved to {output_file}")

        return report_text


# Example usage
if __name__ == "__main__":
    # Create sample marketing campaign data
    np.random.seed(42)

    n_samples = 1000

    sample_data = pd.DataFrame({
        'campaign_id': [f'C{i:04d}' for i in range(n_samples)],
        'campaign_type': np.random.choice(['Email', 'Social', 'Search', 'Display'], n_samples),
        'budget': np.random.exponential(5000, n_samples),
        'impressions': np.random.poisson(10000, n_samples),
        'clicks': np.random.poisson(250, n_samples),
        'conversions': np.random.poisson(15, n_samples),
        'revenue': np.random.exponential(2000, n_samples),
        'industry': np.random.choice(['Tech', 'Finance', 'Healthcare', 'Retail', 'Manufacturing'], n_samples),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'start_date': pd.date_range('2025-01-01', periods=n_samples, freq='H')
    })

    # Add some missing values
    sample_data.loc[np.random.choice(n_samples, 50, replace=False), 'conversions'] = np.nan
    sample_data.loc[np.random.choice(n_samples, 30, replace=False), 'revenue'] = np.nan

    # Calculate derived metrics
    sample_data['ctr'] = sample_data['clicks'] / sample_data['impressions'] * 100
    sample_data['conversion_rate'] = sample_data['conversions'] / sample_data['clicks'] * 100
    sample_data['roas'] = sample_data['revenue'] / sample_data['budget']
    sample_data['cpc'] = sample_data['budget'] / sample_data['clicks']

    print("=" * 80)
    print("AUTOMATED EDA DEMO")
    print("=" * 80)

    # Generate EDA
    eda = EDAGenerator()

    report = eda.generate_report(
        df=sample_data,
        title="Marketing Campaign Performance Analysis",
        output_file="campaign_eda_report.txt"
    )

    print(report)

    print("\n" + "=" * 80)
    print("DETAILED STATISTICS")
    print("=" * 80)

    # Show numeric statistics
    print("\n Numeric Columns:")
    print(eda.analyze_numeric_columns(sample_data))

    # Show correlations
    print("\n Correlations:")
    corr = eda.calculate_correlations(sample_data, threshold=0.5)
    print(corr if not corr.empty else "No high correlations found")
