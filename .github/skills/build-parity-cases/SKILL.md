---
name: build-parity-cases
description: "Build synthetic COBOL-to-Java characterization and differential cases with exact bytes, scenario coverage and trusted reference-output provenance."
---
# Build parity cases

1. Read the approved rule/field map and actual copybooks. Use `record-layouts`
   for offsets; do not generate binary/packed records as text.
2. Create deterministic synthetic inputs under `test-data/modernization/<slice>/`.
   Include empty, normal, boundary, max+1 and invalid/error/restart cases relevant
   to the contract. Mark irrelevant cases with a source-backed reason.
3. Maintain case ID, rule IDs, input/hash, expected records/bytes/order/messages/
   exit behavior, origin of expectation and Java test name.
4. Mark source-derived expectations `inferred`. Golden results require sanitized
   human-supplied z/OS output with program/source and input hashes, job/step
   reference, compiler/runtime options, charset and framing. Missing provenance
   blocks differential parity, not necessarily Java characterization.
5. Compare complete outputs. Normalization (for example a run timestamp) must
   be narrowly defined and approved; never trim whitespace, sort records or
   ignore signs/RCs merely to make outputs match.
6. Missing golden files, unexecuted cases and skipped comparisons must not
   silently succeed. Report blocked cases and mismatches separately.

Never use Java output to overwrite reference outputs. Never use real patient,
customer, account, credential or production records, even as "sample" fixtures.
