---
name: change-request
description: "Run a structured COBOL change through the lead agent: plan, human approval, implementation, independent review, and optional test data and JCL."
argument-hint: "Program and change, e.g. 'TABLE1: stop with RC 9 before an 11th type is stored'"
agent: cobol-lead
---
Handle the change request below with your change request workflow.

Before you start planning, make sure the request states all of the following,
and ask for anything that is missing:

- **Goal**: the behavior to add or change.
- **Scope**: the programs and copybooks that may change, and anything that
  must not change.
- **Constraints**: style, return codes, messages, and file compatibility.
- **Acceptance criteria**: observable results (RC, DISPLAY output, records
  written) for the normal, boundary, and error cases.

Stop for my approval after the plan.
