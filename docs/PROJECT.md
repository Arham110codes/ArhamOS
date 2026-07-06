# Project Specification

---

# Project Name

**ArhamOS**

---

# Project Overview

ArhamOS is a modular autonomous AI agent platform designed to execute complex engineering workflows by combining Large Language Models (LLMs), browser automation, reusable tools, modular skills, and workflow orchestration.

The project emphasizes execution rather than conversation. Every capability is implemented as an independent module that can be composed into larger autonomous workflows.

The first production-ready implementation of the platform is the LeetCode Skill, which demonstrates end-to-end autonomous interaction with a real-world software platform.

---

# Mission

Build a reusable AI platform capable of reasoning, interacting with software systems, executing multi-step workflows, observing outcomes, and continuously expanding through modular skills.

---

# Vision

Transform ArhamOS into a general-purpose autonomous engineering platform capable of assisting with software engineering, research, documentation, browser automation, development workflows, and future multi-agent collaboration.

LeetCode automation serves as the first production-ready capability and architectural proof of concept rather than the project's final objective.

---

# Objectives

## Primary

- Build reusable engineering components.
- Maintain a modular architecture.
- Support interchangeable LLM providers.
- Execute software tasks autonomously.
- Minimize coupling between subsystems.

---

## Secondary

- Support persistent memory.
- Support multiple autonomous skills.
- Enable browser automation.
- Enable future agent collaboration.
- Maintain comprehensive documentation.

---

# Scope

Current scope includes:

- Browser automation
- LeetCode interaction
- LLM integration
- Code generation
- Workflow execution

Future scope includes:

- GitHub automation
- Documentation generation
- Research assistants
- Terminal automation
- File system automation
- Calendar integration
- Email automation
- Multi-agent orchestration

---

# Core Principles

- Execution over conversation.
- Modularity over monolithic design.
- Stable architecture over rapid iteration.
- Reusable components.
- Separation of concerns.
- Documentation-first development.

---

# Platform Architecture

ArhamOS is divided into independent engineering layers.

```
CLI

↓

Workflow

↓

Skills

↓

Tools

↓

External Systems
```

Each layer owns a single responsibility.

---

# Current Capabilities

## Browser

- CDP browser attachment
- Edge session reuse
- Browser persistence

## LeetCode

- Navigation
- Problem extraction
- Language switching
- Monaco editor integration
- Code injection
- Automatic Run

## AI

- LLM abstraction
- Java solution generation

---

# Current Limitations

The following capabilities are still under development.

- Execution result parsing
- Submission parsing
- Self-correction
- Long-term memory
- Multi-agent collaboration

---

# Milestones

## Completed

- Modular architecture
- Browser automation
- Stable CDP integration
- Problem extraction
- Java generation
- Automatic execution

## Current

Execution Result Parsing

## Upcoming

- Submission parsing
- Autonomous retries
- Memory integration
- GitHub Skill
- Research Skill

---

# Success Criteria

The project will be considered successful when new autonomous capabilities can be added by implementing independent Skills without modifying the platform core.

---

# Intended Audience

ArhamOS is intended for:

- Software Engineers
- AI Engineers
- Students
- Researchers
- Open Source Contributors

---

# References

The canonical engineering reference is:

```
ENGINEERING_SPEC.md
```

Operational project status is maintained in:

```
HANDOFF.md
```