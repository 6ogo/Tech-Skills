"""
Prompt A/B Testing Framework
Compare prompt variations with statistical significance testing.
"""

import asyncio
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, asdict
from scipy import stats
import numpy as np
import pandas as pd


@dataclass
class PromptVariant:
    """A prompt variant for A/B testing."""
    id: str
    name: str
    template: str
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class TestResult:
    """Result from testing a single variant."""
    variant_id: str
    response: str
    latency_ms: float
    tokens_used: int
    cost: float
    quality_score: Optional[float] = None
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


class ABTest:
    """A/B test experiment for prompt variants."""

    def __init__(
        self,
        name: str,
        variants: List[PromptVariant],
        evaluation_fn: Optional[Callable] = None
    ):
        self.name = name
        self.variants = {v.id: v for v in variants}
        self.evaluation_fn = evaluation_fn or self._default_evaluation
        self.results: List[TestResult] = []

    def add_result(self, result: TestResult) -> None:
        """Add a test result."""
        self.results.append(result)

    def get_variant_results(self, variant_id: str) -> List[TestResult]:
        """Get all results for a specific variant."""
        return [r for r in self.results if r.variant_id == variant_id]

    def calculate_metrics(self, variant_id: str) -> Dict[str, float]:
        """Calculate aggregate metrics for a variant."""
        results = self.get_variant_results(variant_id)

        if not results:
            return {}

        return {
            "sample_size": len(results),
            "avg_latency_ms": np.mean([r.latency_ms for r in results]),
            "avg_cost": np.mean([r.cost for r in results]),
            "avg_tokens": np.mean([r.tokens_used for r in results]),
            "avg_quality_score": np.mean([r.quality_score for r in results if r.quality_score is not None]),
            "p50_latency": np.percentile([r.latency_ms for r in results], 50),
            "p95_latency": np.percentile([r.latency_ms for r in results], 95),
            "p99_latency": np.percentile([r.latency_ms for r in results], 99),
        }

    def compare_variants(
        self,
        variant_a_id: str,
        variant_b_id: str,
        metric: str = "quality_score"
    ) -> Dict[str, Any]:
        """
        Compare two variants with statistical significance testing.

        Args:
            variant_a_id: First variant ID
            variant_b_id: Second variant ID
            metric: Metric to compare ('quality_score', 'latency_ms', 'cost')

        Returns:
            Comparison results with p-value and effect size
        """
        results_a = self.get_variant_results(variant_a_id)
        results_b = self.get_variant_results(variant_b_id)

        if not results_a or not results_b:
            return {"error": "Insufficient data for comparison"}

        # Extract metric values
        values_a = [getattr(r, metric) for r in results_a if getattr(r, metric) is not None]
        values_b = [getattr(r, metric) for r in results_b if getattr(r, metric) is not None]

        if not values_a or not values_b:
            return {"error": f"No valid {metric} data"}

        # Perform t-test
        t_stat, p_value = stats.ttest_ind(values_a, values_b)

        # Calculate effect size (Cohen's d)
        pooled_std = np.sqrt((np.std(values_a)**2 + np.std(values_b)**2) / 2)
        cohens_d = (np.mean(values_a) - np.mean(values_b)) / pooled_std if pooled_std > 0 else 0

        # Determine winner
        if p_value < 0.05:
            if metric in ["latency_ms", "cost"]:
                # Lower is better
                winner = variant_a_id if np.mean(values_a) < np.mean(values_b) else variant_b_id
            else:
                # Higher is better
                winner = variant_a_id if np.mean(values_a) > np.mean(values_b) else variant_b_id
            significant = True
        else:
            winner = "No significant difference"
            significant = False

        return {
            "variant_a": {
                "id": variant_a_id,
                "mean": float(np.mean(values_a)),
                "std": float(np.std(values_a)),
                "sample_size": len(values_a)
            },
            "variant_b": {
                "id": variant_b_id,
                "mean": float(np.mean(values_b)),
                "std": float(np.std(values_b)),
                "sample_size": len(values_b)
            },
            "t_statistic": float(t_stat),
            "p_value": float(p_value),
            "cohens_d": float(cohens_d),
            "significant": significant,
            "winner": winner,
            "metric": metric,
            "improvement": float((np.mean(values_b) - np.mean(values_a)) / np.mean(values_a) * 100)
        }

    def generate_report(self) -> str:
        """Generate a comprehensive A/B test report."""
        lines = [
            f"📊 A/B Test Report: {self.name}",
            "=" * 80,
            f"Total Results: {len(self.results)}",
            f"Variants Tested: {len(self.variants)}",
            "\n"
        ]

        # Metrics for each variant
        lines.append("📈 Variant Performance:")
        for variant_id, variant in self.variants.items():
            metrics = self.calculate_metrics(variant_id)
            if metrics:
                lines.append(f"\n  {variant.name} (ID: {variant_id})")
                lines.append(f"    Sample Size: {metrics['sample_size']}")
                lines.append(f"    Avg Quality Score: {metrics['avg_quality_score']:.2f}")
                lines.append(f"    Avg Latency: {metrics['avg_latency_ms']:.0f}ms (p95: {metrics['p95_latency']:.0f}ms)")
                lines.append(f"    Avg Cost: ${metrics['avg_cost']:.4f}")
                lines.append(f"    Avg Tokens: {metrics['avg_tokens']:.0f}")

        # Statistical comparisons
        if len(self.variants) == 2:
            variant_ids = list(self.variants.keys())
            comparison = self.compare_variants(variant_ids[0], variant_ids[1])

            lines.append("\n\n🔬 Statistical Comparison:")
            lines.append(f"  Metric: {comparison.get('metric', 'N/A')}")
            lines.append(f"  P-Value: {comparison.get('p_value', 0):.4f}")
            lines.append(f"  Cohen's d: {comparison.get('cohens_d', 0):.3f}")
            lines.append(f"  Significant: {'Yes' if comparison.get('significant') else 'No'}")
            lines.append(f"  Winner: {comparison.get('winner', 'N/A')}")
            lines.append(f"  Improvement: {comparison.get('improvement', 0):.1f}%")

        return "\n".join(lines)

    def _default_evaluation(self, response: str) -> float:
        """Default quality evaluation (length-based)."""
        # Simple heuristic: penalize very short or very long responses
        length = len(response)
        if length < 50:
            return 50.0
        elif length > 2000:
            return 70.0
        else:
            return 85.0

    def export_results(self, filepath: str) -> None:
        """Export results to JSON file."""
        data = {
            "name": self.name,
            "variants": {k: asdict(v) for k, v in self.variants.items()},
            "results": [asdict(r) for r in self.results],
            "summary": {
                variant_id: self.calculate_metrics(variant_id)
                for variant_id in self.variants.keys()
            }
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"✅ Results exported to {filepath}")


