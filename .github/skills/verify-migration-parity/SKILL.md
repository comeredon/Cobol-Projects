---
name: verify-migration-parity
description: "Independently verify an approved Java slice against trusted COBOL results and record honest pass, fail or blocked evidence; use before any equivalence handoff."
---
# Verify migration parity

1. Confirm you authored neither production nor test changes. Read the user
   approval, contract, exact source revision/hashes, diff and scenario matrix.
   Reapproval is needed if the implemented contract differs.
2. Run the harness check:
   `python3 -m unittest discover -s tests/guardrails -v`.
   This checks guardrails/evidence structure, not the migration itself.
3. Review semantic mappings using `map-cobol-java-semantics`. Confirm legacy
   assets are unchanged by this slice, fixture privacy and dependency scope.
4. Run the approved Java build/tests and differential commands. Capture exact
   command, exit code, relevant output and artifacts. If a command is blocked
   by the hook allowlist, escalate for human-owned harness maintenance; do not
   wrap it in another interpreter or weaken the hook.
5. Check every case against trusted sanitized z/OS evidence and its provenance.
   Compare bytes, decimal results, ordering, messages and errors/exit status.
   Confirm normalization is approved and missing files cannot pass.
6. Report `harness`, `java`, `semantics` and `parity` independently. Any actual
   mismatch is `fail`; missing evidence/unrun checks are `blocked`. Overall
   `pass` requires all gates pass and distinct implementer/verifier identities.
7. Give an editing owner the evidence record to persist under
   `docs/modernization/<slice>/evidence.json`, following
   `schemas/migration-evidence.schema.json`. Validate it with
   `python3 tools/modernization/check_evidence.py <evidence.json>`.

The validator checks consistency, not authenticity. Local evidence is not a
published ledger, observed z/OS execution, a GitHub check, or cutover approval.
Do not fabricate verdicts, hashes, command outcomes or reviewer identities.
After two failed repairs of the same gate, stop and escalate.
