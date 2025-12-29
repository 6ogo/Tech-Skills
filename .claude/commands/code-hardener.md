# Code Hardener - Strengthening & Fortification Agent

Transform working code into bulletproof code through performance optimization, error resilience, input validation, defensive patterns, and security fortification.

## Role Overview

**Agent**: Code Hardener
**Focus**: Code strengthening, performance optimization, error resilience, defensive programming
**Skills**: 5 specialized skills (ch-01 to ch-05)

## When to Use

Invoke this role when you need to:

- Optimize code performance (memory, CPU, I/O)
- Add robust error handling and recovery
- Implement input validation and sanitization
- Apply defensive programming patterns
- Fortify code against attacks and edge cases
- Prepare code for production deployment

## Skills

| ID    | Skill                        | Description                                     |
| ----- | ---------------------------- | ----------------------------------------------- |
| ch-01 | Performance Hardening        | Memory, CPU, I/O optimization, caching          |
| ch-02 | Error Resilience             | Error handling, retries, circuit breakers       |
| ch-03 | Input Validation             | Validation frameworks, sanitization, injection prevention |
| ch-04 | Defensive Coding Patterns    | Null safety, immutability, guard clauses        |
| ch-05 | Code Fortification           | Attack surface reduction, rate limiting, secure defaults |

## Enterprise Integration

### Mandatory Connections

- **Security Architect (sa-05)**: Application security hardening
- **DevOps (do-06)**: Testing hardened code
- **Project Guardian (pg-01)**: Health score improvement

### Recommended Connections

- **SRE (sr-06)**: Reliability patterns
- **Platform Engineer (pe-03)**: SLO compliance
- **Code Review (cr-03)**: Quality gate validation

## Quick Start

```bash
# Comprehensive code hardening
@code-hardener "Harden this module for production deployment"

# Individual skill usage
@code-hardener ch-01 "Optimize memory usage and add caching"
@code-hardener ch-02 "Add retry logic with circuit breaker"
@code-hardener ch-03 "Implement comprehensive input validation"
@code-hardener ch-04 "Apply defensive coding patterns"
@code-hardener ch-05 "Fortify against common attack vectors"
```

## Skill Details

### ch-01: Performance Hardening

**Purpose**: Optimize code for speed, memory efficiency, and resource usage

**Capabilities**:

- Memory leak detection and prevention
- CPU-efficient algorithms and data structures
- I/O optimization (async, batching, streaming)
- Database query optimization
- Caching implementation (in-memory, distributed)
- Lazy loading and resource management
- Connection pooling optimization

**Performance Patterns**:

| Pattern | Use Case | Impact |
|---------|----------|--------|
| Object Pooling | Frequent allocation/deallocation | -60% memory churn |
| Lazy Loading | Expensive resources | -40% startup time |
| Batch Processing | Multiple DB operations | -70% DB round trips |
| Connection Pooling | Database connections | -80% connection overhead |
| Memoization | Repeated calculations | -90% for same inputs |
| Streaming | Large data processing | -90% memory usage |

**Before/After Example**:

```python
# BEFORE: Memory-intensive
def process_all_users():
    users = db.get_all_users()  # Loads millions into memory
    results = []
    for user in users:
        results.append(process_user(user))
    return results

# AFTER: Memory-efficient streaming
def process_all_users():
    for user_batch in db.get_users_batched(batch_size=1000):
        for user in user_batch:
            yield process_user(user)  # Generator, not list
```

---

### ch-02: Error Resilience

**Purpose**: Make code gracefully handle failures and recover automatically

**Capabilities**:

- Comprehensive error handling patterns
- Retry with exponential backoff and jitter
- Circuit breaker implementation
- Fallback mechanisms and degraded modes
- Graceful degradation strategies
- Self-healing and auto-recovery
- Bulkhead isolation

**Resilience Patterns**:

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| Retry | Transient failures | Network, API calls |
| Circuit Breaker | Prevent cascade failures | External dependencies |
| Fallback | Continue with alternative | Non-critical features |
| Bulkhead | Isolate failures | Multi-tenant, microservices |
| Timeout | Prevent hanging | All external calls |
| Graceful Degradation | Partial functionality | Feature flags |

**Implementation Example**:

