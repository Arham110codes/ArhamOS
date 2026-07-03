# LLM_CONTEXT.md

# ArhamOS - AI Continuation Context

Version: 0.1
Status: Active Development
Owner: Arham Oberoi

==========================================================
1. PROJECT OVERVIEW
==========================================================

ArhamOS is NOT a chatbot.

ArhamOS is an AI Operating System whose purpose is to automate complex engineering workflows using Local AI, Browser Automation, Memory, Reports and Future Multi-Agent execution.

The end goal is to build an AI Software Engineer that assists and automates real engineering work while keeping the user in complete control of important actions.

The first workflow being developed is the LeetCode Workflow.

The philosophy is:

Complete one workflow completely before starting another.

Never build isolated agents.

==========================================================
2. LONG TERM VISION
==========================================================

ArhamOS should eventually automate:

• LeetCode
• Resume Building
• Portfolio Updates
• GitHub Maintenance
• Project Development
• Cybersecurity Labs
• CTF Solving Assistance
• Research
• Documentation
• Second Brain (Obsidian)
• Personal Knowledge Base
• Weekly Reports

Everything should reuse the same core infrastructure.

==========================================================
3. DEVELOPMENT PHILOSOPHY
==========================================================

This project follows Workflow Driven Development.

NOT

LeetCode Agent
Resume Agent
Cyber Agent

Instead

LeetCode Workflow
Resume Workflow
Cyber Workflow

Each workflow is completed end-to-end before another workflow starts.

A workflow is considered complete only after the complete automation chain works.

==========================================================
4. ARCHITECTURE (FROZEN)
==========================================================

Project Structure

arhamos/

config/
docs/
scripts/
tests/

src/
    arhamos/
        cli/
        core/
        memory/
        skills/
        tools/
        utils/
        workflows/

LLM_CONTEXT.md
pyproject.toml

This structure is frozen.

Do NOT reorganize folders unless there is a critical technical reason.

==========================================================
5. CORE ARCHITECTURE
==========================================================

CLI

↓

Workflow Engine

↓

Skills

↓

Tools

↓

Local LLM

↓

Memory

↓

Reports

Every workflow may reuse every skill.

Skills never know who called them.

==========================================================
6. CURRENT WORKFLOW
==========================================================

Active Workflow:

LeetCode

Current Pipeline

Browser

↓

Extract Problem

↓

Generate Solution

↓

(Next)

Inject Code

↓

User Reviews

↓

User Clicks Submit

↓

Read Verdict

↓

Generate Report

↓

Store Report

↓

Update Knowledge Base

==========================================================
7. USER CONTROL POLICY
==========================================================

The AI must NEVER automatically submit code.

The user always reviews.

The user always presses Submit.

The AI may

Open browser

Extract question

Generate code

Paste code

Read verdict

Generate report

Store learning

But submission remains user controlled.

==========================================================
8. LOCAL AI
==========================================================

Model

Qwen3:8B

Runtime

Ollama

No cloud inference is required for the workflow.

The project is designed to work locally.

==========================================================
9. CURRENT IMPLEMENTATION
==========================================================

Completed

✓ Python Package

✓ Professional Folder Structure

✓ Virtual Environment

✓ Git Repository

✓ Local Ollama

✓ Qwen Integration

✓ Browser Service

✓ Workflow Engine

✓ LeetCode Browser

✓ Problem Extraction

✓ Local AI Pipeline

Current Browser Library

Playwright

Current Browser Strategy

Dedicated Automation Browser Profile

Personal browsing remains separate.

==========================================================
10. CURRENT BLOCKER
==========================================================

Need to configure a dedicated persistent browser profile for automation.

Chrome profile/login strategy is being implemented.

This must be solved before code injection.

==========================================================
11. IMMEDIATE NEXT TASK
==========================================================

Implement Browser Session Manager.

Requirements

Persistent browser profile.

Detect login state.

If not logged in

Allow manual login once.

Reuse session forever.

After this

Implement automatic code injection into LeetCode editor.

==========================================================
12. FUTURE ROADMAP
==========================================================

Finish LeetCode Workflow

↓

Markdown Report Generator

↓

Obsidian Integration

↓

Knowledge Base

↓

Resume Workflow

↓

Project Builder Workflow

↓

Cyber Workflow

==========================================================
13. CODING STANDARDS
==========================================================

Use type hints.

Keep functions short.

One responsibility per class.

One feature per commit.

No duplicate logic.

No magic constants.

Prefer composition over inheritance.

Avoid premature optimization.

==========================================================
14. DEVELOPMENT RULES
==========================================================

Do NOT redesign architecture.

Do NOT change folder structure.

Do NOT replace Playwright.

Do NOT replace Ollama.

Do NOT introduce cloud dependency unless explicitly requested.

Maintain backward compatibility.

Every new feature should move the current workflow closer to full automation.

==========================================================
15. DESIGN PRINCIPLES
==========================================================

Automation over interaction.

Reusable tools.

Reusable workflows.

Minimal coupling.

Maximum modularity.

Local-first.

Privacy-first.

Human remains in control.

==========================================================
16. CURRENT PROJECT STATUS
==========================================================

Infrastructure
100%

Browser Foundation
90%

LeetCode Workflow
60%

Reporting
0%

Memory
0%

Knowledge Base
0%

Automation Engine
30%

Second Brain
0%

==========================================================
17. CONTINUATION PROTOCOL
==========================================================

When continuing this project:

1. Read this file completely.

2. Do not redesign architecture.

3. Continue from the Immediate Next Task.

4. Finish the active workflow before beginning another.

5. Never sacrifice stability for new features.

6. Ask before introducing breaking changes.

7. Preserve code quality over speed.

8. Small commits.

9. Test every feature.

10. Maintain production-quality code.

==========================================================
END OF CONTEXT
==========================================================