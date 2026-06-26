# Stage 0B — Lightweight Agent Bus

**Project:** Electricity Market Simulator POC v4.1

**Stage:** 0B

**Duration:** Week 2

**Status:** Planned

---

# Purpose

The objective of Stage 0B is to establish a lightweight AI agent platform that supports human-in-the-loop software development while avoiding the complexity of fully autonomous multi-agent frameworks.

Rather than adopting large orchestration frameworks such as LangGraph, CrewAI, or AutoGen, this stage introduces a small, modular, Python-based agent bus that provides the core capabilities required for future expansion.

The resulting platform serves as the orchestration layer for AI-assisted engineering throughout the remainder of the project.

---

# Objectives

The Stage 0B implementation will provide:

* Agent registration
* Prompt library
* Task submission
* Task routing
* Persistent agent memory
* Task history
* REST APIs
* Redis integration
* SQLite persistence

The implementation is intentionally simple while remaining extensible enough to support future commercial development.

---

# Design Principles

The platform follows several guiding principles.

## Simplicity

The system should remain understandable by a single developer.

No unnecessary abstraction should be introduced.

---

## Modularity

Each subsystem should have a clearly defined responsibility.

* Registry
* Tasks
* Memory
* Prompts

can later become independent services if necessary.

---

## Human-in-the-Loop

AI agents assist development.

Humans remain responsible for:

* architecture decisions
* code approval
* deployment
* production releases

---

## Extensibility

Future migration should be straightforward.

Possible future enhancements include:

* PostgreSQL
* Qdrant memory
* event streaming
* distributed task execution
* Kubernetes deployment

---

# Scope

This stage does **not** attempt to build autonomous AI agents.

Instead, it provides infrastructure that later AI components can use.

Included functionality:

* Agent Registry
* Task Queue
* Prompt Library
* Memory Store
* REST API
* SQLite persistence
* Redis connectivity

Excluded functionality:

* autonomous planning
* recursive reasoning
* autonomous deployment
* self-modifying code
* continuous execution loops

---

# Technology Stack

## Programming Language

* Python 3.13

## API

* FastAPI

## Data Validation

* Pydantic v2

## ORM

* SQLAlchemy 2

## Database

* SQLite

## Cache / Future Queue

* Redis

## Development

* uv

---

# High-Level Architecture

```text
                User
                  │
                  │
          FastAPI REST API
                  │
        ┌─────────┼─────────┐
        │         │         │
        │         │         │
 Agent Registry  Tasks   Prompt Library
        │         │
        │         │
        └──────┬──┘
               │
          Memory Store
               │
       SQLite + Redis
```

---

# Repository Structure

```text
agent_platform/

├── registry/
│
├── tasks/
│
├── memory/
│
├── prompts/
│
├── database/
│
└── main.py
```

Each directory represents one logical module.

---

# Agent Registry

## Purpose

Maintain metadata describing available AI assistants.

Each agent contains information such as:

* name
* role
* model
* status

Examples include:

* Product Agent
* Market SME Agent
* Engineering Agent
* Review Agent

The registry acts as the directory service for all future task routing.

---

# Prompt Library

The prompt library stores reusable prompts that can be referenced by multiple agents.

Examples include:

* Code Review
* Architecture Review
* API Generation
* Unit Test Generation
* Documentation Generation
* Market Analysis

Benefits include:

* consistency
* versioning
* reuse
* easier prompt refinement

---

# Task Queue

The task queue stores work submitted to agents.

Each task records:

* target agent
* task type
* prompt
* status
* timestamps

Example lifecycle:

```text
QUEUED

↓

RUNNING

↓

COMPLETED

↓

FAILED
```

Future versions may support retries, priorities, and scheduling.

---

# Memory Store

The memory module provides persistent storage for agent-specific information.

Examples include:

* preferred coding style
* architecture decisions
* reusable snippets
* project conventions
* optimization notes

Initially memory is implemented using SQLite.

Future releases may migrate long-term knowledge into Qdrant.

---

# Redis Integration

Redis is introduced during this stage even though only a small subset of its capabilities are required.

Initially Redis serves as:

* cache
* temporary storage
* future task queue

Future stages may expand Redis usage to include:

* pub/sub messaging
* distributed workers
* background execution
* rate limiting

---

# REST API

The platform exposes a REST interface for interaction.

Initial endpoints include:

```text
POST /agents

POST /tasks

POST /memory

POST /prompts
```

Future endpoints may include:

```text
GET /tasks

GET /agents

DELETE /memory

PATCH /tasks/{id}
```

---

# Persistence Strategy

SQLite is selected because it offers:

* zero configuration
* fast startup
* simple backups
* local development

Future migration path:

```text
Stage 0B

SQLite

↓

Stage 1

PostgreSQL

↓

Commercial Platform

PostgreSQL + TimescaleDB
```

---

# Validation Criteria

The stage is considered complete when:

* Agent registration succeeds.
* Agents are stored in SQLite.
* Tasks can be submitted.
* Task status is persisted.
* Memory records can be stored.
* Prompt templates can be created.
* Redis is running.
* FastAPI endpoints are operational.
* Swagger documentation loads successfully.

---

# Deliverables

At the completion of Stage 0B, the repository contains:

* Agent Registry
* Prompt Library
* Task Queue
* Memory Store
* SQLite database
* Redis integration
* FastAPI application
* Swagger API documentation

---

# Risks

Potential risks include:

* overengineering the agent platform
* introducing unnecessary abstractions
* tightly coupling AI models to business logic
* allowing agent complexity to delay market simulator development

The implementation should remain lightweight until there is a demonstrated need for additional capabilities.

---

# Dependencies

Stage 0B depends on successful completion of:

* Stage 0A — AI Engineering Platform

This stage provides the development environment, local LLMs, and AI tooling required to build and test the agent platform.

---

# Exit Criteria

Stage 0B is complete when:

* all APIs are operational
* agent registration works
* prompt storage works
* memory storage works
* task submission works
* SQLite persistence is verified
* Redis connectivity is verified
* automated unit tests pass
* documentation is updated

---

# Next Stage

Successful completion of Stage 0B enables:

**Stage 1 — Infrastructure Foundation**

The project will transition from a lightweight prototype to a production-oriented platform by introducing:

* PostgreSQL
* TimescaleDB
* Alembic
* Docker Compose
* CI/CD
* production repository structure
* environment management
* automated testing infrastructure

These components establish the foundation required for the electricity market engine, optimization models, and future commercial ETRM capabilities.