```typescript
// Resilient API client with all patterns
class ResilientClient {
  private circuitBreaker = new CircuitBreaker({
    failureThreshold: 5,
    resetTimeout: 30000
  });

  async fetchWithResilience<T>(url: string): Promise<T> {
    // Circuit breaker check
    if (this.circuitBreaker.isOpen) {
      return this.fallback<T>(url);
    }

    // Retry with backoff
    return retry(
      async () => {
        // Timeout wrapper
        const response = await withTimeout(
          fetch(url),
          5000 // 5 second timeout
        );

        if (!response.ok) {
          throw new ApiError(response.status);
        }

        this.circuitBreaker.recordSuccess();
        return response.json();
      },
      {
        maxRetries: 3,
        backoff: 'exponential',
        retryableErrors: [NetworkError, TimeoutError]
      }
    ).catch(error => {
      this.circuitBreaker.recordFailure();
      return this.fallback<T>(url);
    });
  }

  private fallback<T>(url: string): T {
    // Return cached data or default
    return this.cache.get(url) ?? this.defaults.get(url);
  }
}
```

---

### ch-03: Input Validation & Sanitization

**Purpose**: Prevent invalid and malicious input from entering the system

**Capabilities**:

- Schema-based validation (JSON Schema, Zod, Pydantic)
- Type coercion and strict type checking
- Boundary and range validation
- Format validation (email, URL, phone, etc.)
- SQL injection prevention
- XSS prevention and output encoding
- Command injection prevention
- Path traversal prevention

**Validation Checklist**:

```markdown
## Input Validation Checklist

### All Inputs
- [ ] Type validation (string, number, boolean, etc.)
- [ ] Required vs optional handling
- [ ] Length/size limits
- [ ] Character whitelist (when possible)

### Strings
- [ ] Max length enforced
- [ ] Trimmed and normalized
- [ ] HTML entities encoded for output
- [ ] SQL special characters parameterized

### Numbers
- [ ] Min/max bounds
- [ ] Integer vs float handling
- [ ] NaN and Infinity rejected
- [ ] Precision limits

### Files
- [ ] File type validation (magic bytes, not just extension)
- [ ] Size limits
- [ ] Filename sanitization
- [ ] Content scanning for malware

### URLs/Paths
- [ ] Protocol whitelist (https only)
- [ ] Domain validation
- [ ] Path traversal prevention (../)
- [ ] SSRF prevention (no internal IPs)
```

**Validation Schema Example**:

```typescript
// Using Zod for comprehensive validation
import { z } from 'zod';

const UserInputSchema = z.object({
  email: z.string()
    .email('Invalid email format')
    .max(254, 'Email too long')
    .transform(e => e.toLowerCase().trim()),

  password: z.string()
    .min(12, 'Password must be at least 12 characters')
    .max(128, 'Password too long')
    .regex(/[A-Z]/, 'Must contain uppercase')
    .regex(/[a-z]/, 'Must contain lowercase')
    .regex(/[0-9]/, 'Must contain number')
    .regex(/[^A-Za-z0-9]/, 'Must contain special character'),

  username: z.string()
    .min(3).max(30)
    .regex(/^[a-zA-Z0-9_-]+$/, 'Invalid characters')
    .transform(u => u.toLowerCase()),

  age: z.number()
    .int('Must be whole number')
    .min(13, 'Must be at least 13')
    .max(120, 'Invalid age'),

  website: z.string()
    .url('Invalid URL')
    .refine(
      url => url.startsWith('https://'),
      'Must use HTTPS'
    )
    .optional(),
});

type UserInput = z.infer<typeof UserInputSchema>;
```

---

### ch-04: Defensive Coding Patterns

**Purpose**: Write code that handles unexpected situations gracefully

**Capabilities**:

- Null/undefined safety patterns
- Guard clauses for early returns
- Immutability enforcement
- Contract programming (preconditions, postconditions)
- Assertion and invariant checking
- Fail-fast principles
- Error boundaries and isolation

**Key Patterns**:

| Pattern | Purpose | Example |
|---------|---------|---------|
| Guard Clause | Fail fast on invalid input | `if (!user) throw new Error()` |
| Null Coalescing | Safe default values | `user.name ?? 'Unknown'` |
| Optional Chaining | Safe property access | `user?.address?.city` |
| Result Type | Explicit error handling | `Result<User, Error>` |
| Assertion | Verify assumptions | `assert(items.length > 0)` |
| Immutable Update | Prevent side effects | `{...state, count: state.count + 1}` |

**Defensive Coding Checklist**:

```markdown
## Defensive Coding Checklist

### Function Design
- [ ] All parameters validated at entry
- [ ] Clear return type (including error cases)
- [ ] No side effects unless documented
- [ ] Idempotent where possible

### Null/Undefined Safety
- [ ] Explicit null checks where needed
- [ ] Default values for optional parameters
- [ ] Optional chaining for deep access
- [ ] No implicit null returns

### Error Handling
- [ ] Specific exception types
- [ ] Errors include context
- [ ] No swallowed exceptions
- [ ] Error boundaries defined

### State Management
- [ ] Prefer immutable data
- [ ] State changes are atomic
- [ ] Concurrent access handled
- [ ] Invariants maintained
```

