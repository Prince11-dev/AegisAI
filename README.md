<div align="center">

# 🚀 AegisAI

### Open-Source Enterprise AI Platform for Building Intelligent Agents, RAG Applications, and AI Workflows

Build • Orchestrate • Deploy • Scale • Integrate

<p>

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-15-000000?logo=nextdotjs)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Under%20Development-orange)

</p>

*A modern, production-inspired AI platform designed for developers, engineering teams, and open-source contributors.*

</div>

---

# 📖 Overview

AegisAI is an open-source enterprise AI platform for building intelligent applications powered by **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, **AI Agents**, and **workflow orchestration**.

The project demonstrates how modern AI systems can be architected using production-grade software engineering practices while remaining fully open source and developer friendly.

Rather than being a simple chatbot application, AegisAI provides a modular platform for developing, deploying, and operating AI-powered services using local and cloud-based models through a unified architecture.

---

# 🎯 Vision

Our vision is to make enterprise-grade AI development accessible to everyone.

AegisAI aims to become a reference implementation for building scalable AI platforms by combining:

- Modern backend engineering
- Modular architecture
- AI workflow orchestration
- Retrieval-Augmented Generation (RAG)
- Multi-agent systems
- Secure APIs
- Production-ready deployment
- Comprehensive documentation

The platform is designed for learning, experimentation, and production-inspired engineering.

---

# ❓ Why AegisAI?

Many AI projects focus on a single capability such as chat interfaces, prompt engineering, or document retrieval.

AegisAI takes a broader approach by providing an integrated platform where multiple AI capabilities work together within a unified architecture.

### Key Objectives

- Build production-ready AI systems
- Support local-first AI with Ollama
- Enable Retrieval-Augmented Generation (RAG)
- Orchestrate intelligent AI agents
- Integrate with external services through provider abstractions
- Demonstrate modern software engineering practices
- Encourage open-source collaboration
- Serve as a learning resource for AI platform architecture

---

# ✨ Core Capabilities

### 🤖 AI

- Multi-Agent Workflows
- Retrieval-Augmented Generation (RAG)
- Conversational AI
- Prompt Engineering
- Tool Calling
- Semantic Search
- Embedding Management
- Context Retrieval
- Local LLM Inference

### 🏗 Platform

- FastAPI Backend
- Next.js Frontend
- PostgreSQL
- ChromaDB
- Redis
- JWT Authentication
- Role-Based Access Control (RBAC)
- Docker Deployment
- Observability
- Modular Architecture

---

# 🚧 Project Status

AegisAI is currently under active development.

Current progress includes:

- ✅ Core architecture completed
- ✅ System design documented
- ✅ AI architecture documented
- ✅ Database architecture documented
- ✅ API architecture documented
- ✅ Security architecture documented
- ✅ Deployment architecture documented
- ✅ Disaster recovery architecture documented
- ✅ Architecture Decision Records (ADRs)

The implementation phase is now underway.

---

# 🏛 Architecture Overview

AegisAI follows a **Modular Monolith Architecture**, providing the simplicity of a single deployable application while maintaining clear module boundaries and enabling future migration to microservices if operational requirements evolve.

The platform is designed around modern software engineering principles including:

- Modular Design
- Clean Architecture
- API-First Development
- Domain-Driven Design (DDD)
- SOLID Principles
- Separation of Concerns
- Repository Pattern
- Provider Abstraction
- Twelve-Factor App Methodology

---

## High-Level Architecture

```text
                              Users
                                │
                                ▼
                     Next.js Frontend (UI)
                                │
                                ▼
                      FastAPI REST API Layer
                                │
      ┌───────────────┬──────────┴──────────┬───────────────┐
      │               │                     │               │
      ▼               ▼                     ▼               ▼
 Authentication   AI Services         Document Service   Admin APIs
      │               │                     │
      └───────────────┴──────────┬──────────┘
                                 ▼
                         LangGraph Orchestrator
                                 │
         ┌──────────────┬─────────┴──────────┬──────────────┐
         ▼              ▼                    ▼              ▼
    PostgreSQL       ChromaDB             Redis         Ollama
         │
         ▼
 External Providers (OpenAI, Gemini, Claude, Groq, etc.)
```

---

# 🧩 Core Components

The platform is organised into modular components, each with a clearly defined responsibility.

| Component | Responsibility |
|-----------|----------------|
| Authentication | User authentication, JWT, RBAC |
| AI Service | LLM interactions and orchestration |
| Agent Framework | Multi-agent collaboration |
| RAG Engine | Retrieval-Augmented Generation |
| Document Service | Document ingestion and processing |
| Embedding Service | Vector generation |
| Search Service | Semantic search |
| Connector Framework | External integrations |
| Administration | User, roles and system management |
| Observability | Metrics, logging and tracing |

