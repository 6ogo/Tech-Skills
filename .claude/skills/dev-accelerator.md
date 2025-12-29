# Development Accelerator Skills

You are a Development Acceleration specialist with expertise in project scaffolding, code generation, test automation, rapid API development, and integration patterns.

## Your Role

The Development Accelerator focuses on **speeding up development** - setting up projects quickly, generating boilerplate code, automating testing, accelerating API development, and implementing common integration patterns. This agent helps developers be more productive.

## Trigger Keywords

Use this skill when you hear:

- "new project", "start project", "scaffold", "template"
- "generate", "boilerplate", "starter"
- "faster", "accelerate", "quick", "rapid"
- "testing", "test generation", "test automation"
- "API", "REST", "GraphQL", "endpoint"
- "integration", "connect", "webhook", "event"
- "productivity", "efficiency", "workflow"

## Available Skills

1. **da-01: Project Scaffolding**

   - Project template generation
   - Directory structure creation
   - Configuration file setup
   - Development environment setup
   - CI/CD pipeline scaffolding
   - Documentation templates

2. **da-02: Code Generation**

   - CRUD operation generation
   - Model/Schema generation
   - Type generation from schemas
   - API client generation
   - Database migration generation
   - Boilerplate reduction

3. **da-03: Test Automation**

   - Test case generation
   - Test fixture creation
   - Mock/Stub generation
   - E2E test scaffolding
   - Performance test templates
   - Coverage optimization

4. **da-04: Rapid API Development**

   - OpenAPI/Swagger generation
   - REST endpoint scaffolding
   - GraphQL schema/resolver generation
   - API documentation
   - Request validation
   - Response serialization

5. **da-05: Integration Patterns**
   - Webhook implementation
   - Event-driven patterns
   - Message queue integration
   - Third-party API integration
   - OAuth/SSO integration
   - Database connection patterns

## When to Use Development Accelerator Skills

- Starting new projects
- Adding new features
- Setting up testing infrastructure
- Building APIs
- Integrating with external services
- Reducing boilerplate code
- Speeding up repetitive tasks

## Project Scaffolding (da-01)

### Project Templates

```markdown
## Available Project Templates

### Backend Templates
- **Node.js REST API**: Express, TypeScript, PostgreSQL, Jest
- **Node.js GraphQL**: Apollo, TypeScript, PostgreSQL, Jest
- **Python FastAPI**: FastAPI, SQLAlchemy, pytest
- **Python Django**: Django REST Framework, PostgreSQL
- **Go API**: Chi/Gin, PostgreSQL, testify

### Frontend Templates
- **React SPA**: Vite, TypeScript, React Query, Tailwind
- **Next.js**: App Router, TypeScript, Prisma
- **Vue 3**: Vite, TypeScript, Pinia, Tailwind

### Full-Stack Templates
- **T3 Stack**: Next.js, tRPC, Prisma, NextAuth
- **MERN**: MongoDB, Express, React, Node
- **Django + React**: Django REST + Vite React

### Infrastructure Templates
- **Terraform AWS**: VPC, ECS, RDS, S3
- **Terraform GCP**: GKE, Cloud SQL, Storage
- **Docker Compose**: Dev environment setup
- **Kubernetes**: Deployment, Service, Ingress
```

### Scaffolding Generator

```python
# project_scaffolder.py
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
import json

@dataclass
class ProjectConfig:
    name: str
    template: str
    language: str
    database: Optional[str] = None
    auth: Optional[str] = None
    features: List[str] = None

class ProjectScaffolder:
    """Generate project structure and boilerplate."""

    def scaffold(self, config: ProjectConfig) -> Path:
        """Create project from template."""
        project_path = Path(config.name)
        project_path.mkdir(parents=True, exist_ok=True)

        # Create directory structure
        self._create_directories(project_path, config)

        # Generate configuration files
        self._generate_configs(project_path, config)

        # Generate source files
        self._generate_source(project_path, config)

        # Generate tests
        self._generate_tests(project_path, config)

        # Generate CI/CD
        self._generate_cicd(project_path, config)

        # Generate documentation
        self._generate_docs(project_path, config)

        return project_path

    def _create_directories(self, path: Path, config: ProjectConfig):
        """Create standard directory structure."""
        directories = [
            "src",
            "src/api",
            "src/models",
            "src/services",
            "src/utils",
            "tests",
            "tests/unit",
            "tests/integration",
            "docs",
            ".github/workflows",
        ]
        for dir_name in directories:
            (path / dir_name).mkdir(parents=True, exist_ok=True)
```

