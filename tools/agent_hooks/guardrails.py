"""Conservative repository hook; not a sandbox for arbitrary executable code."""

import json
import re
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WRITABLE = ("modernization", "test-data/modernization", "docs/modernization")
READ_TOOLS = {"read", "view", "glob", "rg", "grep", "search", "list_dir"}
EDIT_TOOLS = {"edit", "create", "write", "apply_patch", "str_replace_editor"}
SHELL_TOOLS = {"bash", "powershell", "execute", "run_in_terminal"}
OTHER_TOOLS = {"agent", "task", "ask_user", "todo", "update_todo", "todowrite"}
PATH_KEYS = {
    "path", "paths", "file", "file_path", "filepath", "filepaths",
    "filename", "target", "directory", "cwd", "working_directory",
    "old_path", "new_path", "destination", "source",
}
SECRET = re.compile(
    r"(^|/)(\.env(?:\.[^/]*)?|\.npmrc|\.git-credentials|id_(rsa|ed25519)"
    r"(?:\.[^/]*)?|secrets?\.(json|ya?ml|txt))$"
    r"|\.(pem|pfx|p12|key)$",
    re.IGNORECASE,
)


def inside(path, prefix):
    return path == prefix or path.startswith(prefix + "/")


def normalized_path(value, root, cwd):
    if not isinstance(value, str) or not value or "\x00" in value:
        raise ValueError("Invalid path.")
    portable = value.replace("\\", "/")
    if SECRET.search(portable) or any(
        part.casefold() == ".git" for part in Path(portable).parts
    ):
        raise ValueError("Credential or Git-internal path.")
    candidate = Path(portable)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    resolved = candidate.resolve()
    relative = resolved.relative_to(root.resolve()).as_posix()
    if SECRET.search(relative) or any(
        part.casefold() == ".git" for part in Path(relative).parts
    ):
        raise ValueError("Credential or Git-internal path.")
    return relative


def extract_paths(args):
    paths = []
    for key, value in args.items():
        if key.lower() in PATH_KEYS:
            if isinstance(value, list):
                paths.extend(value)
            else:
                paths.append(value)
        elif isinstance(value, dict):
            paths.extend(extract_paths(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    paths.extend(extract_paths(item))
    return paths


def patch_paths(text):
    if not isinstance(text, str) or not text.startswith("*** Begin Patch\n"):
        raise ValueError("Unsupported patch format.")
    if not text.rstrip().endswith("*** End Patch"):
        raise ValueError("Incomplete patch.")
    paths = re.findall(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)$",
                       text, re.MULTILINE)
    if not paths:
        raise ValueError("Patch has no target.")
    return paths


def shell_allowed(command, root, cwd, branch):
    if not isinstance(command, str) or not command:
        return False
    # No compound commands, expansion, redirection or interpreter wrappers.
    if re.search(r"[\n\r;&|<>`$]", command):
        return False
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False
    fixed = [
        ["git", "status", "--short"],
        ["git", "branch", "--show-current"],
        ["git", "diff", "--stat"],
        ["git", "diff", "--check"],
        ["git", "diff", "--", "modernization/", "test-data/modernization/",
         "docs/modernization/"],
        ["java", "-version"],
        ["javac", "-version"],
        ["mvn", "--version"],
    ]
    if tokens in fixed:
        return True
    if tokens == ["python3", "-m", "unittest", "discover", "-s",
                  "tests/guardrails", "-v"]:
        return cwd == root
    if (len(tokens) == 3 and tokens[:2] ==
            ["python3", "tools/modernization/check_evidence.py"] and cwd == root):
        path = normalized_path(tokens[2], root, cwd)
        return inside(path, "docs/modernization") and path.endswith(".json")
    # Maven can execute plugins: approved build files remain a human review boundary.
    if (len(tokens) == 6 and tokens[:3] == ["mvn", "-B", "-f"]
            and tokens[4:] == ["verify", "--no-transfer-progress"]
            and branch.startswith("modernization/")):
        path = normalized_path(tokens[3], root, cwd)
        return bool(re.fullmatch(r"modernization/[^/]+/pom\.xml", path))
    return False


def decide(payload, root=ROOT, branch=""):
    """Return a static reason code, never payload text or credential contents."""
    deny = lambda reason: {"permissionDecision": "deny",
                           "permissionDecisionReason": reason}
    if not isinstance(payload, dict):
        return deny("Malformed hook payload.")
    tool = payload.get("toolName", payload.get("tool_name"))
    args = payload.get("toolArgs", payload.get("tool_input"))
    if not isinstance(tool, str):
        return deny("Missing tool name.")
    tool = tool.lower()
    try:
        cwd = Path(payload.get("cwd", str(root))).resolve()
        cwd.relative_to(root.resolve())
        if isinstance(args, str) and tool != "apply_patch":
            args = json.loads(args)
        if tool == "apply_patch":
            text = args if isinstance(args, str) else (
                args.get("patch", args.get("input")) if isinstance(args, dict) else None)
            paths = patch_paths(text)
        elif not isinstance(args, dict):
            return deny("Unsupported tool arguments.")
        else:
            paths = extract_paths(args)
        normalized = [normalized_path(path, root, cwd) for path in paths]
        if tool in EDIT_TOOLS:
            if not branch.startswith("modernization/"):
                return deny("Delivery edits require a modernization branch.")
            if not normalized or any(
                not any(inside(path, prefix) for prefix in WRITABLE)
                for path in normalized
            ):
                return deny("Legacy assets and harness controls are read-only.")
        elif tool in SHELL_TOOLS:
            command = args.get("command", args.get("commandLine"))
            if not shell_allowed(command, root, cwd, branch):
                return deny("Command not allowlisted. Request human review; do not wrap or bypass.")
        elif tool not in READ_TOOLS | OTHER_TOOLS:
            return deny("Unknown tool requires human-owned hook integration.")
        return {"permissionDecision": "allow"}
    except (ValueError, TypeError, OSError, RuntimeError):
        return deny("Invalid, outside-repository, credential or symlink path.")


def main():
    if sys.argv[1:] != ["pre"]:
        print("Expected pre hook mode.", file=sys.stderr)
        return 2
    try:
        payload = json.load(sys.stdin)
        branch = subprocess.run(
            ["git", "-C", str(ROOT), "branch", "--show-current"],
            check=True, capture_output=True, text=True, timeout=2,
        ).stdout.strip()
        result = decide(payload, ROOT, branch)
    except (ValueError, OSError, subprocess.SubprocessError):
        result = {"permissionDecision": "deny",
                  "permissionDecisionReason": "Hook input or branch could not be verified."}
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
