#!/usr/bin/env python3
"""Verify the deployable static snapshot without external dependencies."""

from __future__ import annotations

import argparse
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"
EXCLUDED_TOP_LEVEL = {".git", ".github", "scripts"}
ALLOWED_EXTERNAL_SCRIPTS = {"plausible.io", "challenges.cloudflare.com"}
REQUIRED_CSP = {
    "base-uri 'none'",
    "object-src 'none'",
    "script-src-attr 'none'",
    "upgrade-insecure-requests",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.references: list[tuple[str, str, str]] = []
        self.metas: list[dict[str, str]] = []
        self.html_lang = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        if tag == "html":
            self.html_lang = values.get("lang", "")
        if tag == "meta":
            self.metas.append(values)
        for attribute in ("href", "src", "poster"):
            if value := values.get(attribute):
                self.references.append((tag, attribute, value))


def deployable_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == MANIFEST:
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def expected_manifest() -> str:
    rows = []
    for path in deployable_files():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    return "\n".join(rows) + "\n"


def validate_reference(page: Path, tag: str, attribute: str, value: str) -> list[str]:
    if value.startswith(("#", "mailto:", "tel:", "data:", "blob:")):
        return []
    parsed = urlparse(value)
    if parsed.scheme:
        if parsed.scheme != "https":
            return [f"{page.name}: insecure external URL in {tag}[{attribute}]: {value}"]
        if tag == "script" and parsed.hostname not in ALLOWED_EXTERNAL_SCRIPTS:
            return [f"{page.name}: external script host is not approved: {parsed.hostname}"]
        return []
    if value.startswith("//"):
        return [f"{page.name}: scheme-relative URL is forbidden: {value}"]
    if value.startswith("/"):
        return [f"{page.name}: root-relative asset breaks on GitHub project Pages: {value}"]

    local_path = unquote(parsed.path)
    if not local_path:
        return []
    resolved = (page.parent / local_path).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return [f"{page.name}: reference escapes repository root: {value}"]
    if local_path.endswith("/"):
        resolved /= "index.html"
    if not resolved.exists():
        return [f"{page.name}: missing local {tag}[{attribute}] target: {value}"]
    return []


def inline_script_errors(page: Path, text: str, csp: str) -> list[str]:
    errors = []
    executable_markup = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    for attributes, body in re.findall(
        r"<script\b([^>]*)>(.*?)</script>", executable_markup, re.DOTALL | re.I
    ):
        if (
            re.search(r"\bsrc\s*=", attributes, re.I)
            or re.search(r"\btype\s*=\s*['\"]application/ld\+json['\"]", attributes, re.I)
            or not body.strip()
        ):
            continue
        digest = base64.b64encode(hashlib.sha256(body.encode("utf-8")).digest()).decode("ascii")
        if f"'sha256-{digest}'" not in csp:
            errors.append(f"{page.name}: CSP lacks hash for one inline script")
    return errors


def validate_html(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(text)
    errors: list[str] = []

    if parser.html_lang != "de":
        errors.append(f"{page.name}: html lang must be de")
    if re.search(r"\bzeeg\b", text, re.I):
        errors.append(f"{page.name}: obsolete Zeeg reference found")

    robots = next((meta.get("content", "") for meta in parser.metas if meta.get("name") == "robots"), "")
    if {item.strip().lower() for item in robots.split(",")} != {"noindex", "nofollow"}:
        errors.append(f"{page.name}: preview must remain noindex,nofollow")

    csp = next(
        (
            meta.get("content", "")
            for meta in parser.metas
            if meta.get("http-equiv", "").lower() == "content-security-policy"
        ),
        "",
    )
    if not csp:
        errors.append(f"{page.name}: CSP meta tag is missing")
    else:
        for directive in REQUIRED_CSP:
            if directive not in csp:
                errors.append(f"{page.name}: CSP lacks {directive}")
        if "'unsafe-eval'" in csp:
            errors.append(f"{page.name}: CSP permits unsafe-eval")
        errors.extend(inline_script_errors(page, text, csp))

    for tag, attribute, value in parser.references:
        errors.extend(validate_reference(page, tag, attribute, value))
    return errors


def validate_workflows() -> list[str]:
    errors = []
    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        for number, line in enumerate(workflow.read_text(encoding="utf-8").splitlines(), 1):
            if "uses:" not in line:
                continue
            ref = line.rsplit("@", 1)[-1].split("#", 1)[0].strip()
            if not re.fullmatch(r"[0-9a-f]{40}", ref):
                errors.append(f"{workflow.relative_to(ROOT)}:{number}: mutable action reference")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    html_pages = sorted(ROOT.glob("*.html"))
    if not html_pages:
        errors.append("no HTML pages found")
    for page in html_pages:
        errors.extend(validate_html(page))

    try:
        manifest = json.loads((ROOT / "manifest.webmanifest").read_text(encoding="utf-8"))
        if manifest.get("start_url") != "./" or manifest.get("scope") != "./":
            errors.append("manifest.webmanifest must remain project-path relative")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"invalid manifest.webmanifest: {error}")

    errors.extend(validate_workflows())
    wanted_manifest = expected_manifest()
    if args.write_manifest:
        MANIFEST.write_text(wanted_manifest, encoding="utf-8")
    elif not MANIFEST.exists():
        errors.append("MANIFEST.sha256 is missing")
    elif MANIFEST.read_text(encoding="utf-8") != wanted_manifest:
        errors.append("MANIFEST.sha256 does not match deployable files")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(html_pages)} HTML pages and {len(deployable_files())} deployable files verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
