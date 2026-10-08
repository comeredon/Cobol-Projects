---
name: copybook-impact-analysis
description: "Step-by-step procedure to find every program, record, JCL step, and data file affected by changing a COBOL copybook or one of its fields, including COPY REPLACING expansions and duplicate copybook members. Use before changing a copybook, record layout, field size or USAGE, or file status field, and for 'where is this used' or 'what breaks if' questions."
argument-hint: "Copybook or field, and the intended change"
---
# Copybook impact analysis

## 1. Locate every copy of the member

- Search all copybook folders case-insensitively: `common/cpy`,
  `Mainframe/ZOS/*/cpy`, and `Mainframe/ZOS/Zowe/**/COPYBOOK`. z/OS member
  names are uppercase, but the source may say `COPY wsfst` or `COPY "wsfst"`.
- If there is more than one copy, compare their contents (not just their names)
  and report which copy each program gets. On z/OS, the SYSLIB concatenation
  order in the compile JCL decides this. Locally, the editor's copybook path
  order decides it. If the JCL is missing, say the choice is unknown.

## 2. Find every COPY statement

- Search `**/*.cbl`, `**/*.cob`, and `**/*.cpy` for `COPY <member>`,
  case-insensitively. Include `*.cpy` because copybooks can copy other
  copybooks. Include quoted names and statements that continue onto the next
  line.
- For each hit, record the `path:line`, where it sits (FD, WORKING-STORAGE,
  LINKAGE), and its `REPLACING` value.

## 3. Expand names, then find the field usage

- Apply `REPLACING ==:tag:== BY ==X==` to get the real names. For example,
  `COPY WSFST REPLACING ==:tag:== BY ==TL==.` generates `WS-TL-Status`,
  `WS-TL-EOF`, `WS-TL-Good`, and `WS-TL-Okay`.
- Search for each expanded name that the change touches, including 88-level
  condition names and REDEFINES.
- Include implicit users that copy bytes without naming the field: group
  MOVEs, `READ ... INTO`, `WRITE ... FROM`, `INITIALIZE`, `CALL ... USING`, and
  other records that redefine the same area.

## 4. Check the physical layout

- Use the `record-layouts` skill to compute the record length before and after
  the change. A length change affects the FD, the JCL DCB `LRECL`, every
  program that reads or writes the same data set, and the sample data in
  `common/data`.
- Match data files by record length and content. For example,
  `common/data/ECBAP/hospin.dat.txt` has 89-character records, matching the
  `PATIENT` layout.

## 5. Report

1. Change summary, with the record length before and after.
2. Impact table: artifact | `path:line` | effect (compile, behavior, data, JCL) | action needed.
3. Every copy of the member, and which one each program gets.
4. Recommended order of change, and what to recompile. Every program that
   copies the member must be recompiled, even if its own source is unchanged.
5. The test data and runs needed to verify the change on z/OS.
6. Unknowns: programs, JCL, or data sets outside this repository.
