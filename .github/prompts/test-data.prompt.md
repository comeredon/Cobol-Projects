---
name: test-data
description: "Build synthetic parity fixtures for an approved Java migration contract."
argument-hint: "Approved slice, field map and scenarios"
agent: parity-test-engineer
---
Use `build-parity-cases` for the approved slice. If the approval, field map or
scenarios are missing, ask before writing. Write only under
`test-data/modernization/<slice>/` and the assigned Java test/documentation paths.
Do not change legacy samples or claim inferred expected values are golden results.
