# JK Archivist

**JK Archivist is a domain-aware OpenClaw-aligned skill focused on judgment, memory, and justification...not just action.**

Most agent skills can *do* things.
JK Archivist is designed to **explain why a thing should be done**, using explicit, inspectable logic that other agents (and humans) can evaluate.

This repository contains the foundational infrastructure for the Archivist.

Built in public as part of the Pump.fun / USDC agent hackathon.

---

## Why JK Archivist Exists

Agent-native systems introduce a core problem:

> When agents act autonomously, **how do we trust their decisions?**

Most agents:
- act on opaque prompts
- score things without showing work
- optimize for novelty or speed
- cannot explain *why* they chose one action over another

JK Archivist takes a different approach.

It treats **judgment itself as infrastructure**.

---

## What Makes JK Archivist Different

JK Archivist is not:
- a generic voting bot
- a prompt wrapper
- a "cool demo" agent
- a black-box LLM scorer

JK Archivist **requires** that decisions be:
- **explicit** (clear criteria, not vibes)
- **inspectable** (scores + rationale are visible)
- **repeatable** (same input → same reasoning path)
- **grounded** (context matters, not just keywords)

In short:
> If an agent can't justify its decision, it shouldn't make one.

---

## What This Skill Does

JK Archivist is designed to:

- Read agent submissions (e.g. hackathon projects)
- Evaluate them using a **defined, transparent rubric**
- Produce a **clear score breakdown**
- Generate a **justified, compliant vote or decision (with posting handled by a future transport layer)**
- Persist evaluations as memory for future reference

Every decision leaves an audit trail.

---

## Evaluation Flow

Submissions flow through scoring, then evaluation, then memory.
All logic is deterministic and inspectable.
Transport and external integrations come later.

---

## Transport Layer (OpenClaw)

JK Archivist uses OpenClaw as a transport runtime.
All judgment, memory, and justification live outside the transport layer.

---

## OpenClaw Skill

JK Archivist is exposed to OpenClaw as a tool using the official OpenClaw SDK.

All judgment, memory, and voice logic remain outside the tool wrapper.
The OpenClaw layer serves only as ingestion and execution plumbing.

---

## How JK Archivist Relates to USDC

JK Archivist does not move USDC directly.
It governs how agents evaluate projects competing for USDC.
Poor judgment leads to misallocation of USDC.
Inspectable reasoning improves trust in agent-native value distribution.

---

## Why This Matters for Agent Coordination

As systems become more agent-native:
- agents submit projects
- agents vote on each other
- agents move programmable money

The weakest link becomes **trust**.

JK Archivist demonstrates a pattern where:
- agents can disagree constructively
- reasoning can be challenged or improved
- coordination happens around shared standards, not hype

This makes agent-to-agent interaction more stable, not just faster.

---

## Relationship to JK Index

JK Archivist is **inspired by** the standards of the JK Index, but is **not coupled** to it.

This repository:
- does not access JK Index databases
- does not use JK Index secrets
- serves as a standalone reasoning prototype

The long-term goal is to explore how **explicit judgment and memory**
can complement data-driven platforms...not replace them.

---

## Why This Isn't a Throwaway Hackathon Project

Even outside the hackathon context, JK Archivist demonstrates:

- how to encode institutional reasoning
- how to make agent decisions auditable
- how to move beyond black-box automation

This makes it reusable across:
- agent governance
- moderation
- evaluation
- coordination systems

Judgment should compound...not reset every run.

---

## Status

This repository currently contains:
- OpenClaw skill scaffolding
- explicit intent and safety guarantees
- early infrastructure for evaluation + memory

Implementation is ongoing.

---

## TL;DR

JK Archivist isn't built to act faster.

It's built to **act more responsibly**
and to show its work when it does.
