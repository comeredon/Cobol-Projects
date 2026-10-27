---
name: review-cobol
description: "Independent COBOL review for defects and standards, with severity-ranked findings and path:line evidence."
argument-hint: "Program or files to review, e.g. TABLE1 (defaults to changed COBOL files)"
agent: legacy-analyst
---
Review the COBOL program or files named in the request. If none are named,
review the COBOL files with uncommitted changes and focus on the changed lines.
Report severity, `path:line`, actual behavior and migration consequence, with
the most important findings first. This is read-only legacy analysis, not an
independent Java parity verdict. Do not repair the baseline.
