---
name: record-layouts
description: "Rules and a worked example for computing COBOL field lengths and byte offsets from PIC and USAGE, and for mapping fixed-width sample data to a record. Use when building or checking test data, comparing an FD with JCL LRECL, reviewing a copybook change, or locating a field in a data record."
argument-hint: "Copybook, FD, or data file"
---
# COBOL record layouts

## Field length by PIC and USAGE

| Definition | Bytes |
| --- | --- |
| `X(n)`, `A(n)` | n |
| `9(n)` DISPLAY (zoned) | n. `V` adds nothing. `S` adds nothing unless `SIGN ... SEPARATE` is coded: the sign is carried in the zone of the last digit (the default, TRAILING) or of the first digit (`SIGN IS LEADING`). |
| `S9(n) SIGN ... SEPARATE` | n + 1 |
| Numeric-edited (`ZZ9.99`, `$$$,$$9.99`, `999999.99+`) | One byte per picture character, so `CR` and `DB` count as 2 |
| `COMP-3` / `PACKED-DECIMAL`, d digits | floor(d / 2) + 1. For example, `S9(7)V99` is 5 bytes and `S99` is 2. |
| `COMP`, `BINARY`, `COMP-4`, `COMP-5`, d digits | 1-4 digits: 2 bytes; 5-9 digits: 4 bytes; 10-18 digits: 8 bytes |
| `COMP-1` / `COMP-2` | 4 / 8 |
| Level 88 | 0 |
| `FILLER` | The length of its PIC |
| Group | The sum of its subordinates, plus slack bytes only with SYNCHRONIZED |
| `REDEFINES` | No extra bytes; it reuses the bytes of the redefined item |
| `OCCURS n` | n x the entry length |
| `OCCURS m TO n DEPENDING ON` | n x the entry length is reserved; a move or write of the record uses the current count |

The first field starts at position 1. Each later field starts at the previous
field's start position plus the previous field's length.

## Worked example: `common/cpy/PATIENT.cpy` (89 bytes)

| Field (after `FD-:tag:-`) | PIC | Positions |
| --- | --- | --- |
| Patient-Num | `9(5)` | 1-5 |
| Patient-LName | `X(10)` | 6-15 |
| Patient-FName | `X(10)` | 16-25 |
| Patient-Phone | `X(10)` | 26-35 |
| Patient-Type | `X(1)` | 36 |
| Patient-Bed-Id | `9(4)` | 37-40 |
| Patient-Date-Admit | `X(10)` | 41-50 |
| Patient-Amt-PDay | `9(5)V99` | 51-57 |
| Patient-Diag-Code | `999` | 58-60 |
| Patient-Ins-Type | `X(3)` | 61-63 |
| Patient-Stay-LTH | `999` | 64-66 |
| Patient-Tot-Amt | `9(7)V99` | 67-75 |
| Patient-PCP-ID | `X(6)` | 76-81 |
| Patient-In-Out-Net | `X(1)` | 82 |
| Patient-CoPay | `S9(3)` | 83-85 |
| Patient-Deduct | `S9(4)` | 86-89 |

The first record in `common/data/ECBAP/hospin.dat.txt` is 89 characters long
and lines up with this table.

## Fixed-width sample data

- The `common/data/**/*.dat.txt` files are text versions of fixed-length
  records (RECFM=FB). The text files may have trailing spaces trimmed, but on
  z/OS every record is padded to the LRECL. Pad every record in new test data
  to the full record length.
- Implied decimals are not written. For example, the value 123.45 in a
  `9(5)V99` field is `0012345`.
- In a signed zoned field (`S9(n)` without SEPARATE), the last character
  carries the sign, or the first character with `SIGN IS LEADING`:
  - Positive: `{` = 0, `A`-`I` = 1-9 (an unsigned digit is also positive).
  - Negative: `}` = 0, `J`-`R` = 1-9.

  For example, in `S9(3)`, +123 is `12C` and -123 is `12L`. A text transfer
  converts these characters to the correct EBCDIC zones.
- `COMP`, `COMP-3`, `COMP-1`, and `COMP-2` fields are binary and cannot be
  written in a text file. Create that data on z/OS instead, for example with a
  small COBOL program or a sort utility.
- A text transfer converts ASCII to EBCDIC. A binary transfer copies bytes
  unchanged, so use it only for data that is already in EBCDIC.
