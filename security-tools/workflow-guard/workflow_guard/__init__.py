"""Static checks for GitHub Actions workflow files."""

from .scanner import Finding, scan_path

__all__ = ["Finding", "scan_path"]
