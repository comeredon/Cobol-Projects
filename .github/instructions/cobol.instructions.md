---
name: COBOL fixed-format standards
description: "Use when reading, writing, reviewing, or editing IBM Enterprise COBOL programs or copybooks in this repository."
applyTo: "**/*.cbl,**/*.cpy,**/*.cob"
---
# IBM Enterprise COBOL: fixed format and house style

## Fixed-format columns

| Columns | Area | Rule |
| --- | --- | --- |
| 1-6 | Sequence | Leave existing content as is; keep it blank on new lines. |
| 7 | Indicator | `*` or `/` comment, `-` continuation, `D` debugging line (compiled only `WITH DEBUGGING MODE`). |
| 8-11 | Area A | Division, section and paragraph names, `FD`, level `01` and `77`. |
| 12-72 | Area B | Statements, clauses, levels `02`-`49`, `66`, `88`. |
| 73-80 | Identification | Ignored by the compiler; never put code here. |

- Nothing may pass column 72. Split long statements over several lines. For a
  long literal, let the first line run to column 72 without a closing quote.
  On the next line, put `-` in column 7 and resume the literal with a quote in
  Area B.
- Use spaces only, never tab characters.
- Leave untouched lines byte-for-byte unchanged, including trailing spaces.

## House style (match the surrounding program)

- Paragraphs are numbered: `0000-Mainline`, `1000-Begin-Job` or `1000-BOJ`,
  `2000-Process`, `3000-End-Job` or `3000-EOJ`. Helper paragraphs are numbered
  inside their parent's range (`1010-`, `1015-`, `1099-`).
- Data names use mixed case and a prefix (`WS-`, `FD-`, a file prefix such as
  `SF-`). ECBAP programs use levels 01/12/15/18 and Normal programs use 01/02;
  follow the program you are in.
- Each file has one status field via
  `COPY WSFST REPLACING ==:tag:== BY ==Name==.`. That gives `WS-Name-Status`
  with 88-levels `WS-Name-Good` ("00"), `WS-Name-EOF` ("10") and
  `WS-Name-Okay` ("00", "10").
- Use explicit scope terminators (`END-IF`, `END-READ`, `END-PERFORM`,
  `END-EVALUATE`, `END-COMPUTE`). Prefer `EVALUATE` for multi-way logic. Use
  `CONTINUE`, not `NEXT SENTENCE`. No `GO TO`, `ALTER`, or `PERFORM THRU` in
  new code.
- Check the file status after every `OPEN`, `READ`, `WRITE`, `REWRITE` and
  `CLOSE`. For a fatal error, `DISPLAY` the paragraph, file and status, then set
  `RETURN-CODE` and `GOBACK`. Existing programs use 8 for I/O failures and 9
  for "table too small".
- Before every store into a table, check the subscript or index against the
  maximum (or the `OCCURS DEPENDING ON` bound).
- Size numeric receiving fields for the largest possible value. Add
  `ON SIZE ERROR` where `COMPUTE`/`ADD` can overflow, and watch for high-order
  truncation when you move into a shorter PIC.
- Keep USAGE consistent with the copybook (DISPLAY, COMP, COMP-3). Never change
  a copybook layout without an impact analysis of every program that copies it.
- If a program has a maintenance log in its header, add an entry when you
  change its behavior.

## Before answering

- Expand COPY ... REPLACING and reason about the expanded names.
- Point to `path:line` for every statement about behavior.
