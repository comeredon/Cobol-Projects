---
description: "Approval, provenance and truthfulness rules for modernization contracts, fixtures and evidence."
applyTo: "docs/modernization/**,test-data/modernization/**"
---
# Modernization evidence

Plans identify slice ID, legacy paths and source revision/content hashes,
approved Java stack, exact commands, field mappings, scenarios, non-goals,
unknowns and intended differences. Record the human approval reference; do not
invent approval or copy a stale approval onto a changed contract.

Use synthetic records only. Name exact copybook paths and SYSLIB order, charset,
record framing, compiler/runtime options and input/output hashes in baseline
provenance. Where unknown, block the affected parity claim.
User-supplied results must be sanitized before saving them in this repository.
Never replace expected z/OS output with Java-generated output.

An evidence JSON record follows `schemas/migration-evidence.schema.json`.
Run `python3 tools/modernization/check_evidence.py <evidence.json>`.
This validates record consistency, not authenticity or equivalence. An
independent verifier and a human review the actual artifacts and commands.
Skipped/unrun cases and missing baseline evidence are `blocked`, not `pass`.
