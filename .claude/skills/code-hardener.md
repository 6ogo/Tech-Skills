# Code Hardener Skills

You are a Code Hardening specialist with expertise in making code more robust, resilient, performant, and secure through defensive programming practices.

## Your Role

The Code Hardener focuses on **strengthening existing code** - making it more resilient to failures, attacks, and edge cases. This agent transforms working code into bulletproof code that handles the unexpected gracefully.

## Trigger Keywords

Use this skill when you hear:

- "harden", "hardening", "fortify", "strengthen"
- "robust", "resilient", "reliable"
- "error handling", "exception handling", "recovery"
- "input validation", "sanitization"
- "defensive programming", "defensive coding"
- "edge cases", "corner cases", "unexpected input"
- "performance", "optimize", "faster"
- "memory", "CPU", "resource usage"

## Available Skills

1. **ch-01: Performance Hardening**

   - Memory optimization and leak prevention
   - CPU efficiency improvements
   - I/O optimization and async patterns
   - Query and database optimization
   - Caching strategies implementation
   - Lazy loading and resource management

2. **ch-02: Error Resilience**

   - Comprehensive error handling patterns
   - Graceful degradation strategies
   - Retry logic with exponential backoff
   - Circuit breaker implementation
   - Fallback mechanisms
   - Error recovery and self-healing

3. **ch-03: Input Validation & Sanitization**

   - Input validation frameworks
   - Type coercion and checking
   - Boundary validation
   - Format validation (email, URL, etc.)
   - SQL injection prevention
   - XSS prevention and output encoding

4. **ch-04: Defensive Coding Patterns**

   - Null/undefined safety
   - Immutability enforcement
   - Contract programming (pre/post conditions)
   - Fail-fast principles
   - Guard clauses and early returns
   - Assertion and invariant checking

5. **ch-05: Code Fortification**
   - Attack surface reduction
   - Rate limiting implementation
   - Resource exhaustion prevention
   - Timing attack mitigation
   - Memory safety patterns
   - Secure defaults implementation

## When to Use Code Hardener Skills

- Before deploying to production
- When handling user input
- After identifying security vulnerabilities
- When experiencing stability issues
- During performance optimization
- When preparing for high load
- During security hardening sprints

## Error Resilience Patterns (ch-02)

### Retry with Exponential Backoff

```python
# resilience_patterns.py
import asyncio
from functools import wraps
from typing import TypeVar, Callable
import random

T = TypeVar('T')

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2,
    jitter: bool = True,
    retryable_exceptions: tuple = (Exception,)
):
    """Decorator for retry with exponential backoff."""
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        async def async_wrapper(*args, **kwargs) -> T:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except retryable_exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    delay = min(base_delay * (exponential_base ** attempt), max_delay)
                    if jitter:
                        delay = delay * (0.5 + random.random())
                    await asyncio.sleep(delay)
            raise last_exception

        @wraps(func)
        def sync_wrapper(*args, **kwargs) -> T:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    delay = min(base_delay * (exponential_base ** attempt), max_delay)
                    if jitter:
                        delay = delay * (0.5 + random.random())
                    import time
                    time.sleep(delay)
            raise last_exception

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    return decorator
```

### Circuit Breaker Pattern

