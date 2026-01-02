"""
Token Cost Estimator for Multiple LLM Providers
Calculate and compare costs across OpenAI, Anthropic, Google, and more.
"""

import tiktoken
from typing import Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Provider(Enum):
    """Supported LLM providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    META = "meta"
    MISTRAL = "mistral"


@dataclass
class ModelPricing:
    """Pricing information for a model."""
    input_cost_per_1k: float  # Cost per 1K input tokens
    output_cost_per_1k: float  # Cost per 1K output tokens
    context_window: int  # Maximum context window in tokens


# Pricing as of December 2025 (prices in USD)
PRICING_TABLE: Dict[str, ModelPricing] = {
    # OpenAI
    "gpt-4-turbo": ModelPricing(0.01, 0.03, 128000),
    "gpt-4": ModelPricing(0.03, 0.06, 8192),
    "gpt-3.5-turbo": ModelPricing(0.0005, 0.0015, 16385),
    "gpt-4o": ModelPricing(0.005, 0.015, 128000),
    "gpt-4o-mini": ModelPricing(0.00015, 0.0006, 128000),

    # Anthropic
    "claude-opus-4": ModelPricing(0.015, 0.075, 200000),
    "claude-sonnet-4": ModelPricing(0.003, 0.015, 200000),
    "claude-haiku-4": ModelPricing(0.00025, 0.00125, 200000),
    "claude-3-opus": ModelPricing(0.015, 0.075, 200000),
    "claude-3-sonnet": ModelPricing(0.003, 0.015, 200000),
    "claude-3-haiku": ModelPricing(0.00025, 0.00125, 200000),

    # Google
    "gemini-pro": ModelPricing(0.000125, 0.000375, 32760),
    "gemini-pro-vision": ModelPricing(0.000125, 0.000375, 16384),
    "gemini-ultra": ModelPricing(0.001, 0.002, 32760),
    "gemini-1.5-pro": ModelPricing(0.00125, 0.005, 1000000),
    "gemini-1.5-flash": ModelPricing(0.000125, 0.0005, 1000000),

    # Meta (via hosting providers - example pricing)
    "llama-3-70b": ModelPricing(0.0007, 0.0009, 8192),
    "llama-3-8b": ModelPricing(0.0002, 0.0002, 8192),

    # Mistral
    "mistral-large": ModelPricing(0.004, 0.012, 32000),
    "mistral-medium": ModelPricing(0.0027, 0.0081, 32000),
    "mistral-small": ModelPricing(0.001, 0.003, 32000),
}


class TokenCounter:
    """Count tokens for different providers."""

    def __init__(self):
        self.encoders = {
            Provider.OPENAI: tiktoken.get_encoding("cl100k_base"),
            # For other providers, we approximate with cl100k_base
            # In production, use provider-specific tokenizers
        }

    def count_tokens(self, text: str, provider: Provider = Provider.OPENAI) -> int:
        """Count tokens in text."""
        encoder = self.encoders.get(provider, self.encoders[Provider.OPENAI])
        return len(encoder.encode(text))

    def count_tokens_for_messages(
        self,
        messages: list,
        model: str = "gpt-4"
    ) -> int:
        """Count tokens for chat completion messages."""
        encoding = tiktoken.encoding_for_model(model)

        # Token counting varies by model
        if "gpt-4" in model or "gpt-3.5" in model:
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            tokens_per_message = 3
            tokens_per_name = 1

        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(str(value)))
                if key == "name":
                    num_tokens += tokens_per_name

        num_tokens += 3  # every reply is primed with assistant
        return num_tokens


class CostEstimator:
    """Estimate costs for LLM API calls."""

    def __init__(self):
        self.token_counter = TokenCounter()

    def estimate_cost(
        self,
        input_text: str,
        model: str,
        estimated_output_tokens: int = 0,
        provider: Optional[Provider] = None
    ) -> Dict[str, float]:
        """
        Estimate the cost of an LLM API call.

        Args:
            input_text: The input prompt
            model: Model name (e.g., 'gpt-4', 'claude-3-opus')
            estimated_output_tokens: Expected output length
            provider: LLM provider (auto-detected if None)

        Returns:
            Dictionary with cost breakdown
        """
        # Auto-detect provider if not specified
        if provider is None:
            provider = self._detect_provider(model)

        # Get pricing info
        pricing = PRICING_TABLE.get(model)
        if not pricing:
            raise ValueError(f"Unknown model: {model}")

        # Count input tokens
        input_tokens = self.token_counter.count_tokens(input_text, provider)

        # Calculate costs
        input_cost = (input_tokens / 1000) * pricing.input_cost_per_1k
        output_cost = (estimated_output_tokens / 1000) * pricing.output_cost_per_1k
        total_cost = input_cost + output_cost

        return {
            "input_tokens": input_tokens,
            "output_tokens": estimated_output_tokens,
            "total_tokens": input_tokens + estimated_output_tokens,
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": total_cost,
            "currency": "USD",
            "model": model,
            "context_window": pricing.context_window,
            "context_utilization": (input_tokens + estimated_output_tokens) / pricing.context_window
        }

    def compare_models(
        self,
        input_text: str,
        models: list,
        estimated_output_tokens: int = 500
    ) -> Dict[str, Dict[str, float]]:
        """Compare costs across multiple models."""
        comparisons = {}

        for model in models:
            try:
                cost = self.estimate_cost(input_text, model, estimated_output_tokens)
                comparisons[model] = cost
            except ValueError as e:
                comparisons[model] = {"error": str(e)}

        return comparisons

    def _detect_provider(self, model: str) -> Provider:
        """Auto-detect provider from model name."""
        if "gpt" in model.lower():
            return Provider.OPENAI
        elif "claude" in model.lower():
            return Provider.ANTHROPIC
        elif "gemini" in model.lower():
            return Provider.GOOGLE
        elif "llama" in model.lower():
            return Provider.META
        elif "mistral" in model.lower():
            return Provider.MISTRAL
        else:
            return Provider.OPENAI  # Default

    def estimate_monthly_cost(
        self,
        queries_per_day: int,
        avg_input_tokens: int,
        avg_output_tokens: int,
        model: str
    ) -> Dict[str, float]:
        """Estimate monthly costs based on usage patterns."""
        pricing = PRICING_TABLE.get(model)
        if not pricing:
            raise ValueError(f"Unknown model: {model}")

        # Daily costs
        daily_input_cost = (queries_per_day * avg_input_tokens / 1000) * pricing.input_cost_per_1k
        daily_output_cost = (queries_per_day * avg_output_tokens / 1000) * pricing.output_cost_per_1k
        daily_cost = daily_input_cost + daily_output_cost

        # Monthly projection (30 days)
        monthly_cost = daily_cost * 30

        return {
            "queries_per_day": queries_per_day,
            "daily_cost": daily_cost,
            "monthly_cost": monthly_cost,
            "yearly_cost": monthly_cost * 12,
            "cost_per_query": daily_cost / queries_per_day,
            "model": model
        }


def format_cost_comparison(comparisons: Dict[str, Dict[str, float]]) -> str:
    """Format cost comparison for display."""
    lines = [" Cost Comparison", "=" * 70]

    # Sort by total cost
    sorted_models = sorted(
        [(k, v) for k, v in comparisons.items() if "error" not in v],
        key=lambda x: x[1]["total_cost"]
    )

    for model, cost in sorted_models:
        lines.append(f"\n {model}")
        lines.append(f"  Input:  {cost['input_tokens']:,} tokens → ${cost['input_cost']:.6f}")
        lines.append(f"  Output: {cost['output_tokens']:,} tokens → ${cost['output_cost']:.6f}")
        lines.append(f"  Total:  ${cost['total_cost']:.6f}")
        lines.append(f"  Context: {cost['context_utilization']:.1%} utilized")

    return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    estimator = CostEstimator()

    # Example prompt
    prompt = """Analyze this marketing campaign and provide detailed recommendations:

    Campaign: Summer Sale 2025
    Budget: $50,000
    Duration: 30 days
    Channels: Email, Social Media, Search Ads

    Current Metrics (Week 1):
    - Impressions: 1,200,000
    - Clicks: 24,000 (CTR: 2%)
    - Conversions: 480 (Conv Rate: 2%)
    - Revenue: $48,000
    - ROAS: 0.96

    Please provide:
    1. Performance analysis
    2. Optimization recommendations
    3. Budget reallocation strategy
    4. Projected outcomes
    """

    # Single model estimate
    print("=" * 70)
    print(" Single Model Estimation")
    print("=" * 70)

    cost = estimator.estimate_cost(
        input_text=prompt,
        model="gpt-4o",
        estimated_output_tokens=1000
    )

    print(f"\nModel: {cost['model']}")
    print(f"Input tokens: {cost['input_tokens']:,}")
    print(f"Estimated output tokens: {cost['output_tokens']:,}")
    print(f"Total cost: ${cost['total_cost']:.4f}")
    print(f"Context utilization: {cost['context_utilization']:.1%}")

    # Compare multiple models
    print("\n" + "=" * 70)
    models_to_compare = [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-sonnet-4",
        "claude-haiku-4",
        "gemini-1.5-pro",
        "gemini-1.5-flash"
    ]

    comparisons = estimator.compare_models(
        input_text=prompt,
        models=models_to_compare,
        estimated_output_tokens=1000
    )

    print(format_cost_comparison(comparisons))

    # Monthly cost projection
    print("\n" + "=" * 70)
    print(" Monthly Cost Projection")
    print("=" * 70)

    monthly = estimator.estimate_monthly_cost(
        queries_per_day=1000,
        avg_input_tokens=500,
        avg_output_tokens=800,
        model="gpt-4o"
    )

    print(f"\nModel: {monthly['model']}")
    print(f"Queries per day: {monthly['queries_per_day']:,}")
    print(f"Daily cost: ${monthly['daily_cost']:.2f}")
    print(f"Monthly cost: ${monthly['monthly_cost']:.2f}")
    print(f"Yearly cost: ${monthly['yearly_cost']:,.2f}")
    print(f"Cost per query: ${monthly['cost_per_query']:.4f}")
