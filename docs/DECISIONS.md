# Engineering Decisions

This document records significant architectural decisions made during the development of ArhamOS.

Its purpose is to explain **why** decisions were made, preventing future contributors from unintentionally reversing deliberate engineering choices.

---

# Decision 001

## Modular Architecture

### Status

Accepted

### Decision

Separate the platform into independent modules.

```
Core
Config
Models
Memory
Skills
Tools
Utilities
Workflows
```

### Rationale

- Better maintainability
- Independent testing
- Easier extension
- Lower coupling

---

# Decision 002

## Browser Automation via CDP

### Status

Accepted

### Decision

Use Microsoft Edge with Chrome DevTools Protocol instead of launching Playwright-managed browsers.

### Rationale

Benefits

- Persistent login sessions
- Reduced authentication issues
- Browser reuse
- Stable debugging
- Better real-world behaviour

Rejected Alternative

- Fresh Playwright browser instances

Reason

Authentication failures and browser detection.

---

# Decision 003

## Manual Authentication

### Status

Accepted

### Decision

Never automate login.

Users authenticate manually once.

ArhamOS attaches to the existing authenticated browser.

### Rationale

- Simpler implementation
- More reliable
- Avoids login failures
- Reduces maintenance

---

# Decision 004

## Skills / Tools Separation

### Status

Accepted

### Decision

High-level reasoning belongs to Skills.

Execution belongs to Tools.

### Example

```
Skill

↓

Browser Tool

↓

Editor Tool

↓

Result Tool
```

### Rationale

Skills remain reusable.

Tools remain deterministic.

---

# Decision 005

## Workflow Orchestration

### Status

Accepted

### Decision

Workflows coordinate complete execution.

Skills should never directly coordinate browser operations.

### Rationale

Improves modularity.

Allows multiple workflows to reuse the same skill.

---

# Decision 006

## LLM Abstraction

### Status

Accepted

### Decision

All language model providers are accessed through a common interface.

### Benefits

- Provider independence
- Easier experimentation
- Future routing
- Better testing

---

# Decision 007

## Selector Registry

### Status

Accepted

### Decision

Store DOM selectors inside:

```
config/selectors.py
```

### Rationale

LeetCode changes frequently.

Updating one file is preferable to modifying selectors throughout the project.

---

# Decision 008

## Browser Layer Freeze

### Status

Accepted

### Decision

After stable browser automation is achieved, browser architecture should remain stable.

Future work should focus on reasoning rather than browser engineering.

### Rationale

Avoid unnecessary regressions.

---

# Decision 009

## Documentation First Releases

### Status

Accepted

### Decision

A release is not complete until:

- Documentation updated
- State updated
- Commit created
- Tag created

### Rationale

Documentation is considered part of the software rather than an afterthought.

---

# Decision 010

## Canonical Engineering Specification

### Status

Accepted

### Decision

ENGINEERING_SPEC.md is the single source of truth.

All other documents derive from it.

### Hierarchy

```
ENGINEERING_SPEC.md

↓

README

↓

HANDOFF

↓

PROJECT

↓

ARCHITECTURE

↓

STATE

↓

DECISIONS

↓

CHANGELOG

↓

LLM_CONTEXT
```

### Rationale

Maintains consistency.

Prevents contradictory documentation.

---

# Future ADRs

As ArhamOS grows, this document may be split into individual Architecture Decision Records (ADRs).

Example

```
docs/adr/

0001-modular-architecture.md

0002-cdp-browser.md

0003-selector-registry.md
```