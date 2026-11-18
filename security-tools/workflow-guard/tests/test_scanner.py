import tempfile
import unittest
from pathlib import Path

from workflow_guard.scanner import scan_path


class ScannerTests(unittest.TestCase):
    def scan(self, content: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "workflow.yml"
            path.write_text(content, encoding="utf-8")
            return scan_path(path)

    def test_detects_high_signal_workflow_risks(self):
        findings = self.scan(
            """\
name: CI
on: pull_request_target
permissions: write-all
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "${{ github.event.pull_request.title }}"
"""
        )
        self.assertEqual(
            {"pull-request-target", "broad-permissions", "unpinned-action", "script-injection"},
            {finding.rule for finding in findings},
        )

    def test_sha_and_explicit_read_permissions_are_clean(self):
        findings = self.scan(
            """\
name: CI
on: push
permissions:
  contents: read
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@0123456789abcdef0123456789abcdef01234567
"""
        )
        self.assertEqual([], findings)

    def test_missing_permissions_is_reported(self):
        findings = self.scan(
            """\
name: CI
on: push
jobs:
  check:
    runs-on: ubuntu-latest
"""
        )
        self.assertEqual({"missing-permissions-policy"}, {finding.rule for finding in findings})


if __name__ == "__main__":
    unittest.main()
