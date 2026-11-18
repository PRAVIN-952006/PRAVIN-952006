from __future__ import annotations

import argparse
import json
from pathlib import Path

from .scanner import scan_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check GitHub Actions workflows for common security risks.")
    parser.add_argument("path", type=Path, help="Workflow YAML file or directory")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    findings = scan_path(args.path)

    if args.format == "json":
        print(json.dumps([finding.as_dict() for finding in findings], indent=2))
    else:
        for finding in findings:
            print(f"{finding.path}:{finding.line}: {finding.severity}: {finding.rule}: {finding.message}")
        print(f"{len(findings)} finding(s)")
    return 1 if findings else 0