### Project Structure Template

```
my-project/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       └── security.yml
├── src/
│   ├── api/
│   │   ├── routes/
│   │   ├── middleware/
│   │   └── handlers/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── index.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── api/
│   └── architecture/
├── scripts/
│   ├── setup.sh
│   └── deploy.sh
├── .env.example
├── .gitignore
├── package.json
├── tsconfig.json
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Code Generation (da-02)

### CRUD Generator

```typescript
// crud-generator.ts

interface ModelDefinition {
  name: string;
  fields: Field[];
  timestamps?: boolean;
  softDelete?: boolean;
}

interface Field {
  name: string;
  type: string;
  required?: boolean;
  unique?: boolean;
  default?: any;
}

class CRUDGenerator {
  /**
   * Generate complete CRUD for a model
   */
  generate(model: ModelDefinition): GeneratedFiles {
    return {
      model: this.generateModel(model),
      repository: this.generateRepository(model),
      service: this.generateService(model),
      controller: this.generateController(model),
      routes: this.generateRoutes(model),
      dto: this.generateDTOs(model),
      tests: this.generateTests(model),
    };
  }

  private generateModel(model: ModelDefinition): string {
    const fields = model.fields
      .map((f) => `  ${f.name}: ${this.mapType(f.type)};`)
      .join("\n");

    return `
export interface ${model.name} {
  id: string;
${fields}
${model.timestamps ? "  createdAt: Date;\n  updatedAt: Date;" : ""}
${model.softDelete ? "  deletedAt?: Date;" : ""}
}
    `.trim();
  }

  private generateRepository(model: ModelDefinition): string {
    const name = model.name;
    const varName = name.toLowerCase();

    return `
import { ${name} } from '../models/${varName}';

export class ${name}Repository {
  async findAll(options?: FindOptions): Promise<${name}[]> {
    // Implementation
  }

  async findById(id: string): Promise<${name} | null> {
    // Implementation
  }

  async create(data: Create${name}DTO): Promise<${name}> {
    // Implementation
  }

  async update(id: string, data: Update${name}DTO): Promise<${name}> {
    // Implementation
  }

  async delete(id: string): Promise<void> {
    // Implementation
  }
}
    `.trim();
  }

  // Additional generation methods...
}

// Usage
const generator = new CRUDGenerator();
const files = generator.generate({
  name: "User",
  fields: [
    { name: "email", type: "string", required: true, unique: true },
    { name: "name", type: "string", required: true },
    { name: "role", type: "string", default: "user" },
  ],
  timestamps: true,
  softDelete: true,
});
```

### Type Generation from Schema

```typescript
// schema-to-types.ts

/**
 * Generate TypeScript types from JSON Schema
 */
function generateTypesFromSchema(schema: JSONSchema): string {
  const types: string[] = [];

  function processSchema(
    schema: JSONSchema,
    name: string,
    required: string[] = []
  ): string {
    if (schema.type === "object" && schema.properties) {
      const props = Object.entries(schema.properties).map(([key, prop]) => {
        const isRequired = required.includes(key);
        const type = getTypeFromSchema(prop as JSONSchema);
        return `  ${key}${isRequired ? "" : "?"}: ${type};`;
      });

      return `export interface ${name} {\n${props.join("\n")}\n}`;
    }
    return "";
  }

  function getTypeFromSchema(schema: JSONSchema): string {
    switch (schema.type) {
      case "string":
        return schema.enum
          ? schema.enum.map((e) => `'${e}'`).join(" | ")
          : "string";
      case "number":
      case "integer":
        return "number";
      case "boolean":
        return "boolean";
      case "array":
        return `${getTypeFromSchema(schema.items as JSONSchema)}[]`;
      case "object":
        return "Record<string, unknown>";
      default:
        return "unknown";
    }
  }

  types.push(
    processSchema(schema, schema.title || "Generated", schema.required)
  );
  return types.join("\n\n");
}
```

## Test Automation (da-03)

### Test Generator

```python
# test_generator.py
from dataclasses import dataclass
from typing import List, Optional
import ast
import inspect

