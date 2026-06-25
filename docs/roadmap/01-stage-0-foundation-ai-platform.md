# Stage 0 — AI Foundation Platform

## Version

1.0

## Purpose

Establish a local AI engineering environment that enables AI-assisted software development for the Electricity Market Simulator platform.

This stage creates the foundation for:

* AI-assisted coding
* AI-assisted architecture design
* AI-assisted debugging
* AI-assisted documentation
* Local LLM-based engineering workflows
* Agent-based development structure (lightweight, non-autonomous)

---

# 1. Objectives

## Primary Objective

Build a fully local AI development environment capable of supporting a single developer building a complex energy market simulation system.

## Secondary Objectives

* Enable offline-first AI development workflow
* Support multiple specialized local LLM roles
* Provide retrieval-augmented knowledge base (RAG)
* Enable structured AI-assisted engineering workflow
* Establish early agent abstraction model (non-autonomous)

---

# 2. System Capabilities (End State)

At the end of Stage 0, the system must support:

## AI Capabilities

* Code generation (backend/frontend/optimization)
* Code refactoring
* Architecture design assistance
* Documentation generation
* Test generation
* Debugging assistance

## Local Models

* Engineering Model: Qwen3-Coder 8B
* Architecture Model: Qwen3 8B
* Optimization Model: DeepSeek-R1-Distill-Qwen-7B

## Tooling

* Ollama (local LLM runtime)
* Open WebUI (chat interface)
* Continue (VS Code AI assistant)
* Aider (CLI coding agent)
* Qdrant (vector database)

## MCP Tools

* Context7 MCP (documentation retrieval)
* Chrome DevTools MCP (frontend debugging)

---

# 3. Architecture Overview

```
User (Developer)
    ↓
VS Code / Warp / CLI Tools
    ↓
AI Layer (Continue / Aider / Open WebUI)
    ↓
Ollama Local Models
    ↓
Qwen3-Coder / Qwen3 / DeepSeek-R1
    ↓
Local System Execution (WSL2)
```

---

# 4. Component Responsibilities

## 4.1 Ollama

* Hosts local LLM models
* Provides inference API
* Acts as central model runtime

## 4.2 Continue (VS Code)

* Inline code generation
* Code explanation
* Refactoring suggestions
* Multi-model switching

## 4.3 Aider

* Git-aware code editing assistant
* CLI-based development agent
* Diff-based code modifications

## 4.4 Open WebUI

* Chat-based AI interface
* Multi-model interaction layer
* Manual prompt engineering interface

## 4.5 Qdrant

* Vector database for embeddings
* Stores:

  * Market knowledge
  * Code snippets
  * Architecture decisions
  * Documentation chunks

## 4.6 MCP Tools

### Context7 MCP

* Retrieves up-to-date library documentation
* Fast access to FastAPI, SQLAlchemy, Pyomo, React docs

### Chrome DevTools MCP

* Debug frontend applications
* Inspect runtime behavior
* Analyze API calls

---

# 5. Agent Abstraction Model (Lightweight)

Stage 0 introduces conceptual agents (not autonomous systems):

## 5.1 Engineering Agent

* Model: Qwen3-Coder 8B
* Role:

  * Backend development
  * Frontend development
  * Debugging
  * Refactoring

## 5.2 Architecture Agent

* Model: Qwen3 8B
* Role:

  * System design
  * Module decomposition
  * API design
  * Data modeling

## 5.3 Optimization Agent

* Model: DeepSeek-R1
* Role:

  * SCUC / SCED logic design
  * DCOPF formulation
  * Mathematical modeling

## 5.4 Review Agent

* Model: Qwen3-Coder 8B
* Role:

  * Code review
  * Test review
  * Security analysis
  * Documentation review

---

# 6. Knowledge Base Design

## Qdrant Collections

* market_rules
* optimization_models
* architecture_decisions
* code_snippets
* system_docs

## Data Sources

* Stage documentation
* Code repository embeddings
* Market theory notes
* IEEE power system references

---

# 7. Workflow Design

## 7.1 AI-Assisted Development Loop

```
Requirement
    ↓
Architecture Agent
    ↓
Engineering Agent
    ↓
Review Agent
    ↓
Human Approval
    ↓
Git Commit
```

---

## 7.2 Debugging Loop

```
Bug Report
    ↓
Continue / Aider
    ↓
Context Retrieval (Qdrant + MCP)
    ↓
Fix Proposal
    ↓
Human Validation
```

---

## 7.3 Documentation Loop

```
Code Change
    ↓
AI Summary Generation
    ↓
Update docs/
    ↓
Store embedding in Qdrant
```

---

# 8. Constraints

## Must

* Fully local execution
* No dependency on cloud LLM APIs
* Human-in-the-loop decision making
* Reproducible environment via Docker + WSL2

## Must NOT

* Fully autonomous agent execution
* Auto-deployment systems
* Hidden stateful AI modifications
* Cloud-only dependencies

---

# 9. Success Criteria

Stage 0 is complete when:

* Ollama runs all required models locally
* Continue integrates with VS Code
* Aider can modify repository via diff workflow
* Open WebUI can access local models
* Qdrant stores and retrieves embeddings
* MCP tools are functional
* Developer can complete full AI-assisted coding loop

---

# 10. Output of Stage 0

At completion, developer can:

* Generate backend FastAPI modules using AI
* Design market simulation architecture with AI support
* Debug code using AI assistance
* Maintain structured documentation
* Build foundation for Stage 1 infrastructure layer

---

# 11. Transition to Stage 1

Stage 1 depends on Stage 0 completion.

Stage 1 introduces:

* PostgreSQL + TimescaleDB
* Alembic migrations
* Production backend structure
* CI/CD pipeline
* Persistent market data layer

---

# End of Document
