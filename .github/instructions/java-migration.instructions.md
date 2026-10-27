---
description: "Java implementation and test rules for approved COBOL modernization slices."
applyTo: "modernization/**/*.java,modernization/**/pom.xml,modernization/**/*.gradle,modernization/**/*.gradle.kts"
---
# Java migration rules

- Use the approved JDK and build tool. Pin dependencies/plugins; no dynamic
  versions, speculative frameworks, reflection-heavy translation or new runtime
  services without approval. No build descriptor exists until a slice is approved.
- Keep each slice self-contained under `modernization/<slice>/`, normally with
  `src/main/java` and `src/test/java`. Production, tests and record codecs have
  explicit ownership. Do not edit legacy source or shared sample data.
- Separate business logic from encoding, files, clocks and runtime exit handling.
  Make these dependencies explicit and deterministic in tests.
- Use `BigDecimal` from exact decimal text/unscaled integers for exact decimal
  arithmetic. Model PIC precision/scale, receiving-field truncation, ROUNDED,
  sign, ON SIZE ERROR and intermediate precision per the actual source/options.
  `setScale` alone does not model a COBOL receiving field.
- Numeric identifiers may need strings to preserve leading zeroes. PIC X bytes
  are not automatically Unicode characters. Use explicit approved charset and
  strict encoding/decoding error behavior; never use platform-default encoding.
- Preserve record length in bytes, FILLER, signs/overpunch, COMP/COMP-3,
  REDEFINES, OCCURS bounds, framing (FB/VB, RDW) and carriage control at the
  external boundary. Do not decode packed/binary records through text readers.
- Preserve COBOL collating order and sort stability/tie behavior where observable;
  Java string ordering is not automatically equivalent to EBCDIC.
- Map file status, EOF and RETURN-CODE to explicit adapter outcomes and approved
  process exit statuses. No broad catch-and-continue or empty output on failure.
- Tests assert exact bytes and observable behavior, not only Java objects.
  Intentional differences require human approval and separate assertions.
- No claim of COBOL execution or differential parity without actual trusted
  z/OS evidence. Java-only tests are necessary but insufficient.
