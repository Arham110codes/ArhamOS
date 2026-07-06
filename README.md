# ArhamOS

> **A modular autonomous AI agent platform for intelligent software execution.**

ArhamOS is an extensible AI engineering platform designed to execute complex technical tasks by combining Large Language Models (LLMs), browser automation, reusable tools, modular skills, and workflow orchestration.

Rather than acting as a conversational chatbot, ArhamOS focuses on **execution**. The platform is built around autonomous workflows capable of interacting with real software systems, reasoning over problems, executing actions, and observing results.

The first production-ready capability implemented on the platform is **LeetCode automation**, demonstrating an end-to-end execution pipeline from browser attachment and problem extraction to code generation, automatic language selection, code injection, execution, and result retrieval.

---

# Features

## Current

- Microsoft Edge automation using Chrome DevTools Protocol (CDP)
- Persistent authenticated browser sessions
- Automatic LeetCode problem navigation
- Automatic problem extraction
- LLM-powered Java solution generation
- Automatic language switching
- Monaco editor integration
- Automatic code injection
- Automatic Run execution
- Modular Skills architecture
- Modular Tools architecture
- Workflow orchestration
- Centralized selector registry

---

# Planned

- Execution result parsing
- Submission result parsing
- Automatic submission
- Self-correction loop
- Persistent memory
- Multi-agent reasoning
- GitHub Skill
- Documentation Skill
- Research Skill
- Terminal Skill
- File System Skill

---

# Project Structure

```text
ArhamOS/
│
├── README.md
├── ENGINEERING_SPEC.md
├── HANDOFF.md
├── LLM_CONTEXT.md
│
├── docs/
│
├── scripts/
│
├── src/
│   └── arhamos/
│       ├── core/
│       ├── config/
│       ├── memory/
│       ├── models/
│       ├── skills/
│       ├── tools/
│       ├── utils/
│       └── workflows/
│
├── tests/
└── user_data/
```

---

# Technology Stack

- Python 3.13
- Playwright
- Microsoft Edge
- Chrome DevTools Protocol (CDP)
- Rich
- OpenRouter / LLM APIs

---

# Current Pipeline

```text
User
    ↓
CLI
    ↓
Workflow
    ↓
Browser Connection
    ↓
LeetCode
    ↓
Problem Extraction
    ↓
LLM
    ↓
Java Solution
    ↓
Language Switching
    ↓
Code Injection
    ↓
Run
    ↓
Execution Feedback
```

---

# Current Status

Current Version

```
v0.3.0-alpha
```

Architecture Status

```
Frozen
```

Current Sprint

```
Execution Result Parsing
```

---

# Documentation

| Document | Purpose |
|-----------|----------|
| ENGINEERING_SPEC.md | Canonical engineering specification |
| HANDOFF.md | Project recovery guide |
| LLM_CONTEXT.md | LLM continuation context |
| docs/PROJECT.md | Project vision |
| docs/ARCHITECTURE.md | Technical architecture |
| docs/STATE.md | Current implementation status |
| docs/DECISIONS.md | Engineering decisions |
| docs/CHANGELOG.md | Release history |

---

# Engineering Philosophy

- Execution over conversation
- Modular architecture
- Separation of responsibilities
- Stable interfaces
- Recoverability
- Documentation-first development

---

# License

This project is currently under active development.