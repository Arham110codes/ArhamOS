# Changelog

All notable changes to ArhamOS are documented in this file.

The project follows a milestone-driven development process where each tagged version represents a stable engineering checkpoint.

---

# v0.3.0-alpha

Status

Current Development Version

---

## Added

### Architecture

- Modular project architecture
- Core / Skills / Tools / Workflows separation
- Canonical engineering specification
- Centralized selector registry

### Browser Automation

- Microsoft Edge CDP attachment
- Persistent authenticated browser sessions
- BrowserService implementation
- Stable browser lifecycle

### LeetCode Automation

- Automatic problem navigation
- Problem extraction
- Monaco editor detection
- Automatic Java language switching
- Automatic code injection
- Automatic Run execution

### AI

- LLM abstraction layer
- Java solution generation
- Prompt pipeline

### Documentation

- Engineering Specification
- Handoff document
- Architecture documentation
- Project documentation
- Engineering decisions
- Project state tracking

---

## Changed

- Browser automation migrated from Playwright-managed browser instances to CDP attachment.
- DOM selectors centralized into `config/selectors.py`.
- Browser layer declared architecturally stable.

---

## Fixed

- Browser authentication failures
- Session persistence issues
- Monaco editor injection
- Automatic Java language selection
- Selector instability
- Browser lifecycle management

---

## Current Work

- ExecutionResult parser
- SubmissionResult parser
- Structured execution models

---

## Planned

- Automatic submission
- Self-correction loop
- Persistent memory
- GitHub Skill
- Documentation Skill
- Research Skill
- Multi-agent execution

---

# Versioning Strategy

Each release follows:

Design

↓

Implementation

↓

Testing

↓

Documentation

↓

Review

↓

Commit

↓

Tag

Only after all stages are complete is a version considered stable.