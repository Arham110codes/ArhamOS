# CHANGELOG.md

All notable changes to ArhamOS are documented here.

---

# Version 0.1.0-prealpha

Status: In Development

---

## Project Initialization

- Initialized Git repository.
- Configured Python virtual environment.
- Created professional project structure.
- Added pyproject.toml.
- Configured environment variables.

---

## Local AI

- Installed Ollama.
- Downloaded Qwen3:8B.
- Implemented local LLM client.
- Verified local inference pipeline.

---

## CLI

- Implemented interactive CLI.
- Added menu system.
- Connected CLI to workflow engine.

---

## Workflow Engine

- Introduced Workflow base class.
- Standardized workflow lifecycle.

---

## LeetCode

- Implemented LeetCodeSkill.
- Implemented LeetCodeWorkflow.
- Added BrowserService.
- Added LeetCodeBrowser.
- Implemented automatic problem extraction.
- Connected extracted problem to local LLM.

---

## Browser Automation

- Integrated Playwright.
- Created reusable browser abstraction.
- Began persistent browser session support.

---

## Documentation

- Added PROJECT.md
- Added ARCHITECTURE.md
- Added STATE.md
- Added CHANGELOG.md
- Added LLM_CONTEXT.md

---

## Next Release Goals

- Dedicated browser profile
- Login persistence
- Automatic code injection
- Verdict extraction
- Markdown report generation
- Obsidian integration

---

## Release Philosophy

Each release must complete one workflow rather than partially implementing multiple workflows.

## LeetCode Automation

- Migrated to workflow-based architecture.
- Implemented CDP browser attachment.
- Implemented Monaco editor detection.
- Implemented automatic Java code injection.