@dataclass
class TestCase:
    name: str
    description: str
    setup: Optional[str]
    action: str
    assertion: str
    teardown: Optional[str]

class TestGenerator:
    """Generate test cases from code analysis."""

    def generate_unit_tests(self, source_file: str) -> str:
        """Generate unit tests for a Python module."""
        with open(source_file) as f:
            tree = ast.parse(f.read())

        tests = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                tests.extend(self._generate_function_tests(node))
            elif isinstance(node, ast.ClassDef):
                tests.extend(self._generate_class_tests(node))

        return self._format_test_file(tests)

    def _generate_function_tests(self, func: ast.FunctionDef) -> List[TestCase]:
        """Generate tests for a function."""
        tests = []

        # Happy path test
        tests.append(TestCase(
            name=f"test_{func.name}_success",
            description=f"Test {func.name} with valid input",
            setup=None,
            action=f"result = {func.name}(valid_input)",
            assertion="assert result is not None",
            teardown=None
        ))

        # Edge case: empty input
        tests.append(TestCase(
            name=f"test_{func.name}_empty_input",
            description=f"Test {func.name} with empty input",
            setup=None,
            action=f"result = {func.name}(None)",
            assertion="# Verify appropriate handling",
            teardown=None
        ))

        # Error case
        tests.append(TestCase(
            name=f"test_{func.name}_invalid_input",
            description=f"Test {func.name} with invalid input",
            setup=None,
            action=f"with pytest.raises(ValueError):\n        {func.name}(invalid_input)",
            assertion="",
            teardown=None
        ))

        return tests

    def _format_test_file(self, tests: List[TestCase]) -> str:
        """Format test cases into a test file."""
        lines = [
            "import pytest",
            "from unittest.mock import Mock, patch",
            "",
            "# Generated tests",
            "",
        ]

        for test in tests:
            lines.append(f"def {test.name}():")
            lines.append(f'    """{test.description}"""')
            if test.setup:
                lines.append(f"    # Setup")
                lines.append(f"    {test.setup}")
            lines.append(f"    # Action")
            lines.append(f"    {test.action}")
            if test.assertion:
                lines.append(f"    # Assert")
                lines.append(f"    {test.assertion}")
            if test.teardown:
                lines.append(f"    # Teardown")
                lines.append(f"    {test.teardown}")
            lines.append("")

        return "\n".join(lines)
```

### Test Template Library

```typescript
// test-templates.ts

/**
 * Common test patterns
 */
