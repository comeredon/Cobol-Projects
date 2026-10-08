---
name: test-data
description: "Generate fixed-width test data for a COBOL program's input files, with a field map and the expected result of each scenario."
argument-hint: "Program and scenarios, e.g. 'TABLE1: 5, 10, and 11 insurance types'"
agent: test-data-builder
---
Create test data for the program and scenarios in the request. If no scenarios
are given, propose a normal case, the boundaries, and the error cases the code
handles, then create them.