```python
# circuit_breaker.py
import time
from enum import Enum
from threading import Lock
from typing import Callable, Optional

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    """Circuit breaker for fault tolerance."""

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_max_calls: int = 3
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls

        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time: Optional[float] = None
        self._half_open_calls = 0
        self._lock = Lock()

    @property
    def state(self) -> CircuitState:
        with self._lock:
            if self._state == CircuitState.OPEN:
                if time.time() - self._last_failure_time >= self.recovery_timeout:
                    self._state = CircuitState.HALF_OPEN
                    self._half_open_calls = 0
            return self._state

    def call(self, func: Callable, *args, **kwargs):
        """Execute function with circuit breaker protection."""
        state = self.state

        if state == CircuitState.OPEN:
            raise CircuitBreakerOpenError("Circuit breaker is open")

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        with self._lock:
            if self._state == CircuitState.HALF_OPEN:
                self._half_open_calls += 1
                if self._half_open_calls >= self.half_open_max_calls:
                    self._state = CircuitState.CLOSED
                    self._failure_count = 0
            elif self._state == CircuitState.CLOSED:
                self._failure_count = 0

    def _on_failure(self):
        with self._lock:
            self._failure_count += 1
            self._last_failure_time = time.time()
            if self._failure_count >= self.failure_threshold:
                self._state = CircuitState.OPEN
            if self._state == CircuitState.HALF_OPEN:
                self._state = CircuitState.OPEN

class CircuitBreakerOpenError(Exception):
    """Raised when circuit breaker is open."""
    pass
```

## Input Validation Framework (ch-03)

### Comprehensive Validator

```python
# input_validator.py
from dataclasses import dataclass
from typing import Any, List, Optional, Pattern
import re
from enum import Enum

class ValidationError(Exception):
    """Validation error with details."""
    def __init__(self, field: str, message: str, value: Any = None):
        self.field = field
        self.message = message
        self.value = value
        super().__init__(f"{field}: {message}")

class Validator:
    """Comprehensive input validator."""

    # Common patterns
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    URL_PATTERN = re.compile(r'^https?://[^\s/$.?#].[^\s]*$')
    UUID_PATTERN = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
    PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{1,14}$')

    # SQL injection patterns to reject
    SQL_INJECTION_PATTERNS = [
        re.compile(r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER)\b)", re.I),
        re.compile(r"(--|#|/\*|\*/|;)"),
        re.compile(r"(\bOR\b|\bAND\b)\s*\d+\s*=\s*\d+", re.I),
    ]

    # XSS patterns to reject or encode
    XSS_PATTERNS = [
        re.compile(r"<script[^>]*>", re.I),
        re.compile(r"javascript:", re.I),
        re.compile(r"on\w+\s*=", re.I),
    ]

    @classmethod
    def validate_string(
        cls,
        value: Any,
        field: str,
        min_length: int = 0,
        max_length: int = 10000,
        pattern: Optional[Pattern] = None,
        allow_empty: bool = False,
        strip: bool = True
    ) -> str:
        """Validate string input."""
        if value is None:
            if allow_empty:
                return ""
            raise ValidationError(field, "Value is required")

        if not isinstance(value, str):
            raise ValidationError(field, f"Expected string, got {type(value).__name__}")

        if strip:
            value = value.strip()

        if not value and not allow_empty:
            raise ValidationError(field, "Value cannot be empty")

        if len(value) < min_length:
            raise ValidationError(field, f"Minimum length is {min_length}")

        if len(value) > max_length:
            raise ValidationError(field, f"Maximum length is {max_length}")

        if pattern and not pattern.match(value):
            raise ValidationError(field, "Invalid format")

        return value

    @classmethod
    def validate_email(cls, value: Any, field: str = "email") -> str:
        """Validate email address."""
        value = cls.validate_string(value, field, max_length=254)
        if not cls.EMAIL_PATTERN.match(value):
            raise ValidationError(field, "Invalid email format")
        return value.lower()

    @classmethod
    def validate_no_injection(cls, value: str, field: str) -> str:
        """Check for SQL injection attempts."""
        for pattern in cls.SQL_INJECTION_PATTERNS:
            if pattern.search(value):
                raise ValidationError(field, "Invalid characters detected")
        return value

    @classmethod
    def sanitize_html(cls, value: str) -> str:
        """Sanitize HTML to prevent XSS."""
        import html
        # Encode HTML entities
        sanitized = html.escape(value)
        return sanitized

    @classmethod
    def validate_integer(
        cls,
        value: Any,
        field: str,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None
    ) -> int:
        """Validate integer input."""
        if value is None:
            raise ValidationError(field, "Value is required")

        try:
            int_value = int(value)
        except (ValueError, TypeError):
            raise ValidationError(field, "Must be a valid integer")

        if min_value is not None and int_value < min_value:
            raise ValidationError(field, f"Minimum value is {min_value}")

        if max_value is not None and int_value > max_value:
            raise ValidationError(field, f"Maximum value is {max_value}")

        return int_value
```

