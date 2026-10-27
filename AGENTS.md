# COBOL-to-Java modernization contract

This branch is a migration harness, not an instruction to translate every file.
The source of truth is the existing IBM Enterprise COBOL/z/OS behavior, including
its observable quirks. Read `.github/copilot-instructions.md` before work.

## Ownership and authority

| Role | Scope |
| --- | --- |
| `modernization-lead` | Route bounded work, obtain human approval, collect evidence; no editing or execution. |
| `legacy-analyst` | Read COBOL, copybooks, JCL, samples and supplied logs; explain observed vs inferred contracts. |
| `migration-planner` | Read-only design, risk analysis, slice boundaries and approval criteria. |
| `java-implementer` | Implement only approved Java production code under `modernization/<slice>/`. |
| `parity-test-engineer` | Synthetic fixtures and Java tests for approved contracts; not production code. |
| `migration-verifier` | Independent read/execute verification; never edits implementation or tests. |

Use the smallest team that fits. Explanations need only an analyst. Migration
delivery needs planning, approval, implementation, tests, and an independent
verifier. At most three concurrent workers, with disjoint editing ownership.
No custom agent may enlarge its tool grants or invoke a shell to bypass its role.
If delegation is unavailable, report the limitation; do not claim independent
verification from one agent impersonating several roles.

## Required gates

1. **Discovery:** source-linked inventory and behavioral contract, explicit
   unknowns, exact copybook resolution and runtime/compiler assumptions.
2. **Approval:** human accepts a slice, non-goals, target Java stack, data
   contracts, planned differences, scenarios and commands. No code before this.
3. **Implementation:** isolated Java slice and synthetic tests; legacy unchanged.
4. **Verification:** actual build/test output, independently reviewed semantic
   mapping, and differential comparison against trusted sanitized z/OS results.
5. **Handoff:** `pass`, `fail`, or `blocked` with evidence. A parity pass is not
   authorization for deployment, replacement, job submission, or cutover.

There is no Java build or trusted z/OS baseline yet. Harness tests do not satisfy
the Java/parity gate. A human must approve operational changes separately.
Two failed repairs of the same gate exhaust the repair budget; stop and report
the failing command, hypotheses, edits, and observations.

## Protected baseline and customization

Treat everything outside `modernization/`, `test-data/modernization/`, and
`docs/modernization/` as read-only during delivery. Hooks enforce this for
recognized edit payloads. `.github/`, `AGENTS.md`, `tools/`, `tests/guardrails/`,
and Git configuration are human-owned controls, not delivery output.
User-requested harness maintenance is a separate task, reviewed by a human;
there is no environment-variable or payload switch to bypass the hook.

Never read secrets, use real customer records, publish without permission, merge,
force push, or run destructive/remote shell commands. Tool permissions, sandbox
boundaries, branch protection, required reviews/checks, and human decisions remain
authoritative: repository hooks are defense in depth, not a security sandbox.
See `docs/modernization/README.md` for limits and host smoke checks.
