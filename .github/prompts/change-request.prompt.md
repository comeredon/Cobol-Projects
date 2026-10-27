---
name: change-request
description: "Plan and deliver an approved COBOL-to-Java modernization slice, not a legacy COBOL edit."
argument-hint: "Program and modernization goal"
agent: modernization-lead
---
Handle this request as a bounded COBOL-to-Java modernization slice.

Before you start planning, make sure the request states all of the following,
and ask for anything that is missing:

- **Goal**: the behavior to add or change.
- **Scope**: legacy programs to analyze and Java boundary to implement.
- **Constraints**: return codes, messages, byte/file compatibility and target stack.
- **Acceptance criteria**: observable results (RC, DISPLAY output, records
  written) for the normal, boundary, and error cases.

Keep all legacy artifacts unchanged. Use discovery and migration planning,
then stop for my explicit approval before writing Java, tests or fixtures.
Missing trusted z/OS baselines block a parity pass.
