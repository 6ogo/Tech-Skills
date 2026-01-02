# Skill 3: LLM Agent Orchestration

##  Overview
Build advanced multi-agent systems with autonomous task delegation, tool execution, and intelligent workflow orchestration for complex AI applications.

##  Connections
- **Data Engineer**: Agent state persistence, conversation history storage (de-01, de-03)
- **Security Architect**: Tool execution sandboxing, agent permission management (sa-02, sa-08)
- **ML Engineer**: Agent model selection and optimization (ml-03, ml-04)
- **MLOps**: Agent performance tracking, multi-agent metrics (mo-01, mo-04)
- **FinOps**: Multi-agent cost attribution, tool execution cost tracking (fo-01, fo-07)
- **DevOps**: Agent deployment, horizontal scaling for agent clusters (do-01, do-03)
- **Data Scientist**: Agent behavior analysis, conversation analytics (ds-01, ds-08)

##  Tools Included

### 1. `agent_orchestrator.py`
Multi-agent coordination system with task delegation, conversation routing, and state management.

### 2. `tool_registry.py`
Centralized tool registry for agent function calling with versioning and permission controls.

### 3. `agent_memory.py`
Short-term and long-term memory management with vector-based conversation retrieval.

### 4. `workflow_executor.py`
Sequential and parallel workflow execution for complex multi-step agent tasks.

### 5. `agent_monitor.py`
Real-time agent performance monitoring with cost tracking and quality metrics.

##  Key Metrics
- Agent task completion rate
- Tool execution success rate
- Multi-agent coordination latency
- Agent decision quality score
- Cost per agent interaction

##  Quick Start

```python
from agent_orchestrator import AgentOrchestrator, Agent

# Define specialized agents
research_agent = Agent(
    name="research_agent",
    model="claude-3-5-sonnet-20241022",
    tools=["web_search", "document_retrieval"],
    system_prompt="You are a research specialist..."
)

coding_agent = Agent(
    name="coding_agent",
    model="claude-3-5-sonnet-20241022",
    tools=["code_executor", "github_api"],
    system_prompt="You are a coding specialist..."
)

# Initialize orchestrator
orchestrator = AgentOrchestrator(
    agents=[research_agent, coding_agent],
    router_model="claude-3-5-sonnet-20241022"
)

# Execute complex task with automatic routing
result = orchestrator.execute(
    task="Research best practices for rate limiting and implement them",
    max_iterations=10
)

print(f"Result: {result.output}")
print(f"Agents used: {result.agents_invoked}")
print(f"Total cost: ${result.total_cost:.4f}")
```

##  Best Practices

### Cost Optimization (FinOps Integration)

1. **Agent-Level Cost Attribution**
   - Track costs per agent type and conversation
   - Identify expensive agent patterns
   - Optimize model selection per agent role
   - Monitor tool execution costs separately
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Optimize Agent Routing**
   - Use lightweight router model for task delegation
   - Cache routing decisions for similar queries
   - Minimize unnecessary agent hand-offs
   - Implement early termination for simple tasks
   - Reference: FinOps fo-03 (Budget Management)

3. **Tool Execution Optimization**
   - Cache tool results for frequent calls
   - Batch API calls where possible
   - Use cheaper alternatives for validation tasks
   - Track and optimize expensive tool chains
   - Reference: FinOps fo-01 (Cost Monitoring)

4. **Prompt Caching for Agents**
   - Cache agent system prompts (90% savings)
   - Cache tool schemas and examples
   - Reuse conversation context across turns
   - Implement semantic caching for agent responses
   - Reference: ai-01 (Prompt Caching), FinOps fo-07

### Security & Privacy (Security Architect Integration)

5. **Tool Execution Sandboxing**
   - Isolate tool execution environments
   - Implement strict permission controls
   - Validate all tool inputs and outputs
   - Monitor for malicious tool usage patterns
   - Reference: Security Architect sa-08 (LLM Security)

6. **Agent Permission Management**
   - Define granular RBAC for each agent
   - Restrict tool access based on agent role
   - Audit all agent actions and decisions
   - Implement least privilege principle
   - Reference: Security Architect sa-02 (IAM)

7. **Prevent Agent Jailbreaking**
   - Validate agent outputs before execution
   - Implement safety filters on tool calls
   - Monitor for prompt injection in agent inputs
   - Log suspicious agent behavior
   - Reference: Security Architect sa-08 (LLM Security)

### Data Quality & Governance (Data Engineer Integration)

8. **Conversation State Management**
   - Persist agent conversation history
   - Implement state recovery mechanisms
   - Version conversation schemas
   - Track conversation lineage
   - Reference: Data Engineer de-01 (Data Ingestion)