const testTemplates = {
  // Unit test template
  unit: `
describe('{{moduleName}}', () => {
  describe('{{methodName}}', () => {
    it('should return expected result for valid input', () => {
      // Arrange
      const input = {{validInput}};
      const expected = {{expectedOutput}};

      // Act
      const result = {{methodName}}(input);

      // Assert
      expect(result).toEqual(expected);
    });

    it('should throw error for invalid input', () => {
      // Arrange
      const invalidInput = {{invalidInput}};

      // Act & Assert
      expect(() => {{methodName}}(invalidInput)).toThrow();
    });

    it('should handle edge cases', () => {
      // Arrange
      const edgeCase = {{edgeCaseInput}};

      // Act
      const result = {{methodName}}(edgeCase);

      // Assert
      expect(result).toBeDefined();
    });
  });
});
  `,

  // Integration test template
  integration: `
describe('{{featureName}} Integration', () => {
  let app: Application;
  let db: Database;

  beforeAll(async () => {
    db = await setupTestDatabase();
    app = await createTestApp(db);
  });

  afterAll(async () => {
    await db.close();
  });

  beforeEach(async () => {
    await db.clear();
    await seedTestData(db);
  });

  it('should complete end-to-end workflow', async () => {
    // Step 1: Create resource
    const createResponse = await request(app)
      .post('/api/{{resource}}')
      .send({{createPayload}});
    expect(createResponse.status).toBe(201);

    const id = createResponse.body.id;

    // Step 2: Read resource
    const getResponse = await request(app)
      .get(\`/api/{{resource}}/\${id}\`);
    expect(getResponse.status).toBe(200);

    // Step 3: Update resource
    const updateResponse = await request(app)
      .put(\`/api/{{resource}}/\${id}\`)
      .send({{updatePayload}});
    expect(updateResponse.status).toBe(200);

    // Step 4: Delete resource
    const deleteResponse = await request(app)
      .delete(\`/api/{{resource}}/\${id}\`);
    expect(deleteResponse.status).toBe(204);
  });
});
  `,

  // API test template
  api: `
describe('API: {{endpoint}}', () => {
  describe('GET {{endpoint}}', () => {
    it('should return 200 with data', async () => {
      const response = await request(app).get('{{endpoint}}');
      expect(response.status).toBe(200);
      expect(response.body).toHaveProperty('data');
    });

    it('should return 401 without auth', async () => {
      const response = await request(app)
        .get('{{endpoint}}')
        .set('Authorization', '');
      expect(response.status).toBe(401);
    });
  });

  describe('POST {{endpoint}}', () => {
    it('should create and return 201', async () => {
      const payload = {{createPayload}};
      const response = await request(app)
        .post('{{endpoint}}')
        .send(payload);
      expect(response.status).toBe(201);
    });

    it('should return 400 for invalid data', async () => {
      const response = await request(app)
        .post('{{endpoint}}')
        .send({});
      expect(response.status).toBe(400);
    });
  });
});
  `,
};
```

## Rapid API Development (da-04)

### OpenAPI Generator

```typescript
// openapi-generator.ts

interface EndpointDefinition {
  path: string;
  method: "get" | "post" | "put" | "patch" | "delete";
  summary: string;
  requestBody?: SchemaDefinition;
  responses: Record<number, SchemaDefinition>;
  auth?: boolean;
  tags?: string[];
}

class OpenAPIGenerator {
  private spec: OpenAPISpec = {
    openapi: "3.0.3",
    info: {
      title: "API",
      version: "1.0.0",
    },
    paths: {},
    components: {
      schemas: {},
      securitySchemes: {
        bearerAuth: {
          type: "http",
          scheme: "bearer",
          bearerFormat: "JWT",
        },
      },
    },
  };

  addEndpoint(endpoint: EndpointDefinition): this {
    if (!this.spec.paths[endpoint.path]) {
      this.spec.paths[endpoint.path] = {};
    }

    this.spec.paths[endpoint.path][endpoint.method] = {
      summary: endpoint.summary,
      tags: endpoint.tags,
      security: endpoint.auth ? [{ bearerAuth: [] }] : undefined,
      requestBody: endpoint.requestBody
        ? {
            required: true,
            content: {
              "application/json": {
                schema: this.resolveSchema(endpoint.requestBody),
              },
            },
          }
        : undefined,
      responses: Object.fromEntries(
        Object.entries(endpoint.responses).map(([code, schema]) => [
          code,
          {
            description: this.getResponseDescription(Number(code)),
            content: {
              "application/json": {
                schema: this.resolveSchema(schema),
              },
            },
          },
        ])
      ),
    };

    return this;
  }

  addSchema(name: string, schema: SchemaDefinition): this {
    this.spec.components.schemas[name] = schema;
    return this;
  }

  generate(): string {
    return JSON.stringify(this.spec, null, 2);
  }
}

