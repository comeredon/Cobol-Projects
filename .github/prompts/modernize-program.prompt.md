---
name: modernize-program
description: "Discover and plan one COBOL-to-Java slice, stop for approval, then route implementation and independent parity verification."
argument-hint: "Program path and migration goal"
agent: modernization-lead
---
Use the modernization workflow in `AGENTS.md`. Keep legacy assets unchanged.
Discover actual behavior, propose a bounded Java slice, and stop for my explicit
approval of its contract, stack, scenarios and commands before any implementation.
Do not infer parity from Java tests without trusted z/OS comparison evidence.
