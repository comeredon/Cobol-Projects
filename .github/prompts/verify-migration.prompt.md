---
name: verify-migration
description: "Independently verify an approved Java migration using actual build/test and z/OS differential evidence."
argument-hint: "Slice, approved contract, author identities and baseline evidence"
agent: migration-verifier
---
Use `verify-migration-parity`. Report harness, Java, semantics and parity gates
separately. Do not edit files, repair code or invent missing baseline results.
If you authored this slice or its tests, report that another verifier is required.
After Java tests pass, run the approved application demo on synthetic data and
return actual stdout/stderr, exit code and generated-file previews/references.
Do not substitute test summaries for application output.