9. **Agent Output Validation**
   - Validate structured outputs from agents
   - Implement data quality checks on tool results
   - Monitor output consistency across agents
   - Track data transformation quality
   - Reference: Data Engineer de-03 (Data Quality)

### Model Lifecycle Management (MLOps Integration)

10. **Agent Model Versioning**
    - Version each agent's model configuration
    - Track model changes and performance impacts
    - Implement A/B testing for agent models
    - Rollback capability for agent updates
    - Reference: MLOps mo-01 (Model Registry), mo-03 (Versioning)

11. **Multi-Agent Performance Monitoring**
    - Track task completion rates per agent
    - Monitor agent collaboration efficiency
    - Measure end-to-end workflow latency
    - Alert on agent performance degradation
    - Reference: MLOps mo-04 (Monitoring)

12. **Agent Behavior Drift Detection**
    - Monitor agent decision patterns over time
    - Detect changes in tool usage patterns
    - Alert on unexpected agent behavior
    - Track agent quality metrics trends
    - Reference: MLOps mo-05 (Drift Detection)

### Deployment & Operations (DevOps Integration)

13. **Containerize Agent Services**
    - Package each agent as microservice
    - Use Docker for local development
    - Deploy to AKS with auto-scaling
    - Implement health checks for agents
    - Reference: DevOps do-03 (Containerization)

14. **CI/CD for Agent Updates**
    - Automate agent deployment pipeline
    - Implement canary deployments for agents
    - Test agent interactions before production
    - Rollback failed agent deployments
    - Reference: DevOps do-01 (CI/CD), do-05 (GitOps)

15. **Observability for Multi-Agent Systems**
    - Instrument agents with OpenTelemetry
    - Trace agent-to-agent communication
    - Monitor agent resource utilization
    - Set up distributed tracing dashboards
    - Reference: DevOps do-08 (Monitoring & Observability)

### Azure-Specific Best Practices

16. **Leverage Azure OpenAI for Agents**
    - Use managed identity for agent authentication
    - Deploy agents in Azure Container Apps
    - Enable diagnostic logging for all agents
    - Use Azure API Management for tool APIs
    - Reference: Azure az-05 (Azure OpenAI)

17. **Azure State Management**
    - Use Azure Cosmos DB for agent state
    - Implement Azure Service Bus for agent messaging
    - Store conversation history in Azure Storage
    - Use Azure Redis for agent caching
    - Reference: Azure az-03 (Storage), az-07 (Networking)

##  Cost Optimization Examples

### Agent Cost Attribution
```python
from agent_orchestrator import AgentOrchestrator
from cost_tracker import AgentCostTracker

cost_tracker = AgentCostTracker()

# Track costs per agent
def execute_with_cost_tracking(task: str, session_id: str):
    result = orchestrator.execute(
        task=task,
        cost_callback=lambda agent, cost: cost_tracker.log_agent_cost(
            session_id=session_id,
            agent_name=agent.name,
            model=agent.model,
            cost=cost
        )
    )

    # Generate cost breakdown
    breakdown = cost_tracker.get_session_breakdown(session_id)
    print(f"\n Cost Breakdown:")
    for agent_name, metrics in breakdown.items():
        print(f"  {agent_name}:")
        print(f"    - Model calls: {metrics.num_calls}")
        print(f"    - Total cost: ${metrics.total_cost:.4f}")
        print(f"    - Avg cost/call: ${metrics.avg_cost:.4f}")

    return result

# Set budget alerts per agent
cost_tracker.set_agent_budget(
    agent_name="research_agent",
    daily_budget=10.00,
    alert_threshold=0.8
)
```

### Prompt Caching for Agents (90% Savings)
```python
from anthropic import Anthropic

client = Anthropic()

def create_agent_with_caching(agent_config: dict):
    """Create agent with cached system prompt and tool schemas."""

    # Cache system prompt
    system_blocks = [
        {
            "type": "text",
            "text": agent_config["system_prompt"],
            "cache_control": {"type": "ephemeral"}
        }
    ]

    # Cache tool schemas
    if agent_config.get("tools"):
        tools_text = json.dumps(agent_config["tools"], indent=2)
        system_blocks.append({
            "type": "text",
            "text": f"Available tools:\n{tools_text}",
            "cache_control": {"type": "ephemeral"}
        })

    def execute_agent(user_message: str, conversation_history: list = None):
        messages = conversation_history or []
        messages.append({"role": "user", "content": user_message})

        response = client.messages.create(
            model=agent_config["model"],
            max_tokens=4096,
            system=system_blocks,
            messages=messages,
            tools=agent_config.get("tools")
        )

        # Log cache performance
        usage = response.usage
        cache_creation_tokens = getattr(usage, 'cache_creation_input_tokens', 0)
        cache_read_tokens = getattr(usage, 'cache_read_input_tokens', 0)

        print(f"Cache stats: {cache_read_tokens} read, {cache_creation_tokens} created")

        return response

    return execute_agent
```

