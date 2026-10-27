---
name: discover-legacy-contract
description: "Discover a source-linked COBOL/z/OS behavioral contract before Java modernization or when explaining a legacy migration boundary."
---
# Discover a legacy contract

1. Locate PROGRAM-ID as well as file name. Read the entire program, recursively
   resolve COPY and REPLACING, and use `copybook-impact-analysis` for duplicate
   members and dependencies. Name exact paths and JCL SYSLIB precedence;
   unresolved selection is a blocker for the affected layout.
2. Trace PERFORM, fall-through, CALL/static/dynamic targets, LINKAGE, file I/O,
   sort/merge and external dependencies. Missing called modules are unknown.
3. Use `record-layouts` to map FD/copybook bytes. Inventory SELECT/ASSIGN to DD,
   RECFM/LRECL, RDW/carriage control, encoding, signed/packed/binary data,
   REDEFINES, OCCURS and bounds. Do not equate exported text to raw z/OS bytes.
4. Extract numbered business rules with `path:line`: condition, arithmetic,
   precision/rounding/truncation, state, ordering, output and error/RC behavior.
   Record compiler options affecting arithmetic/binary representation as unknown
   until supported by a listing. Use `zos-runtime-codes` for runtime evidence.
5. Separate intended rules, observed quirks/defects, and inferences. List scenarios
   and what sanitized job output is needed to establish an execution baseline.

Return an inventory, rule table, file/field map, dependency graph, risk list
and unknowns. Read only. No edits or claims that the program executed.
