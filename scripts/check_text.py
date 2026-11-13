"""Check public documentation bytes without changing or guessing their encoding.

Only high-confidence corruption signatures are blocking. A clean result cannot
prove that an installed font contains every glyph or that a client renders it.
"""

import argparse
import json
from pathlib import Path
import re
import subprocess

SUFFIXES = {".md", ".rst", ".html", ".svg", ".txt"}
CORRUPTION = re.compile("\ufffd|Ã[\u0080-\u00bf]|â€[™œ\u009d]|锟斤拷")
CONTROLS = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
UTF8_META = re.compile(r'''<meta\b[^>]*\bcharset\s*=\s*["']?utf-8\b''', re.I)


def findings(raw, suffix):
    """Return (line, reason) findings; BOM and CRLF are legitimate UTF-8."""
    try:
        content = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return [(1, "not valid UTF-8")]
    if suffix in {".html", ".svg"}:
        # Bundled vendor scripts can intentionally contain U+FFFD regexes or
        # binary-format magic strings. Decode their bytes above, but don't
        # mistake their program literals for displayed document text.
        content = re.sub(
            r"<script\b[^>]*>.*?</script\s*>",
            lambda match: "\n" * match.group().count("\n"),
            content, flags=re.I | re.S,
        )
    issues = []
    for number, line in enumerate(content.split("\n"), 1):
        if CORRUPTION.search(line):
            issues.append((number, "replacement character or a common mojibake signature"))
        if CONTROLS.search(line):
            issues.append((number, "unexpected control character"))
    if suffix == ".html" and re.search(r"<!doctype\s+html|<html\b", content, re.I):
        if not UTF8_META.search(content[:1024]):
            issues.append((1, "standalone HTML needs an early UTF-8 charset declaration"))
    return issues


def inspect(root):
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, check=True, stdout=subprocess.PIPE,
    )
    names = sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})
    checked, issues = 0, []
    for name in names:
        path = root / name
        if path.suffix.lower() not in SUFFIXES:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            issues.append({"path": name, "line": 1, "reason": "documentation symlink leaves the checked file set"})
            continue
        if not path.exists():
            continue  # Staged files deleted in the working tree are not read.
        checked += 1
        issues.extend(
            {"path": name, "line": line, "reason": reason}
            for line, reason in findings(path.read_bytes(), path.suffix.lower())
        )
    return {"checked_files": checked, "issues": issues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="Machine-readable findings; ASCII-safe console output")
    args = parser.parse_args()
    try:
        report = inspect(args.root.resolve())
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Text check failed: {error}") from error
    if args.json:
        print(json.dumps(report, ensure_ascii=True, sort_keys=True))
    else:
        for item in report["issues"]:
            print(f"{item['path']}:{item['line']}: {item['reason']}")
        print(f"Text checks: {report['checked_files']} public files, {len(report['issues'])} findings.")
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
