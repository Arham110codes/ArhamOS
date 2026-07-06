# ENGINEERING_SPEC.md

---

# Document Metadata

| Field | Value |
|-------|-------|
| Project | ArhamOS |
| Version | v0.3.0-alpha |
| Status | Active Development |
| Architecture Status | Frozen |
| Last Updated | 2026-07-06 |
| Author | Arham Oberoi |
| Primary Development Assistant | OpenAI ChatGPT |
| Repository Type | Modular AI Agent Platform |
| Language | Python 3.13 |
| Current Sprint | Execution Result Parsing |

---

# Executive Summary

ArhamOS is a modular autonomous AI agent platform designed to execute complex software engineering tasks through a combination of Large Language Models, browser automation, modular skills, reusable tools, workflows, and persistent context.

Unlike traditional AI chat interfaces, ArhamOS is built around execution rather than conversation. Every capability is implemented as a reusable engineering component, allowing the platform to reason, interact with external software, execute actions, observe results, and improve iteratively.

The first fully implemented production skill is LeetCode automation. It demonstrates the complete execution pipeline from browser attachment and problem extraction to LLM reasoning, automatic code injection, execution, and result retrieval.

The architecture is intentionally modular so future capabilities such as GitHub automation, documentation generation, research assistants, terminal execution, and other autonomous workflows can be added without modifying the core platform.

---

# Vision

The long-term vision of ArhamOS is to become a general-purpose autonomous AI engineering platform capable of understanding goals, planning execution, interacting with software systems, maintaining long-term context, and completing complex technical workflows with minimal human intervention.

Rather than optimizing for a single domain, the platform is designed around extensibility. New capabilities are introduced as Skills that combine reusable Tools, shared infrastructure, and LLM reasoning.

LeetCode automation represents the first production-ready implementation of this architecture rather than the final product.

---

# Philosophy

The architecture is guided by several engineering principles.

Execution over conversation.
The platform exists to perform work, not merely generate text.

Modularity over monolithic design.
Every subsystem should have a single responsibility.

Composition over duplication.
Skills orchestrate reusable tools rather than implementing browser logic directly.

LLM agnostic design.
Language models are interchangeable behind a common interface.

Stable architecture over rapid feature growth.
Subsystems are frozen after stabilization to minimize regressions.

Documentation first.
Every release includes documentation updates before being considered complete.

Recoverability.
Any developer or LLM should be able to resume development using repository documentation alone.

---

# Design Principles

## Separation of Responsibilities

The platform separates concerns into distinct modules.

Core
Configuration
Models
Memory
Skills
Tools
Utilities
Workflows

Each module owns a clearly defined responsibility.

---

## Skills

Skills define high-level capabilities.

Examples include:

LeetCode

Future GitHub

Future Documentation

Future Research

Future Browser Automation

---

## Tools

Tools perform concrete operations.

Examples:

Browser

Editor

Result Reader

Problem Extraction

Filesystem

Terminal

Tools never perform reasoning.

---

## Workflows

Workflows coordinate Skills and Tools into complete execution pipelines.

Example:

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

---

## Browser Automation

Browser automation is implemented using Microsoft Edge connected through the Chrome DevTools Protocol (CDP).

The platform never automates login.

Instead it attaches to an already authenticated browser session.

Advantages include:

Persistent authentication

Reduced bot detection

Session reuse

Reliable browser state

---

## Current Implemented Pipeline

User

↓

CLI

↓

Workflow

↓

Browser Connection

↓

LeetCode Navigation

↓

Problem Extraction

↓

LLM Solution Generation

↓

Automatic Java Selection

↓

Monaco Code Injection

↓

Automatic Run

↓

Execution Feedback

---

# Current Project Status

Completed

✅ Modular project architecture

✅ Browser attachment using CDP

✅ Stable Edge session reuse

✅ LeetCode integration

✅ Problem extraction

✅ LLM abstraction

✅ Java solution generation

✅ Monaco editor injection

✅ Automatic language switching

✅ Automatic Run execution

✅ Selector registry

In Progress

ExecutionResult parser

SubmissionResult parser

Planned

Automatic submission

Self-correction loop

Persistent memory integration

Multi-agent reasoning

GitHub skill

Documentation skill

Research skill

Terminal automation

---

# Engineering Rule

Every subsystem follows the lifecycle:

Design

↓

Implement

↓

Test

↓

Stabilize

↓

Freeze

↓

Document

↓

Commit

↓

Tag

No subsystem should be significantly redesigned after being frozen unless a critical architectural limitation is discovered.