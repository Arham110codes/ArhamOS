# LLM Context

---

# Purpose

This document is intended exclusively for Large Language Models (LLMs) that continue the development of ArhamOS.

Unlike README.md, this document is not user-facing. It contains engineering context, architectural constraints, development philosophy, and project continuity information required to continue development without prior conversations.

The canonical source of truth is:

ENGINEERING_SPEC.md

This document is a distilled operational context optimized for AI-assisted software engineering.

---

# Project Identity

Project Name

ArhamOS

Current Version

v0.3.0-alpha

Project Status

Active Development

Architecture Status

Frozen

Current Sprint

Execution Result Parsing

Primary Language

Python 3.13

---

# Project Summary

ArhamOS is a modular autonomous AI agent platform designed to execute software engineering workflows through reusable Skills, Tools, Workflows, browser automation, and Large Language Models.

The project prioritizes execution rather than conversation.

Current production capability:

LeetCode Skill

The browser automation layer has reached feature stability and should not undergo architectural redesign unless a significant limitation is identified.

---

# Engineering Philosophy

Development follows these principles.

Execution over conversation.

Modularity over monolithic design.

Composition over duplication.

Stable interfaces.

Reusable components.

LLM provider independence.

Documentation-first releases.

Recoverability.

Avoid introducing unnecessary abstractions.

---

# Repository Overview

The project is organized into independent modules.

```
src/arhamos/

core/

config/

memory/

models/

skills/

tools/

utils/

workflows/
```

Each module owns one primary responsibility.

Avoid creating cross-dependencies between modules.

---

# Current Architecture

Execution flow:

```
User

↓

CLI

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

Browser execution:

```
Edge

↓

CDP

↓

Playwright

↓

BrowserService

↓

LeetCodePage

↓

LeetCodeEditor

↓

ResultReader
```

---

# Current Implemented Features

Infrastructure

- Modular architecture
- Configuration layer
- LLM abstraction
- Workflow orchestration

Browser

- CDP attachment
- Persistent authenticated Edge
- Stable browser lifecycle

LeetCode

- Problem extraction
- Java language switching
- Monaco injection
- Automatic Run

AI

- Prompt generation
- Java solution generation

Documentation

- Engineering Specification
- Architecture
- Decisions
- State
- Handoff

---

# Frozen Decisions

The following decisions should not be changed without explicit architectural justification.

- Modular architecture
- Skills / Tools separation
- Workflow orchestration
- Browser automation via CDP
- Persistent authenticated browser sessions
- Selector registry
- LLM abstraction
- Documentation-first development

---

# Coding Standards

Prefer readability.

Prefer composition.

Avoid unnecessary inheritance.

Avoid tightly coupled modules.

Keep Skills free from browser logic.

Keep Tools deterministic.

Avoid duplicated selectors.

Use:

config/selectors.py

for all browser selectors.

---

# Current Sprint

Execution Result Parsing

Objectives

- Parse execution status
- Parse runtime
- Parse passed test cases
- Create ExecutionResult model

After completion:

SubmissionResult parsing

Automatic submission

Reflection

Self-correction

Memory

---

# Known Limitations

Current implementation does not yet support:

- Submission parsing
- Autonomous retries
- Reflection
- Long-term memory
- Multi-agent execution

These are expected future milestones.

---

# Development Workflow

Every feature follows:

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

Documentation updates are considered mandatory before release.

---

# Continuation Instructions

When continuing development:

1.

Read:

ENGINEERING_SPEC.md

2.

Review:

HANDOFF.md

3.

Review:

docs/STATE.md

4.

Review:

docs/DECISIONS.md

5.

Continue from:

Current Sprint

Avoid redesigning stabilized architecture.

Prefer extending Skills and Tools rather than modifying existing interfaces.

Update documentation whenever architecture changes.

---

# Immediate Priorities

1.

ExecutionResult parser

2.

SubmissionResult parser

3.

Automatic submission

4.

Self-correction loop

5.

Persistent memory

---

# Long-Term Direction

The platform is intended to evolve into a modular autonomous AI engineering platform supporting multiple Skills including:

LeetCode

GitHub

Documentation

Research

Filesystem

Terminal

Browser

Email

Calendar

Future capabilities should integrate through existing architectural layers rather than bypassing them.

---

# Final Instruction

Treat ENGINEERING_SPEC.md as the canonical engineering specification.

If documentation conflicts arise, ENGINEERING_SPEC.md takes precedence.

When uncertain:

Preserve modularity.

Preserve frozen architecture.

Document architectural changes.

Avoid unnecessary redesign.