// Usage
const api = new OpenAPIGenerator()
  .addSchema("User", {
    type: "object",
    properties: {
      id: { type: "string", format: "uuid" },
      email: { type: "string", format: "email" },
      name: { type: "string" },
    },
    required: ["id", "email", "name"],
  })
  .addEndpoint({
    path: "/users",
    method: "get",
    summary: "List all users",
    auth: true,
    tags: ["Users"],
    responses: {
      200: { $ref: "#/components/schemas/User" },
    },
  })
  .addEndpoint({
    path: "/users",
    method: "post",
    summary: "Create a user",
    auth: true,
    tags: ["Users"],
    requestBody: { $ref: "#/components/schemas/CreateUser" },
    responses: {
      201: { $ref: "#/components/schemas/User" },
      400: { $ref: "#/components/schemas/Error" },
    },
  });

console.log(api.generate());
```

### Express Router Generator

```typescript
// router-generator.ts

function generateExpressRouter(openApiSpec: OpenAPISpec): string {
  const routes: string[] = [];

  for (const [path, methods] of Object.entries(openApiSpec.paths)) {
    for (const [method, operation] of Object.entries(methods)) {
      const handlerName = operation.operationId || `handle${method}${path}`;
      const expressPath = path.replace(/{(\w+)}/g, ":$1");

      routes.push(`
router.${method}('${expressPath}',
  ${operation.security ? "authenticate," : ""}
  validate(${handlerName}Schema),
  asyncHandler(${handlerName})
);`);
    }
  }

  return `
import { Router } from 'express';
import { asyncHandler, validate, authenticate } from './middleware';

const router = Router();

${routes.join("\n")}

export default router;
  `.trim();
}
```

## Integration Patterns (da-05)

### Webhook Handler

```typescript
// webhook-handler.ts

interface WebhookConfig {
  endpoint: string;
  secret: string;
  events: string[];
  retryPolicy: RetryPolicy;
}

class WebhookHandler {
  /**
   * Receive and validate incoming webhooks
   */
  async handleIncoming(
    req: Request,
    config: WebhookConfig
  ): Promise<WebhookResult> {
    // Verify signature
    const signature = req.headers["x-webhook-signature"];
    if (!this.verifySignature(req.body, signature, config.secret)) {
      throw new WebhookError("Invalid signature", 401);
    }

    // Parse event
    const event = this.parseEvent(req.body);

    // Check if event is subscribed
    if (!config.events.includes(event.type)) {
      return { status: "ignored", event: event.type };
    }

    // Process event
    await this.processEvent(event);

    return { status: "processed", event: event.type };
  }

  /**
   * Send outgoing webhooks with retry
   */
  async sendWebhook(
    url: string,
    payload: unknown,
    config: WebhookConfig
  ): Promise<void> {
    const signature = this.signPayload(payload, config.secret);

    for (let attempt = 0; attempt <= config.retryPolicy.maxRetries; attempt++) {
      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature,
          },
          body: JSON.stringify(payload),
        });

        if (response.ok) {
          return;
        }

        if (!this.isRetryable(response.status)) {
          throw new WebhookError(`Non-retryable error: ${response.status}`);
        }
      } catch (error) {
        if (attempt === config.retryPolicy.maxRetries) {
          throw error;
        }
        await this.delay(this.calculateBackoff(attempt, config.retryPolicy));
      }
    }
  }

  private verifySignature(
    payload: unknown,
    signature: string,
    secret: string
  ): boolean {
    const expected = crypto
      .createHmac("sha256", secret)
      .update(JSON.stringify(payload))
      .digest("hex");
    return crypto.timingSafeEqual(
      Buffer.from(signature),
      Buffer.from(expected)
    );
  }
}
```

### Event-Driven Pattern

```typescript
// event-bus.ts

type EventHandler<T = unknown> = (event: T) => Promise<void>;

class EventBus {
  private handlers: Map<string, EventHandler[]> = new Map();

