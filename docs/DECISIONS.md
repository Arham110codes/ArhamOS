# DECISIONS.md

# ArhamOS Architectural Decisions

Status: ACTIVE

Purpose:
This document records all major architectural and engineering decisions made during the development of ArhamOS.

Once a decision is marked as **Frozen**, it should not be revisited unless there is a critical technical reason.

---

# Decision 001

Title

Workflow-First Development

Status

FROZEN

Decision

ArhamOS will be developed by completing one end-to-end workflow at a time rather than building isolated AI agents.

Reason

Complete workflows deliver usable functionality much earlier and ensure every component is exercised in a real-world scenario.

---

# Decision 002

Title

Local-First AI

Status

FROZEN

Decision

Primary inference will use Ollama with local language models.

Reason

Privacy, offline capability, lower operating cost, and independence from cloud APIs.

Current Model

Qwen3:8B

---

# Decision 003

Title

Workflow Completion Strategy

Status

FROZEN

Decision

A workflow must be completed before beginning another workflow.

Reason

Avoids accumulating partially implemented features and reduces technical debt.

Current Workflow

LeetCode Automation

---

# Decision 004

Title

Browser Automation Framework

Status

FROZEN

Decision

Browser automation uses Playwright.

Reason

Cross-platform support, stability, modern API, and strong automation capabilities.

---

# Decision 005

Title

Human Approval Policy

Status

FROZEN

Decision

ArhamOS must never automatically perform irreversible actions.

Examples

- Code submission
- Repository deletion
- Account changes
- Financial transactions

The user always provides the final approval.

---

# Decision 006

Title

Project Structure

Status

FROZEN

Decision

Application code exists only inside

src/arhamos

Reason

Maintainability, packaging compatibility, and scalability.

---

# Decision 007

Title

Dedicated Automation Browser

Status

FROZEN

Decision

ArhamOS uses its own browser profile for automation.

Personal browsing remains separate.

Reason

Stable automation and isolated sessions.

---

# Decision 008

Title

Reusable Browser Service

Status

FROZEN

Decision

All browser interactions must use BrowserService.

Reason

Avoid duplicated browser management logic.

---

# Decision 009

Title

Reusable Workflow Engine

Status

FROZEN

Decision

Every automation is implemented as a Workflow.

Reason

Ensures consistency, modularity, and reusability.

---

# Decision 010

Title

Skill Isolation

Status

FROZEN

Decision

Skills perform one responsibility only.

Skills never interact directly with the user.

Reason

Loose coupling and improved testability.

---

# Decision 011

Title

CLI Responsibility

Status

FROZEN

Decision

The CLI is responsible only for user interaction.

Business logic belongs inside workflows.

Reason

Separation of concerns.

---

# Decision 012

Title

Documentation Strategy

Status

FROZEN

Decision

Project knowledge is maintained using:

- LLM_CONTEXT.md
- PROJECT.md
- ARCHITECTURE.md
- STATE.md
- CHANGELOG.md
- DECISIONS.md

Reason

Allows any capable LLM to resume development with minimal context loss.

---

# Decision 013

Title

Development Philosophy

Status

FROZEN

Decision

Every commit must move the active workflow closer to completion.

Reason

Maximize visible progress and avoid unnecessary infrastructure work.

---

# Decision 014

Title

Coding Standards

Status

FROZEN

Decision

- Small commits
- Modular code
- Single Responsibility Principle
- Type hints where practical
- No duplicated logic
- Composition over inheritance
- Production-quality code

Reason

Long-term maintainability.

---

# Decision 015

Title

Architecture Stability

Status

FROZEN

Decision

Architecture should not be redesigned during feature development.

Only critical technical issues justify architectural changes.

Reason

Maintain development velocity and reduce unnecessary refactoring.

---

# Future Decisions

Every new architectural decision must be recorded here using the same format.

This file is considered the source of truth for all architectural choices made during the lifetime of ArhamOS.