# Development Accelerator - Productivity & Speed Agent

Accelerate development through project scaffolding, code generation, test automation, rapid API development, and integration patterns.

## Role Overview

**Agent**: Development Accelerator
**Focus**: Project scaffolding, code generation, testing, API development, integrations
**Skills**: 5 specialized skills (da-01 to da-05)

## When to Use

Invoke this role when you need to:

- Start a new project quickly
- Generate boilerplate code
- Create tests automatically
- Build APIs rapidly
- Integrate with external services
- Reduce repetitive coding tasks

## Skills

| ID    | Skill                  | Description                                     |
| ----- | ---------------------- | ----------------------------------------------- |
| da-01 | Project Scaffolding    | Templates, directory structure, config setup    |
| da-02 | Code Generation        | CRUD, models, types, migrations                 |
| da-03 | Test Automation        | Test generation, fixtures, mocks                |
| da-04 | Rapid API Development  | OpenAPI, REST, GraphQL, documentation           |
| da-05 | Integration Patterns   | Webhooks, events, OAuth, third-party APIs       |

## Enterprise Integration

### Mandatory Connections

- **DevOps (do-01)**: CI/CD for generated projects
- **Security Architect (sa-05)**: Security in generated code
- **Code Hardener**: Production-ready patterns

### Recommended Connections

- **Project Guardian (pg-01)**: Health monitoring setup
- **QA Engineer (qa-01)**: Test strategy alignment
- **Technical Writer (tw-01)**: Documentation generation

## Quick Start

```bash
# Full project scaffold
@dev-accelerator "Create production-ready TypeScript API project"

# Individual skill usage
@dev-accelerator da-01 "Scaffold Next.js project with authentication"
@dev-accelerator da-02 "Generate CRUD for Product, Order, and Customer models"
@dev-accelerator da-03 "Generate unit and integration tests for order service"
@dev-accelerator da-04 "Create OpenAPI spec and REST endpoints for products"
@dev-accelerator da-05 "Add Stripe payment webhook integration"
```

## Skill Details

### da-01: Project Scaffolding

**Purpose**: Quickly bootstrap new projects with best practices

**Capabilities**:

- Multi-language project templates
- Directory structure generation
- Configuration files (ESLint, Prettier, tsconfig)
- Development environment setup
- CI/CD pipeline scaffolding
- Docker and docker-compose
- Documentation templates

**Available Templates**:

| Stack | Technologies | Use Case |
|-------|-------------|----------|
| Node.js REST | Express, TypeScript, PostgreSQL | API backend |
| Node.js GraphQL | Apollo, TypeScript, Prisma | GraphQL API |
| Python FastAPI | FastAPI, SQLAlchemy, Alembic | Python API |
| Next.js Full | Next.js 14, Prisma, NextAuth | Full-stack web |
| React SPA | Vite, TypeScript, React Query | Frontend app |
| CLI Tool | Commander, TypeScript | Command-line tool |
| Library | TypeScript, Rollup, Jest | npm package |

**Generated Structure**:

```
my-project/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Continuous integration
│       ├── cd.yml              # Continuous deployment
│       └── security.yml        # Security scanning
├── src/
│   ├── api/                    # API routes and handlers
│   ├── models/                 # Data models
│   ├── services/               # Business logic
│   ├── utils/                  # Utility functions
│   └── index.ts                # Entry point
├── tests/
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── e2e/                    # End-to-end tests
├── docs/                       # Documentation
├── scripts/                    # Build and deploy scripts
├── .env.example                # Environment variables template
├── .gitignore
├── package.json
├── tsconfig.json
├── Dockerfile
├── docker-compose.yml
└── README.md
```

**Usage**:

```bash
# Create REST API project
@dev-accelerator da-01 "Create Node.js REST API with PostgreSQL and JWT auth"

# Create full-stack project
@dev-accelerator da-01 "Scaffold Next.js app with Prisma, NextAuth, and Tailwind"

# Create microservice
@dev-accelerator da-01 "Create Python FastAPI microservice with Redis caching"
```

---

### da-02: Code Generation

**Purpose**: Generate repetitive code automatically

**Capabilities**:

- CRUD operations for models
- Model/Schema generation from definition
- TypeScript types from JSON Schema/OpenAPI
- Database migrations
- API clients from OpenAPI specs
- Form components from schemas

**CRUD Generation**:

For a model definition, generates:

| File | Content |
|------|---------|
| `models/user.ts` | Interface/type definition |
| `repositories/userRepository.ts` | Data access layer |
| `services/userService.ts` | Business logic |
| `controllers/userController.ts` | HTTP handlers |
| `routes/userRoutes.ts` | Route definitions |
| `dto/userDto.ts` | Request/response DTOs |
| `tests/user.test.ts` | Unit tests |
| `migrations/xxx_create_users.ts` | Database migration |