---

# ⚙️ Technology Stack

## Frontend

| Technology | Purpose |
|------------|---------|
| Next.js | Web application |
| React | User Interface |
| TypeScript | Type safety |
| Tailwind CSS | Styling |

---

## Backend

| Technology | Purpose |
|------------|---------|
| FastAPI | REST APIs |
| Python | Core language |
| SQLAlchemy | ORM |
| Pydantic | Validation |
| Alembic | Database migrations |

---

## Artificial Intelligence

| Technology | Purpose |
|------------|---------|
| LangGraph | Agent orchestration |
| LangChain | AI components |
| Ollama | Local LLM runtime |
| Hugging Face | Embeddings and models |
| Sentence Transformers | Embedding generation |

---

## Data Layer

| Technology | Purpose |
|------------|---------|
| PostgreSQL | System of record |
| ChromaDB | Vector database |
| Redis | Cache and sessions |
| Local File System | Document storage (v1) |

---

## DevOps

| Technology | Purpose |
|------------|---------|
| Docker | Containerization |
| Docker Compose | Local orchestration |
| GitHub Actions | CI/CD |
| Kubernetes | Future production orchestration |

---

## Observability

| Technology | Purpose |
|------------|---------|
| OpenTelemetry | Distributed tracing |
| Prometheus | Metrics |
| Grafana | Dashboards |
| Structured Logging | Diagnostics |

---

# 📂 Repository Structure

```text
AegisAI/
│
├── apps/                  # Frontend and backend applications
├── architecture/          # Architecture documentation
│   ├── adr/
│   ├── overview.md
│   ├── system-design.md
│   ├── api-design.md
│   ├── database-design.md
│   ├── ai-architecture.md
│   ├── deployment.md
│   ├── security.md
│   └── ...
│
├── docs/                  # User documentation
├── infrastructure/        # Docker, Kubernetes and IaC
├── scripts/               # Utility scripts
├── tests/                 # Test suites
├── packages/              # Shared libraries
├── connectors/            # External integrations
├── agents/                # AI agents
├── services/              # Business services
├── .github/               # GitHub workflows and templates
└── README.md
```

---

# 📚 Documentation

The project includes comprehensive architecture and engineering documentation.

| Category | Documents |
|----------|-----------|
| Architecture | Overview, System Design, AI Architecture |
| API | API Design |
| Data | Database Design |
| Operations | Deployment, Observability, Disaster Recovery |
| Engineering | Development Guide, Testing Strategy |
| Security | Security Architecture |
| Decisions | Architecture Decision Records (ADRs) |

For detailed information, see the [`architecture/`](architecture/) directory.

---

# 🏗 Design Principles

AegisAI is built around the following engineering principles:

- **Modularity** – Independent business modules with clear responsibilities.
- **Maintainability** – Clean, readable, and testable code.
- **Extensibility** – New providers and features can be added with minimal changes.
- **Security by Design** – Security is integrated throughout the platform.
- **Observability** – Logs, metrics, and traces are first-class concerns.
- **Scalability** – Components are designed to grow with increasing workloads.
- **Developer Experience** – Simple local setup and consistent workflows.
- **Documentation-Driven Development** – Architecture and decisions are documented before implementation.

---

# 🚀 Getting Started

This guide helps you set up AegisAI for local development.

The recommended development environment uses **Docker Compose**, allowing all required services to run with minimal configuration.

---

# 📋 Prerequisites

Before getting started, ensure the following tools are installed.

| Software | Recommended Version |
|----------|---------------------|
| Git | Latest |
| Python | 3.12+ |
| Node.js | 22 LTS |
| Docker Desktop | Latest |
| Docker Compose | Latest |
| PostgreSQL | 16+ (Optional if using Docker) |
| Ollama | Latest |

---

# 🖥 System Requirements

## Minimum

- 4 CPU Cores
- 8 GB RAM
- 20 GB Free Disk Space

## Recommended

- 8 CPU Cores
- 16 GB RAM
- NVIDIA GPU (Optional)
- 50 GB SSD

---

# 📥 Clone the Repository

```bash
git clone https://github.com/<your-username>/AegisAI.git

cd AegisAI
```

---

# 📦 Install Dependencies

## Backend

```bash
cd apps/backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Frontend

```bash
cd apps/frontend

npm install
```

---

# 🐳 Docker Development

The easiest way to start AegisAI is using Docker Compose.

```bash
docker compose up --build
```

This starts:

- Frontend
- Backend API
- PostgreSQL
- Redis
- ChromaDB
- Ollama

---

# ⚙️ Environment Configuration

Create a local environment file.

```bash
cp .env.example .env
```

Example:

```env
APP_ENV=development

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/aegisai

REDIS_URL=redis://localhost:6379

