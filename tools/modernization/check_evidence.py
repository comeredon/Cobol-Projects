"""Validate migration evidence structure and consistency without dependencies."""

import json
import re
import sys
from pathlib import Path


STATUSES = {"pass", "fail", "blocked"}
GATES = {"harness", "java", "semantics", "parity"}


def exact_keys(value, keys, label):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError(f"{label}: missing or unknown fields.")


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def status(value):
    return isinstance(value, str) and value in STATUSES


def validate(record):
    exact_keys(record, [
        "slice", "status", "approval", "proposer", "verifier", "source_revision",
        "java_revision", "gates", "commands", "cases",
    ], "evidence")
    for key in ["slice", "approval", "proposer", "verifier",
                "source_revision", "java_revision"]:
        if not nonempty(record[key]):
            raise ValueError(f"{key}: a nonempty string is required.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record["slice"]):
        raise ValueError("slice: use a lowercase kebab-case ID.")
    if record["proposer"].strip().casefold() == record["verifier"].strip().casefold():
        raise ValueError("Independent proposer and verifier are required.")
    exact_keys(record["gates"], GATES, "gates")
    if not status(record["status"]) or not all(
        status(value) for value in record["gates"].values()
    ):
        raise ValueError("Statuses must be pass, fail or blocked.")
    if not isinstance(record["commands"], list) or not isinstance(record["cases"], list):
        raise ValueError("commands and cases must be arrays.")
    commands = {gate: [] for gate in GATES - {"semantics"}}
    for command in record["commands"]:
        exact_keys(command, ["gate", "command", "exit_code", "artifact"], "command")
        gate = command["gate"]
        if not isinstance(gate, str) or gate not in commands:
            raise ValueError("Unknown command gate.")
        if not all(nonempty(command[key]) for key in ["command", "artifact"]):
            raise ValueError("Command text and artifact reference are required.")
        code = command["exit_code"]
        if code is not None and type(code) is not int:
            raise ValueError("exit_code must be an integer or null.")
        commands[gate].append(code)
    for gate, codes in commands.items():
        if record["gates"][gate] == "pass" and (
            not codes or any(code != 0 for code in codes)
        ):
            raise ValueError(f"{gate}: pass requires executed successful commands.")
    ids = set()
    for case in record["cases"]:
        exact_keys(case, ["id", "status", "rules", "baseline"], "case")
        if not nonempty(case["id"]) or case["id"] in ids:
            raise ValueError("Cases require unique nonempty IDs.")
        ids.add(case["id"])
        if not status(case["status"]):
            raise ValueError("Invalid case status.")
        rules = case["rules"]
        if (not isinstance(rules, list) or not rules
                or not all(nonempty(rule) for rule in rules)
                or len(set(rules)) != len(rules)):
            raise ValueError("Cases require unique rule references.")
        baseline = case["baseline"]
        if baseline is not None:
            exact_keys(baseline, [
                "origin", "reference", "source_revision", "input_sha256",
                "output_sha256", "compiler_options", "runtime", "charset", "framing",
            ], "baseline")
            if not all(nonempty(value) for value in baseline.values()):
                raise ValueError("Baseline provenance fields must be nonempty.")
            if baseline["origin"] != "zos-observed":
                raise ValueError("A baseline must be observed on z/OS.")
            for key in ["input_sha256", "output_sha256"]:
                if not re.fullmatch(r"[0-9a-f]{64}", baseline[key]):
                    raise ValueError("Baseline hashes must be SHA-256 hex strings.")
            if baseline["source_revision"] != record["source_revision"]:
                raise ValueError("Baseline source revision does not match.")
        if case["status"] == "pass" and baseline is None:
            raise ValueError("A passing differential case requires z/OS provenance.")
    if record["gates"]["parity"] == "pass" and (
        not record["cases"] or any(case["status"] != "pass" for case in record["cases"])
    ):
        raise ValueError("Parity pass requires nonempty, entirely passing cases.")
    if (any(case["status"] == "fail" for case in record["cases"])
            and record["gates"]["parity"] != "fail"):
        raise ValueError("A failed differential case requires a failed parity gate.")
    expected = ("fail" if "fail" in record["gates"].values() else
                "blocked" if "blocked" in record["gates"].values() else "pass")
    if record["status"] != expected:
        raise ValueError("Overall status must reflect the gate outcomes.")
    return record["status"]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tools/modernization/check_evidence.py <evidence.json>",
              file=sys.stderr)
        return 2
    try:
        record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        result = validate(record)
    except (ValueError, OSError, TypeError) as error:
        print(f"Invalid evidence: {error}", file=sys.stderr)
        return 1
    print(f"Evidence is structurally consistent; declared migration status: {result}.")
    print("This does not authenticate approval, execution, artifacts or parity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
