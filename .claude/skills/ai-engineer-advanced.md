# AI Engineer - Advanced Skills

Extended skills for AI Engineer covering fine-tuning, multimodal, advanced agents, and local LLMs.

## 🎯 Trigger Keywords

- "fine-tune", "LoRA", "QLoRA", "PEFT", "custom model"
- "multimodal", "vision", "image", "audio", "video"
- "MCP", "tool use", "function calling", "planning"
- "local LLM", "Ollama", "vLLM", "on-prem"
- "synthetic data", "data generation"

---

## ai-09: Fine-Tuning & Custom Models

### When to Use

- Need model customized for specific domain/task
- Want consistent output format/style
- Need to reduce token costs with smaller fine-tuned model
- Require specialized knowledge not in base model

### Skills

```yaml
fine_tuning:
  techniques:
    - LoRA (Low-Rank Adaptation)
    - QLoRA (Quantized LoRA)
    - PEFT (Parameter-Efficient Fine-Tuning)
    - Full fine-tuning (when resources allow)

  platforms:
    - OpenAI Fine-tuning API
    - Azure OpenAI Fine-tuning
    - Hugging Face Transformers
    - Axolotl (advanced configs)
    - Unsloth (fast LoRA)

  dataset_prep:
    - Quality over quantity
    - Diverse examples
    - Consistent format (ChatML, Alpaca)
    - Validation split (10-20%)

  best_practices:
    - Start with 100-500 high-quality examples
    - Use LoRA for cost efficiency (90% cheaper)
    - Monitor loss curves for overfitting
    - A/B test against base model
    - Track with MLflow/W&B
```

### Cost Optimization

```yaml
savings:
  - Fine-tuned small model vs GPT-4: 95% cost reduction
  - LoRA vs full fine-tune: 90% compute reduction
  - Quantization (4-bit): 75% memory reduction
```

### Integration

```
→ mo-02 (MLOps): Experiment tracking
→ mo-03 (MLOps): Model registry
→ fo-07 (FinOps): Training cost tracking
→ sa-01 (Security): PII removal from training data
```

---

## ai-10: Multimodal AI

### When to Use

- Processing images alongside text
- Video analysis or generation
- Audio transcription/generation
- Document understanding (PDFs with images)

### Skills

```yaml
multimodal:
  vision_language:
    - GPT-4 Vision
    - Claude 3 Vision
    - LLaVA (open source)
    - Gemini Pro Vision

  image_generation:
    - DALL-E 3
    - Midjourney API
    - Stable Diffusion
    - Flux

  audio:
    - Whisper (transcription)
    - ElevenLabs (TTS)
    - Bark (open source TTS)

  video:
    - Video understanding (Gemini)
    - Video generation (Runway, Pika)
    - Frame extraction + vision

  document:
    - PDF parsing with images
    - Table extraction
    - Chart/graph understanding
    - OCR + LLM combination
```

### Best Practices

```yaml
vision:
  - Resize images to optimal resolution (minimize tokens)
  - Use base64 encoding for inline, URLs for large
  - Describe expected output format
  - Handle multi-page documents sequentially

audio:
  - Chunk long audio (< 25MB for Whisper)
  - Use diarization for multi-speaker
  - Normalize audio quality

cost_optimization:
  - Compress images before processing
  - Use cheaper models for classification
  - Cache repeated analyses
```

### Integration

```
→ de-02 (Data): Media pipelines
→ ai-04 (AI): Content moderation
→ fo-07 (FinOps): Multimodal cost tracking
```

---

## ai-11: AI Agents 2.0 (MCP & Advanced)

### When to Use

- Complex multi-step reasoning
- Tool/API orchestration
- Autonomous task execution
- Persistent memory across sessions

### Skills

```yaml
agents_v2:
  mcp_integration:
    description: "Model Context Protocol for tool use"
    capabilities:
      - Dynamic server activation
      - Tool discovery
      - Resource management
      - Prompt injection
    servers:
      - filesystem (file operations)
      - github (repo management)
      - postgres (database)
      - fetch (web content)
      - puppeteer (browser)

  advanced_reasoning:
    - ReAct (Reasoning + Acting)
    - Chain-of-Thought (CoT)
    - Tree-of-Thoughts (ToT)
    - Self-Consistency
    - Reflexion (self-improvement)

  memory_systems:
    - Short-term (conversation)
    - Long-term (vector store)
    - Episodic (experience replay)
    - Semantic (knowledge graph)
    - Procedural (learned workflows)

  planning:
    - Task decomposition
    - Goal-directed planning
    - Backtracking on failure
    - Parallel execution
    - Resource scheduling

  tool_use:
    - Function calling (OpenAI, Anthropic)
    - MCP servers
    - Custom tool definition
    - Error handling & retry
    - Rate limiting
```