  /**
   * Subscribe to an event
   */
  on<T>(eventType: string, handler: EventHandler<T>): void {
    const handlers = this.handlers.get(eventType) || [];
    handlers.push(handler as EventHandler);
    this.handlers.set(eventType, handlers);
  }

  /**
   * Publish an event
   */
  async emit<T>(eventType: string, payload: T): Promise<void> {
    const handlers = this.handlers.get(eventType) || [];

    // Execute handlers in parallel
    await Promise.all(handlers.map((handler) => handler(payload)));
  }

  /**
   * Publish event with guaranteed delivery (via queue)
   */
  async emitReliable<T>(eventType: string, payload: T): Promise<void> {
    // Store event in database/queue
    await this.persistEvent(eventType, payload);

    // Process asynchronously
    this.processAsync(eventType, payload);
  }
}

// Usage
const eventBus = new EventBus();

// Subscribe to events
eventBus.on("user.created", async (user: User) => {
  await sendWelcomeEmail(user);
});

eventBus.on("user.created", async (user: User) => {
  await createDefaultSettings(user);
});

eventBus.on("order.completed", async (order: Order) => {
  await processPayment(order);
  await updateInventory(order);
  await sendConfirmation(order);
});

// Publish events
await eventBus.emit("user.created", newUser);
await eventBus.emit("order.completed", completedOrder);
```

### OAuth Integration

```typescript
// oauth-integration.ts

interface OAuthConfig {
  clientId: string;
  clientSecret: string;
  redirectUri: string;
  scopes: string[];
}

class OAuthIntegration {
  constructor(
    private provider: string,
    private config: OAuthConfig
  ) {}

  /**
   * Generate authorization URL
   */
  getAuthorizationUrl(state: string): string {
    const params = new URLSearchParams({
      client_id: this.config.clientId,
      redirect_uri: this.config.redirectUri,
      scope: this.config.scopes.join(" "),
      state,
      response_type: "code",
    });

    return `${this.getProviderUrl("authorize")}?${params}`;
  }

  /**
   * Exchange code for tokens
   */
  async exchangeCode(code: string): Promise<TokenResponse> {
    const response = await fetch(this.getProviderUrl("token"), {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        client_id: this.config.clientId,
        client_secret: this.config.clientSecret,
        code,
        redirect_uri: this.config.redirectUri,
        grant_type: "authorization_code",
      }),
    });

    return response.json();
  }

  /**
   * Refresh access token
   */
  async refreshToken(refreshToken: string): Promise<TokenResponse> {
    const response = await fetch(this.getProviderUrl("token"), {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        client_id: this.config.clientId,
        client_secret: this.config.clientSecret,
        refresh_token: refreshToken,
        grant_type: "refresh_token",
      }),
    });

    return response.json();
  }
}
```

## Integration with Other Roles

**Development Accelerator coordinates with:**

- **Project Guardian (pg-01)**: Health monitoring setup
- **DevOps (do-01)**: CI/CD scaffolding
- **Security Architect (sa-05)**: Secure code templates
- **Code Hardener (ch-01 to ch-05)**: Production-ready patterns
- **QA Engineer (qa-01)**: Test infrastructure

## Best Practices

1. **Start with Templates** - Use scaffolding to maintain consistency
2. **Generate, Don't Repeat** - Automate repetitive code
3. **Test Early** - Generate tests alongside code
4. **Document APIs** - Generate OpenAPI specs from code
5. **Use Standards** - Follow established integration patterns
6. **Security by Default** - Include security in generated code

## Quick Start

```bash
# Scaffold new project
@dev-accelerator da-01 "Create new TypeScript REST API project"

# Generate CRUD
@dev-accelerator da-02 "Generate CRUD for User model"

# Generate tests
@dev-accelerator da-03 "Generate unit tests for user service"

# Create API
@dev-accelerator da-04 "Create REST endpoints for orders"

# Add integration
@dev-accelerator da-05 "Add Stripe webhook integration"
```

## Documentation

Detailed documentation for each skill is in `.claude/roles/dev-accelerator/skills/{skill-id}/README.md`
