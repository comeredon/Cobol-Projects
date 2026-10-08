---
name: impact-analysis
description: "Find everything affected by changing a copybook, record layout, or field: programs, COPY REPLACING expansions, JCL, and sample data."
argument-hint: "Copybook or field and the change, e.g. 'PATIENT: Patient-Phone X(10) to X(12)'"
agent: cobol-planner
---
Run the `copybook-impact-analysis` skill for the change in the request, and
report in that skill's format. Plan no edits beyond the recommended order of
change, and do not edit files.