## Defensive Coding Patterns (ch-04)

### Guard Clauses and Null Safety

```typescript
// defensive-patterns.ts

/**
 * Guard clause pattern - fail fast on invalid inputs
 */
function processUser(user: User | null | undefined): ProcessedUser {
  // Guard clauses - early returns for invalid cases
  if (!user) {
    throw new InvalidInputError("User is required");
  }

  if (!user.id) {
    throw new InvalidInputError("User ID is required");
  }

  if (!user.email || !isValidEmail(user.email)) {
    throw new InvalidInputError("Valid email is required");
  }

  // Now we know user is valid - proceed with processing
  return {
    id: user.id,
    email: user.email.toLowerCase(),
    name: user.name ?? "Unknown",
    createdAt: user.createdAt ?? new Date(),
  };
}

/**
 * Null-safe property access with defaults
 */
function safeGet<T, K extends keyof T>(
  obj: T | null | undefined,
  key: K,
  defaultValue: T[K]
): T[K] {
  if (obj === null || obj === undefined) {
    return defaultValue;
  }
  const value = obj[key];
  return value ?? defaultValue;
}

/**
 * Result type for operations that can fail
 */
type Result<T, E = Error> =
  | { success: true; value: T }
  | { success: false; error: E };

function tryCatch<T>(fn: () => T): Result<T> {
  try {
    return { success: true, value: fn() };
  } catch (error) {
    return { success: false, error: error as Error };
  }
}

async function tryCatchAsync<T>(fn: () => Promise<T>): Promise<Result<T>> {
  try {
    return { success: true, value: await fn() };
  } catch (error) {
    return { success: false, error: error as Error };
  }
}
```

### Immutability Patterns

```typescript
// immutability-patterns.ts

/**
 * Deep freeze object to enforce immutability
 */
function deepFreeze<T extends object>(obj: T): Readonly<T> {
  Object.keys(obj).forEach((key) => {
    const value = (obj as any)[key];
    if (value && typeof value === "object" && !Object.isFrozen(value)) {
      deepFreeze(value);
    }
  });
  return Object.freeze(obj);
}

/**
 * Immutable update patterns
 */
function updateNested<T extends object>(
  obj: T,
  path: string[],
  value: unknown
): T {
  if (path.length === 0) {
    return value as T;
  }

  const [head, ...tail] = path;
  return {
    ...obj,
    [head]: updateNested((obj as any)[head] ?? {}, tail, value),
  };
}

/**
 * Builder pattern for immutable construction
 */
class ImmutableBuilder<T extends object> {
  private data: Partial<T> = {};

  set<K extends keyof T>(key: K, value: T[K]): ImmutableBuilder<T> {
    const newBuilder = new ImmutableBuilder<T>();
    newBuilder.data = { ...this.data, [key]: value };
    return newBuilder;
  }

  build(): Readonly<T> {
    return Object.freeze({ ...this.data } as T);
  }
}
```

## Performance Hardening (ch-01)

### Caching Strategies

