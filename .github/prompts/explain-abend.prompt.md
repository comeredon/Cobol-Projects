---
name: explain-abend
description: "Explain an abend, file status, or return code from a job log or SYSOUT, and trace it to the likely COBOL statements."
argument-hint: "Program plus the code or job log lines, e.g. 'TABLE1 file status 47 on TABLOAD'"
agent: cobol-mentor
---
Use the `zos-runtime-codes` skill to explain the failure in the request:

1. Say what the code means in one sentence.
2. Find the program and the statements that can produce it, with `path:line`.
3. Rank the likely causes by evidence. For each cause, name the evidence that
   would confirm or rule it out.
4. Give the next diagnostic steps: job log sections, DD statements, data
   checks.
5. Suggest a code fix only if the evidence supports one. Do not edit files.

If the program name or the job output is missing, ask for it instead of
guessing.
