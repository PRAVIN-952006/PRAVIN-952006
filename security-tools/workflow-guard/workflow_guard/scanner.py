"""Dependency-free, conservative checks for GitHub Actions workflows."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import re
from typing import Iterable


_ACTION_RE = re.compile(
    r"^\s*(?:-\s*)?uses:\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([^\s#]+)"
)
_RUN_RE = re.compile(r"^\s*(?:-\s*)?run:\s*(.*)$")
_UNTRUSTED_RE = re.compile(
    r"\$\{\{\s*(?:github\.(?:event\.pull_request\.(?:title|body|head\.ref)|head_ref)|"
    r"inputs\.[^}]+)\s*\}\}"
)
_SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _workflow_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    yield from sorted(
        file
        for file in path.rglob("*")
        if file.is_file() and file.suffix in {".yml", ".yaml"}
    )


def _scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    relative = str(path)
    has_workflow_permissions = False

    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if re.match(r"^permissions\s*:", stripped):
            has_workflow_permissions = True
        if re.match(r"^permissions\s*:\s*(?:write-all|read-all)", stripped):
            findings.append(
                Finding(
                    "broad-permissions",
                    "high",
                    relative,
                    number,
                    "Workflow permissions grant broad write access; prefer read-only defaults and job-level scopes.",
                )
            )
        if re.search(r"\bpull_request_target\b", stripped):
            findings.append(
                Finding(
                    "pull-request-target",
                    "high",
                    relative,
                    number,
                    "pull_request_target runs workflow code with the target repository trust boundary; review checkout and writes carefully.",
                )
            )

        action = _ACTION_RE.match(line)
        if action and not _SHA_RE.fullmatch(action.group(2)):
            findings.append(
                Finding(
                    "unpinned-action",
                    "medium",
                    relative,
                    number,
                    f"Action {action.group(1)} uses mutable ref {action.group(2)!r}; pin third-party actions to a full commit SHA.",
                )
            )

        run = _RUN_RE.match(line)
        if run and _UNTRUSTED_RE.search(run.group(1)):
            findings.append(
                Finding(
                    "script-injection",
                    "high",
                    relative,
                    number,
                    "Untrusted event or input data is interpolated directly into a shell command; pass it through an environment variable or an action input.",
                )
            )

    if not has_workflow_permissions:
        findings.append(
            Finding(
                "missing-permissions-policy",
                "low",
                relative,
                1,
                "Workflow has no explicit permissions policy; declare least-privilege permissions at workflow or job scope.",
            )
        )
    return findings


def scan_path(path: str | Path) -> list[Finding]:
    """Scan one workflow file or a directory of YAML files."""

    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(target)
    findings: list[Finding] = []
    for file in _workflow_files(target):
        findings.extend(_scan_file(file))
    return findings