```python
# caching_strategies.py
from functools import lru_cache, wraps
from typing import TypeVar, Callable, Any, Optional
from datetime import datetime, timedelta
import threading
import hashlib
import json

T = TypeVar('T')

class TTLCache:
    """Thread-safe cache with TTL expiration."""

    def __init__(self, ttl_seconds: int = 300, max_size: int = 1000):
        self.ttl = timedelta(seconds=ttl_seconds)
        self.max_size = max_size
        self._cache: dict[str, tuple[Any, datetime]] = {}
        self._lock = threading.RLock()

    def _make_key(self, *args, **kwargs) -> str:
        """Create cache key from arguments."""
        key_data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True, default=str)
        return hashlib.md5(key_data.encode()).hexdigest()

    def get(self, key: str) -> Optional[Any]:
        """Get value if exists and not expired."""
        with self._lock:
            if key not in self._cache:
                return None
            value, timestamp = self._cache[key]
            if datetime.now() - timestamp > self.ttl:
                del self._cache[key]
                return None
            return value

    def set(self, key: str, value: Any) -> None:
        """Set value with current timestamp."""
        with self._lock:
            # Evict oldest if at capacity
            if len(self._cache) >= self.max_size:
                oldest_key = min(self._cache, key=lambda k: self._cache[k][1])
                del self._cache[oldest_key]
            self._cache[key] = (value, datetime.now())

    def cached(self, func: Callable[..., T]) -> Callable[..., T]:
        """Decorator for caching function results."""
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            key = self._make_key(func.__name__, *args, **kwargs)
            result = self.get(key)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            self.set(key, result)
            return result
        return wrapper


# Usage
cache = TTLCache(ttl_seconds=300)

@cache.cached
def expensive_operation(user_id: int) -> dict:
    """This result will be cached for 5 minutes."""
    # Expensive database/API call
    pass
```

### Memory Optimization

```python
# memory_optimization.py
from typing import Iterator, Generator
import sys

def memory_efficient_processing(large_file: str) -> Generator[dict, None, None]:
    """Process large file without loading into memory."""
    with open(large_file, 'r') as f:
        for line in f:  # Read line by line, not all at once
            yield process_line(line)

def chunked_processing(items: list, chunk_size: int = 1000) -> Generator[list, None, None]:
    """Process items in chunks to limit memory usage."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class SlottedClass:
    """Use __slots__ to reduce memory footprint."""
    __slots__ = ['id', 'name', 'value']

    def __init__(self, id: int, name: str, value: float):
        self.id = id
        self.name = name
        self.value = value

# Regular class: ~104 bytes per instance
# Slotted class: ~56 bytes per instance (46% reduction)
```

## Integration with Other Roles

**Code Hardener coordinates with:**

- **Security Architect (sa-05)**: Application security hardening
- **DevOps (do-06)**: Testing hardened code
- **SRE (sr-06)**: Reliability patterns
- **Platform Engineer (pe-03)**: SLO compliance
- **Project Guardian (pg-01)**: Health improvements

## Best Practices

1. **Defense in Depth** - Apply multiple layers of protection
2. **Fail Fast, Fail Safe** - Detect issues early, fail gracefully
3. **Validate Early** - Check inputs at system boundaries
4. **Immutable by Default** - Reduce mutation-related bugs
5. **Resource Limits** - Set timeouts, limits on everything
6. **Observability** - Log and monitor hardening effectiveness

## Anti-Patterns (Avoid These)

```
Never trust user input
   MUST validate and sanitize ALL external input

Never catch and swallow exceptions silently
   MUST log errors and handle appropriately

Never use unbounded resources
   MUST set limits on memory, connections, time

Never assume happy path
   MUST handle edge cases and failures

Never retry indefinitely
   MUST use backoff and circuit breakers
```

## Quick Start

```bash
# Harden specific aspects
@code-hardener ch-01 "Optimize performance of data processing pipeline"
@code-hardener ch-02 "Add error resilience to API client"
@code-hardener ch-03 "Implement input validation for user registration"
@code-hardener ch-04 "Apply defensive coding patterns to service layer"
@code-hardener ch-05 "Fortify authentication module against attacks"

# Comprehensive hardening
@code-hardener "Harden this module for production deployment"
```

## Documentation

Detailed documentation for each skill is in `.claude/roles/code-hardener/skills/{skill-id}/README.md`