### Tool Execution Cost Optimization
```python
from tool_registry import ToolRegistry
from functools import lru_cache
import hashlib

class CostOptimizedToolRegistry(ToolRegistry):
    def __init__(self):
        super().__init__()
        self.execution_cache = {}

    def execute_tool(self, tool_name: str, params: dict):
        # Cache deterministic tool results
        if self.is_deterministic(tool_name):
            cache_key = self._get_cache_key(tool_name, params)

            if cache_key in self.execution_cache:
                print(f" Cache hit for {tool_name}")
                return self.execution_cache[cache_key]

        # Execute tool
        result = super().execute_tool(tool_name, params)

        # Cache result
        if self.is_deterministic(tool_name):
            self.execution_cache[cache_key] = result

        # Track costs
        cost = self._estimate_tool_cost(tool_name, params, result)
        self.log_tool_cost(tool_name, cost)

        return result

    def _get_cache_key(self, tool_name: str, params: dict) -> str:
        """Generate cache key from tool name and params."""
        params_str = json.dumps(params, sort_keys=True)
        return hashlib.md5(f"{tool_name}:{params_str}".encode()).hexdigest()

    def get_tool_cost_report(self) -> dict:
        """Generate cost report by tool."""
        return {
            tool: {
                "executions": metrics.count,
                "total_cost": metrics.total_cost,
                "avg_cost": metrics.avg_cost
            }
            for tool, metrics in self.tool_metrics.items()
        }
```

##  Security Best Practices Examples

### Tool Execution Sandboxing
```python
from tool_registry import ToolRegistry
from security_sandbox import ToolSandbox  # from sa-08

class SecureToolRegistry(ToolRegistry):
    def __init__(self):
        super().__init__()
        self.sandbox = ToolSandbox()

    def execute_tool(self, tool_name: str, params: dict, agent_id: str):
        # Validate agent permissions
        if not self.has_permission(agent_id, tool_name):
            raise PermissionError(f"Agent {agent_id} not authorized for {tool_name}")

        # Validate inputs
        validation_result = self.validate_tool_params(tool_name, params)
        if not validation_result.valid:
            raise ValueError(f"Invalid params: {validation_result.errors}")

        # Execute in sandbox
        result = self.sandbox.execute(
            tool_name=tool_name,
            params=params,
            timeout=30,
            max_memory_mb=512,
            network_access=self.requires_network(tool_name)
        )

        # Validate outputs
        if not self.validate_tool_output(tool_name, result):
            raise ValueError(f"Tool output failed validation")

        # Audit log
        self.audit_log.record({
            "timestamp": datetime.now(),
            "agent_id": agent_id,
            "tool_name": tool_name,
            "params": params,
            "success": result.success,
            "duration_ms": result.duration_ms
        })

        return result.output

# Define tool permissions
registry = SecureToolRegistry()
registry.set_tool_permissions("research_agent", [
    "web_search",
    "document_retrieval"
])
registry.set_tool_permissions("coding_agent", [
    "code_executor",
    "github_api",
    "file_operations"
])
```

### Agent Input Validation
```python
from pii_detector import PIIDetector  # from sa-01
from prompt_injection_detector import PromptInjectionDetector  # from sa-08

class SecureAgentOrchestrator(AgentOrchestrator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pii_detector = PIIDetector()
        self.injection_detector = PromptInjectionDetector()

    def execute(self, task: str, user_context: dict = None):
        # Check for PII in user input
        pii_findings = self.pii_detector.analyze_text(task)
        if pii_findings:
            # Redact or alert
            print(f" PII detected in user input: {pii_findings}")
            task = self.pii_detector.redact_text(task, pii_findings)

        # Check for prompt injection
        injection_score = self.injection_detector.analyze(task)
        if injection_score > 0.8:
            raise SecurityError("Potential prompt injection detected")

        # Execute with validation
        result = super().execute(task, user_context)

        # Validate agent outputs before returning
        if not self.validate_output(result.output):
            raise ValueError("Agent output failed safety checks")

        return result
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Agent Performance** | Task completion rate | >0.95 | Custom monitor |
| | Agent response time (p95) | <5s | Azure Monitor |
| | Multi-agent coordination time | <10s | App Insights |
| | Agent decision accuracy | >0.90 | MLflow |
| **Tool Execution** | Tool success rate | >0.98 | Custom tracker |
| | Tool execution time (p95) | <2s | App Insights |
| | Tool cache hit rate | >60% | Redis metrics |
| **Costs** | Cost per agent interaction | <$0.10 | FinOps dashboard |
| | Cost per tool execution | <$0.01 | Cost tracker |
| | Cache savings percentage | >70% | Cost analyzer |
| **Quality** | Agent handoff accuracy | >0.92 | MLflow |
| | Workflow success rate | >0.95 | Custom monitor |
| | Output validation pass rate | >0.99 | Quality tracker |
| **Security** | Permission violations | 0 | Security logs |
| | Sandbox escapes | 0 | Security monitor |
| | Injection attempts blocked | 100% | WAF logs |

##  Deployment Pipeline

### CI/CD for Multi-Agent System
```yaml
# .github/workflows/agent-deployment.yml
name: Agent Orchestration Deployment