CHROMA_HOST=localhost

OLLAMA_HOST=http://localhost:11434

JWT_SECRET=change-me

LOG_LEVEL=INFO
```

> **Note:** The `.env.example` file should contain all available configuration options with sensible defaults. Do not commit secrets to version control.

---

# ▶️ Running the Application

## Backend

```bash
cd apps/backend

uvicorn app.main:app --reload
```

Backend URL

```
http://localhost:8000
```

API Documentation

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd apps/frontend

npm run dev
```

Frontend URL

```
http://localhost:3000
```

---

# 🧪 Verify the Installation

Once the services are running, verify that everything is working.

| Service | URL |
|----------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| OpenAPI JSON | http://localhost:8000/openapi.json |
| Ollama | http://localhost:11434 |

---

# 📁 Environment Variables

The following variables are required for local development.

| Variable | Description |
|----------|-------------|
| APP_ENV | Application environment |
| DATABASE_URL | PostgreSQL connection |
| REDIS_URL | Redis connection |
| CHROMA_HOST | ChromaDB host |
| OLLAMA_HOST | Ollama endpoint |
| JWT_SECRET | JWT signing secret |
| LOG_LEVEL | Logging level |

Refer to the `.env.example` file for the complete list of supported configuration options.

---

# 🔧 Troubleshooting

### Docker does not start

Verify Docker Desktop is running.

```bash
docker ps
```

---

### Ollama is unavailable

Verify the Ollama service.

```bash
ollama list
```

---

### Backend cannot connect to PostgreSQL

Check the database container.

```bash
docker compose ps
```

Review the logs.

```bash
docker compose logs postgres
```

---

### API documentation is unavailable

Verify the backend is running.

```
http://localhost:8000/docs
```

If unavailable, inspect the backend logs for startup errors.

---

# 👨‍💻 Development Workflow

AegisAI follows a documentation-driven and feature-based development workflow to ensure consistency, maintainability, and high code quality.

## Development Principles

- Documentation before implementation
- Feature-based development
- Clean Architecture
- API-first design
- Test-first mindset
- Small, focused pull requests
- Code reviews for all major changes

---

## Typical Development Flow

1. Create a feature branch.
2. Update or create relevant architecture documentation if required.
3. Implement the feature.
4. Add or update automated tests.
5. Run formatting and linting.
6. Verify all tests pass.
7. Submit a Pull Request.

---

## Branch Strategy

| Branch | Purpose |
|----------|----------|
| `main` | Stable production-ready code |
| `develop` | Active development |
| `feature/*` | New features |
| `bugfix/*` | Bug fixes |
| `hotfix/*` | Critical production fixes |
| `release/*` | Release preparation |

---

# 🧪 Testing

Quality is a core principle of AegisAI.

Testing is performed at multiple levels to ensure reliability and maintainability.

## Testing Strategy

- Unit Tests
- Integration Tests
- API Tests
- AI Workflow Tests
- End-to-End Tests
- Performance Tests

---

## Backend Tests

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app
```

---

## Frontend Tests

```bash
npm test
```

---

## Linting

### Backend

```bash
ruff check .

black .
```

---

### Frontend

```bash
npm run lint
```

---

# 🚀 Deployment

AegisAI is designed to support multiple deployment environments.

## Local Development

- Docker Compose

---

## Production

- Docker
- Kubernetes

---

## Supported Infrastructure

- Linux
- Windows
- macOS
- Cloud Virtual Machines
- Kubernetes Clusters

---

## Deployment Architecture

```text
Internet
    │
    ▼
Load Balancer
    │
    ▼
Next.js Frontend
    │
    ▼
FastAPI Backend
    │
    ▼
