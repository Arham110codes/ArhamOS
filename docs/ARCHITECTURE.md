# ARCHITECTURE.md

# ArhamOS Architecture

Version: 0.1

Status: Frozen

---

# Purpose

This document defines the technical architecture of ArhamOS.

Its purpose is to ensure every contributor (human or AI) understands the system structure and avoids unnecessary architectural changes.

Unless a critical technical issue exists, the architecture described here must remain unchanged.

---

# High-Level Architecture

```
                        User
                          │
                          ▼
                    CLI / Interface
                          │
                          ▼
                  Workflow Engine
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
     Skills             Tools            Memory
        │                 │                 │
        ▼                 ▼                 ▼
      Local LLM      Browser/File/Git     Reports
```

---

# Layer Responsibilities

## 1. CLI

Responsible only for interacting with the user.

Must never contain business logic.

Examples:

- Display menu
- Read user input
- Trigger workflows

---

## 2. Workflow Engine

Coordinates complete workflows.

A workflow may use multiple skills and multiple tools.

Workflows own the execution sequence.

Example:

LeetCode Workflow

↓

Browser

↓

Problem Extraction

↓

LLM

↓

Code Injection

↓

Verdict

↓

Report

---

## 3. Skills

Skills perform one specialized task.

Examples:

- LeetCode Solver
- Resume Writer
- Code Explainer
- Project Planner

Skills never interact directly with the user.

Skills do not know who called them.

---

## 4. Tools

Tools provide access to external systems.

Examples:

- Browser (Playwright)
- File System
- Git
- Terminal
- Obsidian
- Future APIs

Tools contain no AI logic.

---

## 5. Core

Core contains reusable infrastructure.

Examples:

- Configuration
- LLM Client
- Prompt Loader (future)
- Logging (future)

---

## 6. Memory

Persistent project memory.

Future responsibilities:

- Learning history
- Knowledge base
- Embeddings
- Vector database

---

# Current Folder Structure

```
arhamos/

config/
docs/
scripts/
tests/

src/
└── arhamos/
    ├── cli/
    ├── core/
    ├── memory/
    ├── skills/
    ├── tools/
    ├── utils/
    ├── workflows/
    ├── __init__.py
    └── main.py

LLM_CONTEXT.md
README.md
pyproject.toml
```

This structure is frozen.

---

# Dependency Rules

Allowed

Workflow
→ Skills

Workflow
→ Tools

Skills
→ Core

Tools
→ Core

CLI
→ Workflow

Forbidden

Skill
→ CLI

Tool
→ Workflow

Workflow
→ CLI

Skill
→ Skill (unless absolutely necessary)

---

# Browser Strategy

Browser automation uses Playwright.

A dedicated automation browser profile will be maintained.

Personal browsing profiles must remain untouched.

The browser is shared across workflows.

---

# AI Strategy

Primary Runtime

- Ollama

Primary Model

- Qwen3:8B

Cloud models may be added later but must never become mandatory.

The project should continue functioning offline.

---

# User Control Policy

The system may:

- Open browsers
- Read web pages
- Generate code
- Generate reports
- Read verdicts

The system must not:

- Submit code automatically
- Perform irreversible actions without user approval

Human approval is mandatory before critical actions.

---

# Engineering Standards

- Type hints where practical.
- Single Responsibility Principle.
- Small commits.
- Modular code.
- Reusable components.
- No duplicated business logic.
- Prefer composition over inheritance.
- Minimize coupling.

---

# Frozen Decisions

The following decisions are frozen:

- Folder structure
- Workflow-first development
- Playwright as browser framework
- Ollama as local inference engine
- Local-first philosophy
- Human approval before submissions
- One workflow completed before starting another

Future contributors should extend this architecture rather than redesign it.
