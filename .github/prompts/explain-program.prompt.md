---
name: explain-program
description: "Explain a COBOL program for a developer new to it: purpose, files, a PERFORM flow diagram, key data, return codes, and watch-outs."
argument-hint: "Program name or path, e.g. TABLE1"
agent: legacy-analyst
---
Explain the COBOL program named in the request. If no program is named, use
the file open in the editor. Resolve its copybooks and JCL, and answer in your
legacy contract format using `discover-legacy-contract`. Highlight Java migration
boundaries and unknowns. Read only; do not change the baseline.
