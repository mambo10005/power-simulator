# Stage 1 – Infrastructure Foundation

**Document:** 03-stage-1-infrastructure-foundation.md

**Version:** 1.0

**Status:** Planned

**Duration:** Weeks 3–5

---

# Purpose

The objective of Stage 1 is to establish the production-quality infrastructure that will support all future development of the Electricity Market Simulator.

This stage creates the software foundation upon which the network model, optimization engine, market clearing engine, settlement engine, analytics platform, and AI copilot will be built.

No electricity market logic is implemented during this stage.

Instead, the focus is on building a reliable, maintainable, and extensible engineering platform.

---

# Objectives

At the completion of this stage, the project will provide:

* Production-ready FastAPI backend
* PostgreSQL 17 database
* TimescaleDB extension
* Redis cache
* SQLAlchemy ORM
* Alembic database migrations
* Docker Compose infrastructure
* Environment configuration
* GitHub Actions CI pipeline
* Automated unit testing
* Standardized repository structure

---

# Business Value

This stage establishes the infrastructure required to support future commercial capabilities, including:

* ISO/RTO market simulation
* Security-Constrained Unit Commitment (SCUC)
* Security-Constrained Economic Dispatch (SCED)
* DC Optimal Power Flow (DCOPF)
* Locational Marginal Pricing (LMP)
* Market settlements
* Battery optimization
* Virtual Power Plant (VPP)
* Risk analytics
* AI-powered market analysis

---

# Scope

## Included

### Backend Framework

* FastAPI
* Pydantic v2
* SQLAlchemy 2

### Database

* PostgreSQL 17
* TimescaleDB
* Redis

### Infrastructure

* Docker Compose
* Environment configuration
* Dockerfile

### Database Management

* Alembic migrations
* Initial schema
* Hypertable configuration

### Development

* uv package management
* Virtual environments
* Repository structure
* Logging foundation

### Quality

* Pytest
* GitHub Actions
* Health endpoint

---

## Excluded

The following capabilities are intentionally deferred to later stages:

* Power flow analysis
* IEEE test systems
* Market clearing
* SCED
* SCUC
* DCOPF
* LMP calculation
* Battery optimization
* Renewable generation
* React frontend
* AI market copilot

---

# Technology Stack

## Backend

* Python 3.13
* FastAPI
* Pydantic v2
* SQLAlchemy 2
* Alembic

## Database

* PostgreSQL 17
* TimescaleDB
* Redis

## Infrastructure

* Docker
* Docker Compose
* uv
* Git

## Testing

* Pytest
* HTTPX

## CI/CD

* GitHub Actions

---

# Repository Structure

At the conclusion of Stage 1 the repository should resemble:

```text
power-simulator/

backend/
    app/
        api/
        core/
        db/
        market/
        schemas/
        services/

    alembic/
    tests/

frontend/

modules/

docs/

scripts/

infrastructure/

.github/
```

---

# Primary Components

## FastAPI Application

Responsibilities:

* REST API
* Dependency injection
* Health monitoring
* API documentation
* Future market endpoints

---

## PostgreSQL

Responsibilities:

* Persistent storage
* Market data
* Configuration
* Generator metadata
* Transmission metadata

---

## TimescaleDB

Responsibilities:

* Time-series storage
* Historical LMP
* Dispatch history
* Forecast history
* Market intervals

---

## Redis

Responsibilities:

* Caching
* Future task queue
* Session cache
* Agent communication

---

## Alembic

Responsibilities:

* Schema versioning
* Database migrations
* Upgrade management
* Rollback support

---

## SQLAlchemy

Responsibilities:

* ORM models
* Database abstraction
* Transaction management

---

# Initial Database Model

The initial implementation introduces the LMP Price table.

Purpose:

* Validate SQLAlchemy configuration
* Validate Alembic migrations
* Validate TimescaleDB integration

Future stages will expand the schema significantly.

---

# Deliverables

The following deliverables are required before Stage 1 is considered complete.

## Infrastructure

* Docker Compose configuration
* Backend Dockerfile
* Environment configuration

## Backend

* FastAPI application
* Health endpoint
* OpenAPI documentation

## Database

* PostgreSQL operational
* TimescaleDB enabled
* Redis operational
* SQLAlchemy configured
* Alembic operational

## Development

* uv project
* Dependency management
* Standard project layout

## Testing

* Unit tests
* GitHub Actions pipeline

---

# Validation Criteria

The following must succeed.

## Infrastructure

* Docker Compose starts successfully.
* PostgreSQL accepts connections.
* Redis accepts connections.

## Backend

* FastAPI starts successfully.
* Swagger UI loads.
* Health endpoint returns HTTP 200.

## Database

* Alembic migration completes successfully.
* LMP table exists.
* Timescale hypertable created successfully.

## Testing

* Unit tests pass.
* GitHub Actions completes successfully.

---

# Success Criteria

Stage 1 is complete when all of the following are true:

* Backend application starts without errors.
* PostgreSQL is operational.
* TimescaleDB extension is installed.
* Redis is operational.
* Docker Compose launches the infrastructure.
* Database migrations execute successfully.
* Health endpoint passes automated testing.
* GitHub Actions pipeline passes on every commit.

---

# Risks

## Environment Differences

Development environments may differ between Windows, WSL2, and GitHub Actions.

Mitigation:

* Use Docker Compose.
* Use uv for dependency management.
* Keep environment variables in a dedicated configuration.

---

## Database Migration Errors

Schema changes may become inconsistent.

Mitigation:

* Use Alembic for every schema modification.
* Never modify production tables manually.

---

## Dependency Management

Python packages may drift between developers.

Mitigation:

* Manage all dependencies using uv.
* Commit the lock file to source control.

---

## CI Failures

Infrastructure-dependent scripts can fail in CI environments.

Mitigation:

* Restrict automated tests to unit tests.
* Keep Redis and PostgreSQL validation scripts outside the pytest test suite.
* Execute infrastructure validation separately from GitHub Actions unit tests.

---

# Dependencies

This stage depends on:

* Stage 0A – AI Engineering Platform
* Stage 0B – Lightweight Agent Bus

---

# Outputs

The outputs of this stage become the foundation for:

* Stage 2 – Network Modeling
* Stage 3 – Market Clearing
* Stage 4 – SCED and DCOPF
* Stage 5 – SCUC
* Stage 6 – Settlement Engine
* Stage 10 – Analytics Platform
* Stage 12 – AI Market Copilot

---

# Related Documents

* 00-master-roadmap.md
* 01-stage-0-foundation-ai-platform.md
* 02-stage-0b-agent-bus.md
* 04-stage-2-network-modeling.md

Development implementation details are documented separately in:

* docs/development/stage-1-infrastructure-guide.md

Architecture decisions related to this stage should be recorded in:

* docs/decisions/ADR-001-fastapi.md
* docs/decisions/ADR-002-postgresql.md
* docs/decisions/ADR-003-timescaledb.md
* docs/decisions/ADR-004-redis.md
* docs/decisions/ADR-005-sqlalchemy.md
* docs/decisions/ADR-006-alembic.md

---

# Exit Criteria

The project may proceed to Stage 2 only after:

* All Stage 1 deliverables are complete.
* All validation criteria are satisfied.
* The GitHub Actions pipeline is consistently passing.
* The infrastructure supports local development using Docker Compose.
* The backend provides a stable foundation for implementing network models and market simulation logic.