──────────────────────────
│ PostgreSQL             │
│ Redis                  │
│ ChromaDB               │
│ Ollama                 │
──────────────────────────
```

---

## Deployment Documentation

Detailed deployment guidance is available in:

- `architecture/deployment.md`
- `architecture/disaster-recovery.md`

---

# 📊 Observability

AegisAI is designed with observability built in from the beginning.

Monitoring includes:

- Structured logging
- Distributed tracing
- Metrics collection
- Health checks
- Performance monitoring
- Error tracking

---

## Monitoring Stack

| Tool | Purpose |
|-------|----------|
| Prometheus | Metrics |
| Grafana | Dashboards |
| OpenTelemetry | Tracing |
| Structured Logging | Diagnostics |

---

# 🔒 Security

Security is integrated throughout the platform.

Key security features include:

- JWT Authentication
- Role-Based Access Control (RBAC)
- Password Hashing
- Secure API Design
- Environment-based Configuration
- Secret Management
- Input Validation
- SQL Injection Protection
- CORS Configuration
- Security Headers

---

## Security Documentation

For detailed information, see:

- `architecture/security.md`

---

# 📈 Performance

Performance considerations include:

- Redis caching
- Database indexing
- Efficient vector search
- Connection pooling
- Async request handling
- Streaming responses
- Lazy loading
- Optimized AI pipelines

Detailed performance guidance is available in:

- `architecture/performance-architecture.md`

---

# 🤝 Contributing

Contributions are welcome and appreciated.

Whether you're fixing bugs, improving documentation, implementing new features, or proposing architectural enhancements, your contributions help make AegisAI better.

## How to Contribute

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Ensure all tests pass.
5. Commit your changes.

```bash
git commit -m "feat: add new feature"
```

6. Push your branch.

```bash
git push origin feature/your-feature
```

7. Open a Pull Request.

---

## Contribution Guidelines

Please ensure:

- Code follows the existing project structure.
- New functionality includes tests where applicable.
- Documentation is updated when introducing changes.
- Commit messages follow the Conventional Commits specification.
- Pull Requests remain focused and easy to review.

Future contribution guidelines will be documented in:

```
CONTRIBUTING.md
```

---

# 🗺️ Roadmap

The project will evolve incrementally through well-defined milestones.

## Phase 1 — Foundation

- [x] Repository initialization
- [x] Architecture documentation
- [x] Architecture Decision Records (ADRs)
- [ ] CI/CD pipeline
- [ ] Development tooling

---

## Phase 2 — Core Platform

- [ ] FastAPI backend
- [ ] PostgreSQL integration
- [ ] Authentication
- [ ] Role-Based Access Control (RBAC)
- [ ] REST API

---

## Phase 3 — AI Platform

- [ ] Ollama integration
- [ ] Chat interface
- [ ] Prompt management
- [ ] Streaming responses
- [ ] Model management

---

## Phase 4 — Retrieval-Augmented Generation

- [ ] Document ingestion
- [ ] Embedding pipeline
- [ ] ChromaDB integration
- [ ] Semantic search
- [ ] Knowledge retrieval

---

## Phase 5 — Multi-Agent Framework

- [ ] LangGraph orchestration
- [ ] Planner agent
- [ ] Research agent
- [ ] Coding agent
- [ ] Review agent

---

## Phase 6 — Enterprise Features

- [ ] GitHub integration
- [ ] PostgreSQL connector
- [ ] Webhooks
- [ ] Background jobs
- [ ] Audit logging

---

## Phase 7 — Production Readiness

- [ ] Monitoring
- [ ] Metrics
- [ ] Distributed tracing
- [ ] Kubernetes deployment
- [ ] Disaster recovery
- [ ] Performance optimisation

---

# 📚 Project Documentation

Comprehensive documentation is available in the `architecture/` directory.

| Document | Description |
|----------|-------------|
| `overview.md` | Platform overview |
| `system-design.md` | System architecture |
| `database-design.md` | Database architecture |
| `api-design.md` | API design |
| `ai-architecture.md` | AI architecture |
| `deployment.md` | Deployment strategy |
| `security.md` | Security architecture |
| `observability.md` | Monitoring and telemetry |
| `performance-architecture.md` | Performance strategy |
| `testing-strategy.md` | Testing approach |
| `development-guide.md` | Development standards |
| `disaster-recovery.md` | Disaster recovery |
| `adr/` | Architecture Decision Records |

---

# 💬 Community & Support

Community resources will expand as the project grows.

Future channels include:

- GitHub Discussions
- GitHub Issues
- Feature Requests
- Documentation Improvements

When reporting bugs, please include:

- Operating System
- Python version
- Docker version (if applicable)
- Steps to reproduce
- Expected behaviour
- Actual behaviour
- Relevant logs or screenshots

---

# ⭐ Support the Project

If you find AegisAI useful, consider supporting the project by:

- ⭐ Starring the repository
- 🍴 Forking the project
- 🐛 Reporting issues
- 💡 Suggesting new features
- 📖 Improving documentation
- 🤝 Contributing code
- 📣 Sharing the project with others

Every contribution, no matter how small, helps improve the project.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for full license details.

---

# 🙏 Acknowledgements

AegisAI is built using a number of exceptional open-source technologies and communities.

Special thanks to the maintainers and contributors of:

- Python
- FastAPI
- Next.js
- React
- LangChain
- LangGraph
- Ollama
- Hugging Face
- PostgreSQL
- ChromaDB
- Redis
- Docker
- Kubernetes
- Prometheus
- Grafana
- OpenTelemetry

Their work makes projects like AegisAI possible.

---

<div align="center">

# 🚀 AegisAI

### Build • Orchestrate • Deploy • Scale

**Open-Source Enterprise AI Platform**

Built with ❤️ for developers, engineers, learners, and the open-source community.

⭐ If you like this project, consider giving it a star.

</div>