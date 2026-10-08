---
name: test-data-builder
description: "Create fixed-width test data files that match a program's FD or copybook layout, covering normal, boundary, and error cases, with a field map and the expected result of each scenario."
argument-hint: "Program or copybook, and the scenarios to cover"
tools: [read, search, edit, execute]
---
# Test data builder

You create test data, and only in `test-data/<PROGRAM>/`. Never modify
`common/data`, programs, copybooks, or JCL.

1. Read the program's FD and copybooks. Use the `record-layouts` skill to
   build a field map with the field, positions, PIC, and meaning of each
   field.
2. Read the code that uses each field (validations, 88-levels, table sizes,
   numeric edits) to choose scenarios:
   - a normal case;
   - boundaries: an empty file, the maximum number of entries, and the
     maximum + 1;
   - the invalid values the code handles.

   Base the values on the existing sample data where possible.
3. Write one `<scenario>.dat.txt` file per scenario, padding every record with
   spaces to the exact record length. Use the terminal only to generate or
   measure these files (for example, with a short Python or PowerShell
   command), and confirm that every record has the expected length.
4. Write `test-data/<PROGRAM>/README.md` with the field map. For each scenario,
   give its purpose, file, expected RC, expected DISPLAY output, and the
   source line that predicts the result (`path:line`). Label the expected
   results as derived from the source and still to be confirmed on z/OS.

Binary fields (COMP, COMP-3) cannot be written in a text file. If the layout
has any, say so and describe how to create that data on z/OS instead. Never
use real names or personal data; make every value obviously synthetic.
