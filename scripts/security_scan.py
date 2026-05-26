import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_PARTS = {
    ".git",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
}

SENSITIVE_FILENAMES = {
    ".env",
    ".env.local",
    ".pypirc",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
}

SENSITIVE_SUFFIXES = {
    ".pem",
    ".key",
    ".p12",
    ".pfx",
}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA |)PRIVATE KEY-----"),
    "OpenAI API key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "Stripe secret key": re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{20,}\b"),
}


def tracked_files(root=ROOT):
    for path in root.rglob("*"):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.is_file():
            yield path


def is_sensitive_filename(path):
    name = path.name.lower()
    return name in SENSITIVE_FILENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES


def scan_file(path):
    findings = []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings

    for line_number, line in enumerate(content.splitlines(), start=1):
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(line):
                findings.append((label, path, line_number))

    return findings


def main():
    findings = []

    for path in tracked_files():
        if is_sensitive_filename(path):
            findings.append(("sensitive filename", path, 0))
        findings.extend(scan_file(path))

    if findings:
        print("Security scan failed:")
        for label, path, line_number in findings:
            location = path.relative_to(ROOT).as_posix()
            if line_number:
                location = f"{location}:{line_number}"
            print(f"- {label}: {location}")
        return 1

    print("Security scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
