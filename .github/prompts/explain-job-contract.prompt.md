---
name: explain-job-contract
description: "Read a legacy job's DD, step, RC and dataset contracts to identify what a Java batch replacement must preserve."
argument-hint: "Program and JCL paths"
agent: legacy-analyst
---
Read the program, resolved copybooks and JCL. Map SELECT/ASSIGN names to DDs,
record formats/lengths, step dependencies/conditions, external sort utilities,
return codes, dataset lifecycle and restart assumptions using `path:line`.
Mark absent JCL and unknown compiler/site settings explicitly. Explain the
replacement boundary; do not write JCL, allocate datasets, upload or submit jobs.
