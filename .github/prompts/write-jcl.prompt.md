---
name: write-jcl
description: "Create compile, link, and run JCL for a COBOL program from its SELECT/ASSIGN statements, copybooks, and record lengths, without submitting it."
argument-hint: "Program name, e.g. TABLE1"
agent: jcl-assistant
---
Write compile, link, and run JCL for the program named in the request,
following your process. Use sample data from `test-data/<PROGRAM>/` if it
exists, and otherwise from `common/data`. Do not submit the job.
