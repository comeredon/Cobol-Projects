---
name: map-cobol-java-semantics
description: "Map COBOL arithmetic, state, byte records, sorting and error semantics to Java during implementation or semantic review of a migration slice."
---
# Map semantics, not syntax

For each approved rule, record legacy `path:line`, Java destination, observable
contract, implementation choice and parity case IDs.

| COBOL concern | Java mapping must account for |
| --- | --- |
| PIC 9, V, S, edited numerics | Exact precision/scale, signs, zero padding, editing and invalid data. |
| COMPUTE/MOVE/ROUNDED | Intermediate arithmetic, receiving-field size, truncation direction, rounding and ON SIZE ERROR; compiler options matter. |
| COMP, COMP-3, DISPLAY | Explicit binary/packed/zoned codecs and byte order; not naive text parsing. |
| PIC X, spaces, LOW/HIGH-VALUES | Explicit charset, byte lengths, padding and sentinel semantics. |
| REDEFINES, OCCURS DEPENDING ON | Overlapping storage, active count, reserved vs transferred length and bounds. |
| WORKING-STORAGE, INITIAL, LINKAGE | Initialization, state lifetime across calls, parameter mutation/aliasing. |
| PERFORM, fall-through, GO TO | Actual control flow, not a mechanical method per paragraph. |
| SORT/MERGE, comparisons | EBCDIC/collating sequence, duplicates and tie/order semantics. |
| READ/WRITE, EOF, FILE STATUS | Exact framing and error behavior, not exception swallowing. |
| RETURN-CODE, JCL conditions | Explicit process exit mapping and orchestration contract. |

Use exact decimals, never binary floating point for decimal parity. Avoid
changing external records just to get idiomatic Java objects. Do not "repair"
legacy quirks without a documented, human-approved behavioral difference.
If evidence is insufficient, stop the affected mapping and report the unknown.