class ABTestRunner:
    """Runner for executing A/B tests with actual LLM calls."""

    def __init__(self, llm_client: Optional[Any] = None):
        self.llm_client = llm_client

    async def run_test(
        self,
        test: ABTest,
        test_cases: List[Dict[str, Any]],
        samples_per_variant: int = 30
    ) -> ABTest:
        """
        Run an A/B test with multiple test cases.

        Args:
            test: The ABTest instance
            test_cases: List of test case dictionaries with template variables
            samples_per_variant: Number of samples to collect per variant

        Returns:
            The test instance with results
        """
        for variant_id, variant in test.variants.items():
            print(f"Testing variant: {variant.name} ({samples_per_variant} samples)")

            for i, test_case in enumerate(test_cases[:samples_per_variant]):
                # Render prompt with test case
                # In production, use actual template rendering
                prompt = variant.template.format(**test_case)

                # Simulate LLM call (replace with actual API call)
                result = await self._simulate_llm_call(prompt, variant_id)

                # Evaluate quality
                quality_score = test.evaluation_fn(result.response)
                result.quality_score = quality_score

                test.add_result(result)

                if (i + 1) % 10 == 0:
                    print(f"  Progress: {i + 1}/{samples_per_variant}")

        return test

    async def _simulate_llm_call(
        self,
        prompt: str,
        variant_id: str
    ) -> TestResult:
        """Simulate an LLM API call (replace with actual implementation)."""
        # In production, call actual LLM API here
        await asyncio.sleep(0.1)  # Simulate API latency

        # Generate mock response
        response = f"This is a simulated response for variant {variant_id}. " + "Sample content. " * 20

        return TestResult(
            variant_id=variant_id,
            response=response,
            latency_ms=np.random.uniform(200, 800),
            tokens_used=np.random.randint(100, 500),
            cost=np.random.uniform(0.001, 0.01)
        )


# Example usage
if __name__ == "__main__":
    # Define variants
    variant_a = PromptVariant(
        id="v1_concise",
        name="Concise Prompt",
        template="""Analyze this marketing campaign: {campaign_details}

Provide brief recommendations.""",
        metadata={"author": "Team A", "hypothesis": "Shorter prompts = faster responses"}
    )

    variant_b = PromptVariant(
        id="v2_detailed",
        name="Detailed Prompt",
        template="""You are a marketing analytics expert. Analyze the following campaign in detail.

Campaign Details: {campaign_details}

Please provide:
1. Performance assessment
2. Key insights
3. Specific recommendations
4. Action items

Be thorough and data-driven.""",
        metadata={"author": "Team B", "hypothesis": "Detailed prompts = better quality"}
    )

    # Create test
    test = ABTest(
        name="Marketing Prompt Optimization Q1 2025",
        variants=[variant_a, variant_b]
    )

    # Define test cases
    test_cases = [
        {
            "campaign_details": f"Campaign {i}: Budget $10K, CTR 2.5%, Conv 1.2%"
        }
        for i in range(50)
    ]

    # Run test
    runner = ABTestRunner()

    async def run():
        test_with_results = await runner.run_test(
            test=test,
            test_cases=test_cases,
            samples_per_variant=25
        )

        # Generate report
        print("\n" + test_with_results.generate_report())

        # Compare variants
        print("\n" + "=" * 80)
        comparison = test_with_results.compare_variants("v1_concise", "v2_detailed", "quality_score")
        print(f"\n🏆 Winner: {comparison['winner']}")
        print(f"📊 Statistical Significance: {'Yes ✓' if comparison['significant'] else 'No ✗'}")
        print(f"📈 Improvement: {comparison['improvement']:.1f}%")

        # Export results
        test_with_results.export_results("ab_test_results.json")

    # Run async test
    asyncio.run(run())
