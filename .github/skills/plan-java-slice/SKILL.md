---
name: plan-java-slice
description: "Plan an incremental Java migration from a discovered COBOL contract, defining human approval, target stack, file ownership and parity gates before coding."
---
# Plan one Java slice

1. Read the discovered contract and confirm program, source revision, goal,
   external boundary, non-goals and acceptance criteria. Do not assume the
   whole repository is one application or migrate all programs at once.
2. Propose a small batch slice and a source-rule-to-Java mapping. Separate domain
   calculations, record codecs, file adapters and process exit handling.
   Compare straight replacement vs incremental coexistence only where required.
3. Ask the human to approve JDK, Maven/Gradle, framework (including none),
   dependency policy, charset, framing, decimal rules, error/exit mapping,
   approved behavior differences and missing-dependency strategy.
4. Assign exact production, test, fixture and documentation paths. State exact
   build/test/comparison commands and prerequisites. A build command is not yet
   verified merely because it appears in the plan.
5. Define normal, boundary, invalid-input and failure cases, required z/OS
   baselines/provenance, comparison/normalization rules and pass thresholds.
   Include restart/idempotency and rollback needs; no automated cutover.
6. Present the plan and all blocking questions. Stop for explicit approval.
   Changes to the contract, stack or planned differences require reapproval.

Do not write Java, change COBOL or install dependencies during planning.
