# GitHub Copilot for COBOL: setup summary

> **Historical record for the `release` development profile.** Statements below
> about removed modernization material and current agents describe that earlier
> setup, not this branch. See the [modernization guide](modernization/README.md)
> for the active COBOL-to-Java harness.

This is a record of the work done on 2026-10-08 to turn this repository into a
GitHub Copilot for COBOL demo. For the talk track itself, see the
[demo guide](COPILOT-FOR-COBOL.md).

The repository now demonstrates GitHub Copilot for everyday COBOL work only.
All modernization and Java material was permanently deleted at the owner's
request. The agents were not run in Copilot Chat while this was built, so do
one dry run of the demo before you present it.

What was checked automatically: every agent, prompt and skill file loads
cleanly, every agent name and link resolves, and every source line the guide
cites says what the guide claims. No COBOL, copybook, JCL or data file was
changed.

## What the repository contains

- **Demo guide:** [COPILOT-FOR-COBOL.md](COPILOT-FOR-COBOL.md) is your talk
  track. It covers:
  - ISPF habits mapped to VS Code and Rocket (COLS, TABS, line commands,
    SRCHFOR, SuperC, SUBMIT/SDSF).
  - Ten tips for the first week.
  - What Rocket can do with the extension alone versus with a Rocket COBOL
    product installed.
  - A table of seven levels of structure, from a plain question up to agents
    with an approval step.
  - A 30-minute demo script on TABLE1, WS162E and the PATIENT copybook, with
    an answer key of real defects in TABLE1.
- **Copilot setup:**
  - [copilot-instructions.md](../.github/copilot-instructions.md) applies to
    every chat. It fixes the target as IBM Enterprise COBOL in fixed format,
    asks for `path:line` evidence, and forbids claiming anything compiled or
    ran.
  - COBOL and JCL rules apply automatically when those files are edited.
  - Three skills: file status and abend codes, copybook impact analysis, and
    record layouts.
- **Agents:** `cobol-lead` hands work to `cobol-mentor`, `cobol-planner`,
  `cobol-developer`, `cobol-reviewer`, `jcl-assistant` and
  `test-data-builder`. The mentor, planner and reviewer can't edit files, and
  the lead stops for your approval before any code changes.
- **Slash commands:** `/explain-program`, `/explain-abend`, `/review-cobol`,
  `/impact-analysis`, `/change-request`, `/write-jcl`, `/test-data` and
  `/document-program`.
- **Workspace settings:** in [.vscode](../.vscode), Rocket's dialect is set to
  Enterprise COBOL for z/OS, trailing spaces are never trimmed, and the needed
  extensions are recommended.

## Independent review

A separate review agent checked the work, and each finding was verified before
acting on it.

- **Fixed:**
  - The Demo 2 "without structure" question now runs in a window with no
    folder open. Otherwise the always-on instructions would apply anyway.
  - The TABLE1 answer key gained a finding: its record counter is never set
    to zero.
  - The PATIENT impact answer now includes phone-number truncation in WS162E.
  - WSFST exists in four folders, not three.
  - The JCL rules now say how to work out record lengths for variable files
    and print files. Print files need one extra byte, which the reviewer
    missed.
- **Rejected:** the reviewer said a missing DD gives file status 96. IBM's
  Enterprise COBOL Language Reference says OPEN INPUT of a required file that
  isn't available gives **35**, so the guide keeps 35. The skill's description
  of 96 was tightened.

## Before you present

- Open the repository in **VS Code Insiders**, which is where Rocket 2.0.18 is
  installed.
- No Rocket COBOL product is installed, so local compile, debug, Go to
  Definition and Rocket's own AI context won't work. Section 1 of the guide
  has a table that makes this a talking point.
- Run Demo 6 (`/change-request`) once in advance. It is the part that depends
  most on how the model responds on the day.
- The old `.venv` folder from the removed Python tooling is still on disk and
  ignored by git. Delete it if you don't need it.
