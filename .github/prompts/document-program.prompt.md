---
name: document-program
description: "Document a legacy program's contract for a migration slice without altering the source."
argument-hint: "Program path and migration slice ID"
agent: agent
tools: [read, search, edit]
---
Create or update `docs/modernization/<slice>/legacy-contract.md` for the COBOL
program and slice named in the request. Ask if either is missing. Read
the program, its copybooks, its JCL, and matching sample data first. Do not
change any other file.

Use exactly these sections:

1. **Overview**: purpose, PROGRAM-ID, source path, and a summary of the
   maintenance log.
2. **Files**: a table of SELECT name, DD name, organization, record layout
   (copybook or FD), record length, and sample data.
3. **Processing**: a Mermaid flowchart of the PERFORM structure, followed by a
   numbered walkthrough.
4. **Business rules**: one row per rule, with ID (`BR-01`, ...), description,
   and `path:line`.
5. **Errors and return codes**.
6. **Dependencies**: copybooks (with folder and REPLACING tag), called
   programs, and JCL.
7. **Open questions**: what the source cannot tell us.

Link to source files with relative paths. Label inferences clearly.