**Type Generation**:

```bash
# From OpenAPI spec
@dev-accelerator da-02 "Generate TypeScript types from openapi.yaml"

# From JSON Schema
@dev-accelerator da-02 "Generate types from schema.json"

# From database schema
@dev-accelerator da-02 "Generate Prisma models from existing PostgreSQL database"
```

**Usage**:

```bash
# Generate full CRUD
@dev-accelerator da-02 "Generate CRUD for User with email, name, role fields"

# Generate multiple models
@dev-accelerator da-02 "Generate models for e-commerce: Product, Order, Customer, Review"

# Generate API client
@dev-accelerator da-02 "Generate TypeScript API client from petstore OpenAPI spec"
```

---

### da-03: Test Automation

**Purpose**: Automatically generate test cases and infrastructure

**Capabilities**:

- Unit test generation from functions
- Integration test scaffolding
- API endpoint test generation
- Test fixtures and factories
- Mock and stub generation
- E2E test templates
- Coverage optimization suggestions

**Test Generation Matrix**:

| Code Type | Generated Tests |
|-----------|-----------------|
| Function | Unit tests with happy path, edge cases, errors |
| Class | Unit tests for each method |
| API Endpoint | Request/response tests, auth, validation |
| Service | Integration tests with mocked dependencies |
| Component | Render tests, interaction tests |

**Test Patterns**:

```typescript
// Generated unit test
describe('calculateTotal', () => {
  it('should calculate total with valid items', () => {
    const items = [{ price: 10, qty: 2 }, { price: 5, qty: 3 }];
    expect(calculateTotal(items)).toBe(35);
  });

  it('should return 0 for empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('should throw for negative quantities', () => {
    const items = [{ price: 10, qty: -1 }];
    expect(() => calculateTotal(items)).toThrow();
  });
});

// Generated API test
describe('POST /api/orders', () => {
  it('should create order and return 201', async () => {
    const payload = { items: [{ productId: '1', qty: 2 }] };
    const response = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${token}`)
      .send(payload);

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
  });

  it('should return 400 for empty items', async () => {
    const response = await request(app)
      .post('/api/orders')
      .set('Authorization', `Bearer ${token}`)
      .send({ items: [] });

    expect(response.status).toBe(400);
  });

  it('should return 401 without auth', async () => {
    const response = await request(app)
      .post('/api/orders')
      .send({ items: [] });

    expect(response.status).toBe(401);
  });
});
```

**Usage**:

```bash
# Generate tests for a file
@dev-accelerator da-03 "Generate unit tests for src/services/orderService.ts"

# Generate API tests
@dev-accelerator da-03 "Generate API tests for all endpoints in /api/orders"

# Generate test fixtures
@dev-accelerator da-03 "Create test fixtures and factories for User, Order, Product"
```

---

### da-04: Rapid API Development

**Purpose**: Quickly build and document APIs

**Capabilities**:

- OpenAPI/Swagger specification generation
- REST endpoint scaffolding
- GraphQL schema and resolver generation
- Request validation setup
- Response serialization
- API documentation generation
- Postman collection export

**API Generation Workflow**:

```
1. Define resources (e.g., User, Order, Product)
   ↓
2. Generate OpenAPI specification
   ↓
3. Generate route handlers
   ↓
4. Add validation middleware
   ↓
5. Generate documentation
   ↓
6. Export Postman collection
```

**REST Endpoint Template**:

```typescript
// Generated: src/api/orders.ts
import { Router } from 'express';
import { validate } from '../middleware/validate';
import { authenticate } from '../middleware/auth';
import { OrderService } from '../services/orderService';
import { createOrderSchema, updateOrderSchema } from '../dto/orderDto';

const router = Router();
const orderService = new OrderService();

// List orders
router.get('/', authenticate, async (req, res) => {
  const orders = await orderService.findAll(req.user.id);
  res.json(orders);
});

// Get order by ID
router.get('/:id', authenticate, async (req, res) => {
  const order = await orderService.findById(req.params.id);
  if (!order) return res.status(404).json({ error: 'Not found' });
  res.json(order);
});

// Create order
router.post('/',
  authenticate,
  validate(createOrderSchema),
  async (req, res) => {
    const order = await orderService.create(req.user.id, req.body);
    res.status(201).json(order);
  }
);

// Update order
router.put('/:id',
  authenticate,
  validate(updateOrderSchema),
  async (req, res) => {
    const order = await orderService.update(req.params.id, req.body);
    res.json(order);
  }
);

