---
name: z/OS JCL conventions
description: "Use when reading, writing, or editing z/OS JCL that compiles, links, or runs the COBOL examples."
applyTo: "**/*.jcl,**/*.JCL,**/*.jcl.txt"
---
# z/OS JCL conventions

On the modernization branch, use these conventions to interpret the read-only
job contract. Do not create or modify JCL, allocate datasets or submit jobs.
Derive Java batch integration requirements from the actual job, not a template.

- JCL statements are 80-byte records. Columns 1-2 hold `//`, and a name starts
  in column 3 (maximum 8 characters). Parameters end by column 71; leave
  column 72 blank. To continue a statement, end the line after a comma, then
  start the next line with `//`, a blank in column 3, and the parameters
  somewhere in columns 4-16.
- Follow the compile-link-go pattern in
  [BDS0801.jcl](../../Mainframe/ZOS/Normal/jcl/BDS0801.jcl):
  - `EXEC IGYWCL` with `COBOL.SYSIN` for the source member, `COBOL.SYSLIB` for
    the copybooks, and `LKED.SYSLMOD` for the load module.
  - Then `// IF RC = 0 THEN` and a run step with `STEPLIB`, one DD for each
    `SELECT ... ASSIGN TO ddname`, and `SYSOUT DD SYSOUT=*`.
- Use `&SYSUID..` as the data set high-level qualifier and a placeholder job
  name. Never hard-code a real user ID, account, or production data set.
- Name test input data sets `&SYSUID..<PROGRAM>.<SCENARIO>`, for example
  `&SYSUID..TABLE1.TYPES11`. Each qualifier is 1-8 letters and digits and
  starts with a letter.
- Every `ASSIGN TO` name needs a matching DD statement. Concatenate every
  copybook library the program needs in SYSLIB and state the order, because
  some copybooks exist in more than one folder.
- Derive DCB attributes from the FD:
  - Fixed records (RECFM=FB): LRECL is the record length.
  - Variable records (`RECORDING MODE IS V`, RECFM=VB): LRECL is the longest
    record plus 4 for the record descriptor word.
  - Files written with `WRITE ... ADVANCING`: with the default ADV compiler
    option, each record starts with a carriage-control byte. Use RECFM=FBA
    and LRECL of the record length plus 1, for example 133 for a 132-byte
    print line. A `SYSOUT=*` DD needs no DCB.
- To test several scenarios, compile once and add one run step per scenario.
  Condition each run step only on the compile and link steps, for example
  `// IF (COBRUN.COBOL.RC = 0 AND COBRUN.LKED.RC = 0) THEN`, so that an
  expected nonzero RC in one scenario does not skip the next. A missing-DD
  scenario is a run step without that DD statement.
- For a new data set, code `DISP=(NEW,CATLG,DELETE)` with explicit SPACE and
  DCB. Clearly flag any step that deletes or replaces a data set.
- In generated JCL, put a `//*` comment before each step that says what it
  does. Never submit jobs; the user submits them (Zowe Explorer, ISPF).
