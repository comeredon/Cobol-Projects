---
name: zos-runtime-codes
description: "Quick reference for z/OS COBOL file status codes, common system and user abend codes, compiler and step return codes, and how to triage a failing job. Use when explaining a job log, SYSOUT, abend, file status, condition code, or RETURN-CODE, or when choosing error handling for a COBOL program."
argument-hint: "File status, abend code, RC, or pasted job log lines"
---
# z/OS COBOL runtime codes

This is a quick reference for triage. File status meanings follow the "File
status key values and meanings" table in the
[Enterprise COBOL for z/OS Language Reference](https://www.ibm.com/docs/en/cobol-zos/6.4.0?topic=operations-common-processing-facilities).
Confirm details for your Enterprise COBOL, Language Environment, and DFSMS
levels before you state a root cause.

## Triage a failing job

1. In the job log (`JESMSGLG`, `JESYSMSG`), find the first step that failed
   and its completion code: `COND CODE`/RC, `ABEND Sxxx`, or `ABEND Uxxxx`.
2. Read the program's own `DISPLAY` lines in `SYSOUT`, then the Language
   Environment messages (`CEE...`, `IGZ...`) in `SYSOUT` or `CEEDUMP`. The
   first message usually names the cause; later ones are consequences.
3. Map the failure to the source, using the paragraph names in the program's
   DISPLAYs, or the statement numbers and offsets from the LE traceback
   against the compile listing.
4. Rank the likely causes by evidence. Give each one a `path:line` and a next
   diagnostic step. Label anything you cannot see as "not in the evidence
   supplied".

Without a FILE STATUS clause or an error declarative, many I/O errors end the
program with an LE message and an abend instead of setting a status. That is
why every SELECT in this repository has a FILE STATUS clause.

Each I/O statement overwrites the file status. If the program does not check
an OPEN, the next READ or WRITE replaces the OPEN status with 47 or 48. That
proves only that the file was not open; the job log and the DD statements
show why.

## File status

| Status | Meaning | Usual batch cause |
| --- | --- | --- |
| 00 | Successful | |
| 02 | Successful, duplicate alternate key (VSAM) | Expected with `WITH DUPLICATES` |
| 04 | Successful, but the record length does not match the FD | LRECL differs from the FD record |
| 05 | OPEN successful, OPTIONAL file not present | |
| 10 | End of file | Normal end of a sequential read loop |
| 21 | Key sequence error | Input not sorted, or the key changed before REWRITE |
| 22 | Duplicate key | WRITE of an existing primary key |
| 23 | Record not found | Random READ or START with an unknown key |
| 24 | Boundary violation, indexed or relative file | Out of space, or key outside the file's range |
| 30 | Permanent I/O error | Hardware or data set problem; check the job log |
| 34 | Boundary violation, sequential file | Out of space (see SB37/SD37/SE37) |
| 35 | OPEN INPUT, I-O, or EXTEND of a nonoptional file that is not available | Missing or misspelled DD statement |
| 37 | OPEN mode not allowed | For example, OPEN I-O on a data set that cannot be updated |
| 38 | OPEN of a file previously closed WITH LOCK | Logic error |
| 39 | OPEN failed, attribute conflict | Organization, key, record size, fixed or variable records, or blocking differs from the program |
| 41 | OPEN of a file that is already open | Logic error |
| 42 | CLOSE of a file that is not open | Logic error |
| 43 | REWRITE or DELETE without a prior successful READ | Sequential-access logic error |
| 44 | Invalid record length on WRITE or REWRITE | Variable record outside its minimum or maximum |
| 46 | READ after end of file or after a failed READ | Loop condition not tested |
| 47 | READ on a file not open for INPUT or I-O | Often an unchecked OPEN that failed |
| 48 | WRITE on a file not open for OUTPUT, I-O, or EXTEND | Often an unchecked OPEN that failed |
| 49 | DELETE or REWRITE on a file not open for I-O | |
| 9x | Implementor-defined | 90 for QSAM: see the DFSMS message in the job log. 92 logic error. 93 resource not available (not QSAM). 96 no DD statement for an OPEN OUTPUT, or for an OPEN I-O or EXTEND of an OPTIONAL file (for QSAM, only with the CBLQDA(OFF) runtime option). 97 VSAM OPEN successful, file integrity verified. |

## Common abend codes

| Code | Meaning | Typical COBOL cause |
| --- | --- | --- |
| S0C1 | Operation exception | Branch to a bad address: a CALLed module not linked correctly, or code overwritten |
| S0C4 | Protection exception | Subscript or index out of range, a write past the end of a table, or a LINKAGE item with no matching CALL parameter |
| S0C7 | Data exception | Invalid packed or zoned data in arithmetic or a numeric compare: spaces or low-values in `PIC 9`/`COMP-3`, uninitialized fields, a misaligned record layout |
| S0CB | Decimal divide exception | Division by zero (packed decimal) |
| S001 | I/O error | Wrong-length record, or a read past end of file |
| S013 | OPEN error | DCB conflict, or PDS member not found |
| S806 | Module not found | STEPLIB or JOBLIB missing, or wrong program or member name |
| S222 | Job or step cancelled | Operator or user cancel |
| S322 | CPU time exceeded | Loop, or TIME too low |
| SB37, SD37, SE37 | Out of space | No space to extend; no secondary allocation; extent or volume limit reached |
| U4038 | Language Environment severe condition | The first CEE or IGZ message in SYSOUT/CEEDUMP gives the real cause |
| Other Unnnn | User abend from the program or a utility | Find the CALL or utility that issues it |

## Return codes

- The compiler (IGYCRCTL) sets the step RC from its most severe message:
  I = 0, W = 4, E = 8, S = 12, U = 16. The JCL in this repository runs the
  program only when the compile and link RC is 0 (`// IF RC = 0 THEN`), so
  even an RC 4 warning skips the run step.
- A program sets the step RC with `MOVE n TO RETURN-CODE` before `GOBACK` or
  `STOP RUN`. In this repository, 8 means an I/O failure and 9 means a table
  was too small for its input (see the WARNINGS block in the program header).
- An abended step has no RC. Later steps run only when their `COND` or
  `IF` logic allows it (for example, `// IF ABEND` or `COND=EVEN`).
