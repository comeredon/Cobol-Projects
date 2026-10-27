# COBOL-to-Java modernization

This repository contains learning examples for IBM Enterprise COBOL on z/OS.
The implementation is kept under [Mainframe/ZOS](Mainframe/ZOS); alternative
platform implementations and unrelated utilities have been removed.
These are independent batch programs and workshops, not one application with a
single entry point. On `modernization/cobol-to-java`, they are a **read-only
behavioral baseline** for incremental Java modernization. No program has been
translated and no Java stack or z/OS parity baseline is selected by this setup.

## GitHub Copilot for modernization

Start with the [agent contract](AGENTS.md) and
[modernization guide](docs/modernization/README.md). The harness adapts the
orchestration, narrow specialist roles, independent verification and evidence
pattern of `comeredon/copilot-agentic-delivery-center` to COBOL-to-Java migration.
The `release` branch retains the everyday COBOL-development profile; this branch
replaces that profile rather than mixing two competing agent teams.

The Copilot setup lives in [.github](.github):

- `modernization-lead` coordinates a legacy analyst, migration planner, Java
  implementer, parity test engineer and independent migration verifier.
- `/modernize-program` discovers a contract and stops for human approval before
  coding. `/verify-migration` checks actual build and differential evidence.
- Skills cover discovery, slicing, semantic mapping, synthetic parity cases and
  verification, alongside the retained COBOL layout/impact/runtime skills.
- Hooks protect legacy assets and harness controls and allow only bounded
  commands. Harness tests run locally and in the included GitHub workflow.
- Evidence records distinguish Java checks from observed z/OS parity. Missing
  baselines block equivalence claims; the harness does not authorize cutover.

Workspace settings in [.vscode](.vscode) set Rocket to the Enterprise COBOL
for z/OS dialect for reading the baseline and recommend the Java extension pack.
Select the target Java toolchain during slice approval; no framework is
prescribed in advance.

## Repository layout

| Location | Purpose |
| :------- | :------ |
| [Normal](Mainframe/ZOS/Normal) | COBOL examples and their available compile/run JCL. |
| [ECBAP](Mainframe/ZOS/ECBAP) | Enterprise COBOL for Business Application Programming workshops, copybooks, documentation, and an upload script. |
| [Internal-Sort](Mainframe/ZOS/Internal-Sort) | Internal sort examples, copybooks, and sample JCL. |
| [Zowe](Mainframe/ZOS/Zowe) | Data-set initialization, allocation, VSAM, and report examples using Zowe CLI. |
| [Shared copybooks](common/cpy) | Record layouts and helpers used by the z/OS examples. |
| [Sample data](common/data) | Tutorial inputs and sample outputs, including [ECBAP data](common/data/ECBAP). |
| [Modernization guide](docs/modernization) | Active migration workflow, guardrail limits and evidence rules. |
| `modernization/<slice>/` | Future approved Java production code and tests; no application scaffold yet. |
| `test-data/modernization/<slice>/` | Future synthetic migration fixtures, separate from legacy samples. |
| [Supporting documentation](docs) | Historical COBOL-development demo guides and the hospital-edit calculation workbook. |
| [IBM batch template](pgm_templates/Batch/slt_base_ibm_batch.cob) | Starting point for an IBM COBOL batch program. |

Keep the shared files alongside the z/OS tree. For example,
[WS162E](Mainframe/ZOS/ECBAP/cbl/WS162E.cbl) uses
[PATIENT](common/cpy/PATIENT.cpy), which is not duplicated in its local copybook
directory.

## Building and running on z/OS

You need access to a z/OS system with IBM Enterprise COBOL, a compiler/link-edit
procedure such as `IGYWCL`, and permission to allocate data sets and submit jobs.
The optional shell scripts also require a POSIX-compatible shell, Zowe CLI, and
a configured connection to your own z/OS system.

1. Choose an example and its JCL from [Normal](Mainframe/ZOS/Normal) or
   [Internal-Sort](Mainframe/ZOS/Internal-Sort).
2. Allocate source, copybook, load, and input data sets as required by that job.
   Upload the COBOL source and its local copybooks, adding any required
   [shared copybooks](common/cpy) to the compiler's `SYSLIB`.
3. Upload the matching [sample data](common/data). Match the program's record
   layout and the data set's record format/length; use appropriate text
   conversion for text inputs and binary transfer for packed/binary data.
4. Adapt the job card, high-level qualifiers, compiler procedure, and DD
   statements to your installation. The supplied user IDs are examples.
5. Submit the JCL and inspect the compiler, link-edit, and execution output.

For a small starting example, [BDS0702](Mainframe/ZOS/Normal/cbl/BDS0702.cbl)
reads employee records. Its [JCL](Mainframe/ZOS/Normal/jcl/BDS0702.jcl) uses
`<userid>.CBL(BDS0702)`, `<userid>.LOAD(BDS0702)`, and
`<userid>.CH7.EMPLOYEE`. The input
[c07-employee.dat.txt](common/data/c07-employee.dat.txt) corresponds to its
43-character employee record layout.

### Existing setup limitations

These learning materials are not a fully automated deployment. Not every source
has accompanying JCL, and some scripts retain assumptions from the original
training environment:

- The ECBAP [upload script](Mainframe/ZOS/ECBAP/scripts/upload_data.sh) refers to
  a local JCL directory and `DDS0001.LEARN.*` data exports that are not included.
  It also creates the copybook library without uploading copybooks. Supply the
  course-specific assets or adapt the script to the checked-in sources,
  copybooks, and data before using it.
- The Zowe [Simple_Report script](Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/run-project.sh)
  uploads to project-specific libraries, while its
  [run JCL](Mainframe/ZOS/Zowe/Simple_Report/JCL/RUN.jcl) references different
  source/copybook libraries. The [report source](Mainframe/ZOS/Zowe/Simple_Report/COBOL/prtrpt1.cbl)
  also retains local file assignments rather than the JCL's DD names. Align
  these before running this example.
- The Zowe [hybrid allocation script](Mainframe/ZOS/Zowe/Create_Test_DataSet/hybrid-method/allocate.sh)
  names `psap.dat.txt`, which is not included. Select the intended input and
  matching allocation settings first.
- Scripts use relative paths. Run them from their containing directories after
  reviewing their settings. Allocation and cleanup jobs can delete existing
  data sets; use dedicated test qualifiers.

The platform cleanup preserves the z/OS sources, JCL, scripts, copybooks, and
data unchanged. Compilation and execution must be verified on your target z/OS
system; no local COBOL automated test suite is provided. Copilot agents in this
repository never compile COBOL, run z/OS jobs, or submit them; they hand you the
steps to verify on z/OS. The modernization verifier may execute approved local
Java checks, but cannot claim they establish z/OS parity on their own.

## Documentation

- [Tutorial sources and naming conventions](README2.md)
- [z/OS example inventory](README3.md)
- [ECBAP course assignment history](README4.md)
- [Internal sort notes](Mainframe/ZOS/Internal-Sort/README.md)
- [COBOL-to-Java modernization guide](docs/modernization/README.md)
- [Historical COBOL-development demo guide](docs/COPILOT-FOR-COBOL.md)
- [Historical COBOL-development setup summary](docs/COPILOT-FOR-COBOL-SUMMARY.md)
