---
name: review-cobol
description: "Independent COBOL review for defects and standards, with severity-ranked findings and path:line evidence."
argument-hint: "Program or files to review, e.g. TABLE1 (defaults to changed COBOL files)"
agent: cobol-reviewer
---
Review the COBOL program or files named in the request. If none are named,
review the COBOL files with uncommitted changes and focus on the changed lines.
Use your checklist and output format, with the most important findings first.