on:
  push:
    paths:
      - 'agents/**'
      - 'tools/**'
    branches:
      - main

jobs:
  test-agents:
    runs-on: ubuntu-latest
    steps:
      - name: Unit test agents
        run: pytest tests/test_agents.py -v

      - name: Integration test agent coordination
        run: pytest tests/test_agent_orchestration.py -v

      - name: Test tool execution sandbox
        run: pytest tests/test_tool_security.py -v

      - name: Validate agent permissions
        run: python scripts/validate_permissions.py

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Scan for security vulnerabilities
        run: python scripts/security_scan.py

      - name: Test prompt injection detection
        run: pytest tests/test_prompt_injection.py

      - name: Validate tool sandboxing
        run: python scripts/test_sandbox.py

  deploy-staging:
    needs: [test-agents, security-scan]
    runs-on: ubuntu-latest
    steps:
      - name: Build agent containers
        run: |
          docker build -t agent-orchestrator:${{ github.sha }} .
          docker build -t tool-registry:${{ github.sha }} ./tools

      - name: Push to Azure Container Registry
        run: |
          az acr login --name myregistry
          docker push agent-orchestrator:${{ github.sha }}

      - name: Deploy to AKS staging
        run: |
          kubectl set image deployment/agent-orchestrator \
            agent-orchestrator=myregistry.azurecr.io/agent-orchestrator:${{ github.sha }} \
            --namespace staging

      - name: Run smoke tests
        run: python scripts/smoke_test_agents.py --environment staging

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Canary deployment (10%)
        run: |
          kubectl set image deployment/agent-orchestrator \
            agent-orchestrator=myregistry.azurecr.io/agent-orchestrator:${{ github.sha }} \
            --namespace production
          kubectl patch deployment agent-orchestrator \
            -p '{"spec":{"replicas":1}}' --namespace production

      - name: Monitor canary metrics
        run: python scripts/monitor_canary.py --duration 30m

      - name: Full production rollout
        if: success()
        run: kubectl scale deployment agent-orchestrator --replicas=10 --namespace production

      - name: Monitor production agents
        run: python scripts/monitor_agents.py --duration 2h
```

##  Integration Workflow

### End-to-End Multi-Agent Pipeline with All Roles
```
1. User Request Received
   ↓
2. Input Validation & PII Detection (sa-01, sa-08)
   ↓
3. Task Router (ai-03)
   ↓
4. Agent Selection & Delegation (ai-03)
   ↓
5. Tool Permission Check (sa-02)
   ↓
6. Tool Execution in Sandbox (sa-08)
   ↓
7. Tool Cost Tracking (fo-07)
   ↓
8. Agent Coordination & Handoffs (ai-03)
   ↓
9. Conversation State Persistence (de-01)
   ↓
10. Output Validation (de-03)
    ↓
11. Security Filtering (sa-08)
    ↓
12. Response Caching (ai-01)
    ↓
13. Performance Monitoring (mo-04)
    ↓
14. Cost Attribution (fo-01)
    ↓
15. Behavior Drift Detection (mo-05)
```

##  Quick Wins

1. **Enable prompt caching for agents** - 90% cost reduction on repeated agent calls
2. **Implement tool result caching** - Reduce expensive API call costs
3. **Set up agent-level cost tracking** - Identify and optimize expensive agent patterns
4. **Add tool execution sandboxing** - Prevent security vulnerabilities
5. **Implement agent permission controls** - Follow least privilege principle
6. **Enable distributed tracing** - Full visibility into multi-agent workflows
7. **Set up agent performance monitoring** - Catch quality degradation early
8. **Containerize agents as microservices** - Enable independent scaling and deployment
