---
name: impact-analysis
description: "Find copybook consumers and external contracts that a Java migration must preserve; read-only."
argument-hint: "Copybook, field or program and proposed Java boundary"
agent: migration-planner
---
Run the `copybook-impact-analysis` skill for the change in the request, and
report in that skill's format. Translate its impact findings into migration
contract risks and parity scenarios. Do not propose changes to the legacy layout
as part of Java modernization, and do not edit files.