### MCP Best Practices

```yaml
efficiency:
  - Activate MCP servers on-demand only
  - Deactivate immediately after use
  - Fetch minimal required data
  - Cache repeated operations

security:
  - Validate tool inputs
  - Limit tool permissions
  - Audit all tool calls
  - Sandbox dangerous operations
```

### Integration

```
→ mcp-01 to mcp-05: MCP management
→ ai-04: Guardrails for agent actions
→ mo-06: Agent observability
→ sa-02: Threat model for agents
```

---

## ai-12: Local LLMs & On-Prem

### When to Use

- Data cannot leave premises (compliance)
- Need offline capability
- Cost optimization for high volume
- Privacy-sensitive applications

### Skills

```yaml
local_llms:
  inference_servers:
    - Ollama (easiest setup)
    - vLLM (production speed)
    - Text Generation Inference (HuggingFace)
    - llama.cpp (CPU/low resource)
    - LocalAI (OpenAI-compatible)

  models:
    - Llama 3.x (Meta)
    - Mistral/Mixtral
    - Qwen 2.x
    - Phi-3 (Microsoft)
    - CodeLlama/DeepSeek Coder

  quantization:
    - GGUF format (llama.cpp)
    - AWQ (activation-aware)
    - GPTQ (post-training)
    - 4-bit, 8-bit options

  deployment:
    - Docker containers
    - Kubernetes (scaling)
    - GPU optimization (CUDA)
    - CPU fallback (AVX2)

  hybrid:
    - Local for privacy-sensitive
    - Cloud for complex reasoning
    - Routing based on task type
```

### Best Practices

```yaml
performance:
  - Use quantized models (4-bit for speed)
  - Enable KV cache
  - Batch requests when possible
  - Profile GPU memory usage

cost:
  - Local GPU: $0.001/1K tokens (vs $0.01+ cloud)
  - Amortized hardware cost
  - No per-token API costs

security:
  - Data never leaves network
  - Air-gapped deployments possible
  - Audit logs stay internal
```

### Integration

```
→ do-02 (DevOps): Container deployment
→ pe-01 (Platform): GPU resource management
→ sa-06 (Security): On-prem secrets
→ fo-01 (FinOps): TCO analysis
```

---

## ai-13: Synthetic Data Generation

### When to Use

- Need training data for fine-tuning
- Augment limited real data
- Create test datasets
- Generate evaluation benchmarks

### Skills

```yaml
synthetic_data:
  generation_methods:
    - LLM-based generation
    - Template expansion
    - Paraphrasing
    - Back-translation
    - Self-instruct

  quality_control:
    - Diversity metrics
    - Quality scoring
    - Deduplication
    - Human validation sample

  use_cases:
    - Fine-tuning datasets
    - Evaluation benchmarks
    - Test data for QA
    - Privacy-safe alternatives
    - Edge case generation

  frameworks:
    - Distilabel (HuggingFace)
    - Self-Instruct
    - Evol-Instruct
    - Custom pipelines
```

### Best Practices

```yaml
quality:
  - Validate 5-10% manually
  - Check for repetition/collapse
  - Ensure diversity (topics, styles)
  - Remove low-quality samples

ethics:
  - Don't claim synthetic data is real
  - Document generation method
  - Check for bias amplification
  - PII removal from seeds
```

### Integration

```
→ ai-09: For fine-tuning with synthetic data
→ ai-06: Evaluate synthetic data quality
→ sa-01: PII removal from seed data
→ dg-03: Data quality framework
```

---

## Skill Dependencies

| Skill              | Requires      | Enables            |
| ------------------ | ------------- | ------------------ |
| ai-09 (Fine-tune)  | mo-02, sa-01  | Custom models      |
| ai-10 (Multimodal) | de-02, fo-07  | Vision/audio apps  |
| ai-11 (Agents 2.0) | mcp-\*, ai-04 | Autonomous systems |
| ai-12 (Local LLMs) | do-02, pe-01  | On-prem AI         |
| ai-13 (Synthetic)  | ai-06, dg-03  | Training data      |

## Quick Reference

```yaml
# When to use which skill
fine_tuning: "I need a custom model for my use case"
multimodal: "I need to process images/audio/video"
agents_v2: "I need autonomous multi-step execution"
local_llms: "I need to run AI on-premises"
synthetic: "I need to generate training data"
```