// Delete order
router.delete('/:id', authenticate, async (req, res) => {
  await orderService.delete(req.params.id);
  res.status(204).send();
});

export default router;
```

**Usage**:

```bash
# Generate REST API
@dev-accelerator da-04 "Create REST API for products with CRUD operations"

# Generate GraphQL API
@dev-accelerator da-04 "Create GraphQL schema and resolvers for user management"

# Generate OpenAPI spec
@dev-accelerator da-04 "Generate OpenAPI 3.0 specification for existing endpoints"
```

---

### da-05: Integration Patterns

**Purpose**: Implement common integration patterns quickly

**Capabilities**:

- Webhook sending and receiving
- Event-driven architecture patterns
- Message queue integration (SQS, RabbitMQ, Redis)
- Third-party API clients
- OAuth/SSO implementation
- Database connection patterns

**Integration Templates**:

| Pattern | Use Case | Components |
|---------|----------|------------|
| Webhook Receiver | Payment notifications | Signature verification, event routing |
| Webhook Sender | Status updates | Retry logic, delivery tracking |
| Event Bus | Microservices | Pub/sub, guaranteed delivery |
| OAuth Flow | SSO login | Token exchange, refresh |
| API Client | Third-party integration | Rate limiting, error handling |

**Webhook Implementation**:

```typescript
// Webhook receiver with signature verification
app.post('/webhooks/stripe',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    const sig = req.headers['stripe-signature'];

    try {
      const event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        process.env.STRIPE_WEBHOOK_SECRET
      );

      switch (event.type) {
        case 'payment_intent.succeeded':
          await handlePaymentSuccess(event.data.object);
          break;
        case 'payment_intent.failed':
          await handlePaymentFailure(event.data.object);
          break;
      }

      res.json({ received: true });
    } catch (err) {
      console.error('Webhook error:', err.message);
      res.status(400).send(`Webhook Error: ${err.message}`);
    }
  }
);
```

**Event-Driven Pattern**:

```typescript
// Event bus with guaranteed delivery
const eventBus = new EventBus({
  persistence: new PostgresEventStore(),
  retryPolicy: { maxRetries: 3, backoff: 'exponential' },
});

// Subscribe to events
eventBus.subscribe('order.created', async (event) => {
  await inventoryService.reserveItems(event.data.items);
});

eventBus.subscribe('order.created', async (event) => {
  await notificationService.sendOrderConfirmation(event.data);
});

// Publish events
await eventBus.publish('order.created', { orderId, items, userId });
```

**Usage**:

```bash
# Add webhook integration
@dev-accelerator da-05 "Add Stripe webhook handler for payment events"

# Add OAuth integration
@dev-accelerator da-05 "Implement Google OAuth login flow"

# Add event-driven pattern
@dev-accelerator da-05 "Set up event bus for order processing workflow"

# Add third-party API client
@dev-accelerator da-05 "Create Twilio SMS client with rate limiting"
```

---

## Enterprise Workflow

### New Feature Development

```
1. Scaffold feature structure (da-01)
   ↓
2. Generate models and CRUD (da-02)
   ↓
3. Create API endpoints (da-04)
   ↓
4. Generate tests (da-03)
   ↓
5. Add integrations (da-05)
   ↓
6. Review and harden (@code-hardener)
```

---

## Integration with Other Skills

| Skill                | Integration                           |
| -------------------- | ------------------------------------- |
| @project-guardian    | Health check for generated projects   |
| @devops do-01        | CI/CD for scaffolded projects         |
| @security-architect  | Security in generated code            |
| @code-hardener       | Hardening generated code              |
| @qa-engineer         | Test strategy alignment               |

---

## Best Practices

1. **Template Consistency**: Use scaffolding for all projects in an org
2. **Generate Early**: Generate boilerplate at project start
3. **Test Alongside**: Generate tests with every code generation
4. **Document APIs**: Always generate OpenAPI specs
5. **Standardize Integrations**: Use common patterns for all integrations
6. **Review Generated Code**: Always review and customize generated code

---

## Quick Reference

```bash
# Full project setup
@dev-accelerator "Create production-ready e-commerce API with products, orders, payments"

# Individual tasks
@dev-accelerator da-01 "Scaffold TypeScript monorepo with packages for api, web, shared"
@dev-accelerator da-02 "Generate models from this Prisma schema"
@dev-accelerator da-03 "Create comprehensive test suite for user authentication"
@dev-accelerator da-04 "Build REST API with OpenAPI docs for inventory management"
@dev-accelerator da-05 "Integrate with Shopify webhooks for order sync"
```
