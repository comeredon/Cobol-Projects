---
name: modernize-program
description: "Discover and challenge one COBOL-to-Java plan, stop for approval, then author and review tests before implementation and independent parity verification."
argument-hint: "Program path and migration goal"
agent: modernization-lead
---
Use the modernization workflow in `AGENTS.md`. Keep legacy assets unchanged.
Discover actual behavior, propose a bounded Java slice, and stop for my explicit
approval of its contract, stack, scenarios and commands before any implementation.
Use `migration-rubber-duck` to challenge the plan before approval and authored
tests before production implementation. Author synthetic fixtures and tests first.
Include an approved synthetic application demonstration after Java tests and
show its actual output, exit code and generated files in the handoff.
Do not infer parity from Java tests without trusted z/OS comparison evidence.