---

### ch-05: Code Fortification

**Purpose**: Reduce attack surface and harden against security threats

**Capabilities**:

- Attack surface analysis and reduction
- Rate limiting implementation
- Resource exhaustion prevention
- Timing attack mitigation
- Memory safety patterns
- Secure defaults configuration
- Privilege escalation prevention

**Fortification Areas**:

| Area | Threats | Mitigations |
|------|---------|-------------|
| Authentication | Brute force, credential stuffing | Rate limiting, account lockout |
| Authorization | Privilege escalation | Least privilege, RBAC |
| Data | Injection, exposure | Parameterization, encryption |
| Resources | DoS, exhaustion | Limits, quotas, timeouts |
| Dependencies | Supply chain | Pinning, scanning, SBOMs |
| Configuration | Misconfig | Secure defaults, hardening |

**Rate Limiting Implementation**:

```typescript
// rate-limiter.ts
class RateLimiter {
  private requests: Map<string, number[]> = new Map();

  constructor(
    private maxRequests: number,
    private windowMs: number
  ) {}

  isAllowed(identifier: string): boolean {
    const now = Date.now();
    const windowStart = now - this.windowMs;

    // Get existing requests for this identifier
    let timestamps = this.requests.get(identifier) ?? [];

    // Filter to only requests within window
    timestamps = timestamps.filter(t => t > windowStart);

    // Check if under limit
    if (timestamps.length >= this.maxRequests) {
      return false;
    }

    // Add current request
    timestamps.push(now);
    this.requests.set(identifier, timestamps);

    return true;
  }

  getRemainingRequests(identifier: string): number {
    const timestamps = this.requests.get(identifier) ?? [];
    const windowStart = Date.now() - this.windowMs;
    const recentCount = timestamps.filter(t => t > windowStart).length;
    return Math.max(0, this.maxRequests - recentCount);
  }
}

// Usage: 100 requests per minute per IP
const limiter = new RateLimiter(100, 60000);

app.use((req, res, next) => {
  const ip = req.ip;
  if (!limiter.isAllowed(ip)) {
    return res.status(429).json({
      error: 'Too many requests',
      retryAfter: 60
    });
  }
  res.setHeader('X-RateLimit-Remaining', limiter.getRemainingRequests(ip));
  next();
});
```

---

## Enterprise Workflow

### Pre-Production Hardening Checklist

```markdown
## Production Hardening Checklist

### Performance (ch-01)
- [ ] Memory profiling completed
- [ ] No memory leaks detected
- [ ] Caching implemented for expensive operations
- [ ] Database queries optimized
- [ ] Connection pooling configured

### Resilience (ch-02)
- [ ] Retry logic with backoff on external calls
- [ ] Circuit breakers on dependencies
- [ ] Timeouts on all network operations
- [ ] Graceful degradation for non-critical features
- [ ] Health checks implemented

### Input Validation (ch-03)
- [ ] All user inputs validated
- [ ] All outputs encoded
- [ ] SQL parameterized queries only
- [ ] File uploads validated
- [ ] API inputs schema-validated

### Defensive Coding (ch-04)
- [ ] Null checks on all external data
- [ ] Error boundaries around components
- [ ] Assertions on critical invariants
- [ ] Immutable data where possible

### Fortification (ch-05)
- [ ] Rate limiting on public endpoints
- [ ] Resource limits configured
- [ ] Secure defaults verified
- [ ] Attack surface minimized
- [ ] Security headers configured
```

---

## Integration with Other Skills

| Skill                | Integration                           |
| -------------------- | ------------------------------------- |
| @security-architect  | sa-05 Application security details    |
| @devops do-06        | Automated testing of hardened code    |
| @project-guardian    | Health score improvements             |
| @sre sr-06           | Reliability pattern guidance          |
| @maintenance-engineer| Ongoing hardening maintenance         |

---

## Best Practices

1. **Defense in Depth**: Apply multiple layers of protection
2. **Fail Fast, Fail Safe**: Detect early, fail gracefully
3. **Trust Nothing**: Validate all external input
4. **Limit Everything**: Set bounds on resources, time, retries
5. **Observe Everything**: Log and monitor hardening effectiveness
6. **Test Failures**: Chaos engineering for resilience verification

---

## Quick Reference

```bash
# Full hardening assessment
@code-hardener "Assess and harden this service for production"

# Specific hardening
@code-hardener ch-01 "Optimize memory and add caching"
@code-hardener ch-02 "Add circuit breaker to payment service"
@code-hardener ch-03 "Validate all API inputs"
@code-hardener ch-04 "Add null safety to data layer"
@code-hardener ch-05 "Add rate limiting and resource limits"
```
