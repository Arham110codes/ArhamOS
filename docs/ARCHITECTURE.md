# System Architecture

---

# Purpose

This document describes the technical architecture of ArhamOS.

It explains how the platform is organized, the responsibility of every major subsystem, and the interaction between components during execution.

The canonical engineering reference remains:

ENGINEERING_SPEC.md

---

# High-Level Architecture

```
                    User
                      │
                      ▼
                    CLI
                      │
                      ▼
                 Workflows
                /         \
               ▼           ▼
          Skills         Tools
               │           │
               ▼           ▼
             LLM      Browser/API
               │           │
               └─────┬─────┘
                     ▼
               External Systems
```

---

# Repository Layout

```
ArhamOS/

README.md
ENGINEERING_SPEC.md
HANDOFF.md
LLM_CONTEXT.md

docs/

scripts/

src/
    arhamos/
        core/
        config/
        memory/
        models/
        skills/
        tools/
        utils/
        workflows/

tests/

user_data/
```

---

# Architectural Principles

The architecture follows these principles:

- Separation of concerns
- Single responsibility
- Composition over inheritance
- Reusable modules
- LLM independence
- Browser abstraction
- Workflow orchestration

---

# Core Layer

Purpose

Provides shared infrastructure used throughout the platform.

Responsibilities

- LLM abstraction
- Shared interfaces
- Global services

Future

- Provider routing
- Cost tracking
- Model benchmarking

---

# Config Layer

Purpose

Centralized configuration.

Responsibilities

- Selectors
- Constants
- Environment configuration

Current

```
selectors.py
```

Future

Additional configuration modules.

---

# Models Layer

Purpose

Contains data models shared throughout the platform.

Examples

- ExecutionResult
- SubmissionResult

Responsibilities

- Structured outputs
- Shared schemas
- Type safety

---

# Memory Layer

Status

Foundation created.

Purpose

Persistent storage of execution context.

Future

- Long-term memory
- Session memory
- Vector retrieval
- Skill history

---

# Skills Layer

Purpose

Skills define high-level capabilities.

Current

LeetCode Skill

Future

GitHub Skill

Documentation Skill

Research Skill

Terminal Skill

Email Skill

Calendar Skill

Filesystem Skill

---

# Tools Layer

Purpose

Reusable implementations.

Current

BrowserService

LeetCodePage

LeetCodeEditor

ResultReader

Responsibilities

- Browser interaction
- Parsing
- Navigation
- Execution

Tools never perform reasoning.

---

# Workflow Layer

Purpose

Coordinates complete execution.

Responsibilities

- Receive user intent
- Call skills
- Call tools
- Return structured output

Current Workflow

```
User

↓

Workflow

↓

Skill

↓

LLM

↓

Browser

↓

Execution

↓

Observation
```

---

# Browser Automation Layer

Technology

Microsoft Edge

Playwright

Chrome DevTools Protocol

Responsibilities

- Browser connection
- Navigation
- Problem extraction
- Language switching
- Monaco injection
- Execution

Current Status

Stable

Frozen

---

# LLM Layer

Responsibilities

- Prompt construction
- Solution generation
- Reasoning

Current

Java solution generation.

Future

Reflection

Self-correction

Multiple providers

Agent collaboration

---

# Current Execution Pipeline

```
User

↓

CLI

↓

Workflow

↓

Browser

↓

LeetCode

↓

Problem Extraction

↓

LLM

↓

Java Solution

↓

Language Selection

↓

Code Injection

↓

Run

↓

Execution Result
```

---

# Current State

Completed

- Browser automation
- CDP integration
- Selector registry
- Problem extraction
- Java generation
- Monaco injection
- Automatic Run

In Progress

Execution parser

Submission parser

Future

Autonomous retries

Memory

Multi-agent reasoning

---

# Engineering Rules

Every subsystem follows:

Design

↓

Implement

↓

Test

↓

Freeze

↓

Document

↓

Commit

↓

Tag

Architecture changes should be rare and supported by documented engineering decisions.