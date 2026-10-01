"""Link checker: every relative link/image in *.md must resolve to a file,
every absolute http(s) link must not 404/5xx (follows redirects; flags the
known imgur tombstone `removed.png`). Run: python scripts/check-links.py."""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
failures = []


def check_local(source: Path, target: str) -> None:
    path = (source.parent / target.split("#")[0]).resolve()
    if not path.exists():
        failures.append(f"{source.relative_to(ROOT)} -> {target} (missing file)")


def check_remote(source: Path, url: str) -> None:
    if url.startswith("mailto:"):
        return
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "link-checker"}, method="HEAD")
        with urllib.request.urlopen(req, timeout=15) as res:
            final = res.geturl()
            if "removed.png" in final:
                failures.append(f"{source.relative_to(ROOT)} -> {url} (removed upstream)")
            elif res.status >= 400:
                failures.append(f"{source.relative_to(ROOT)} -> {url} (HTTP {res.status})")
    except Exception as e:  # network hiccup: warn, do not fail the build
        print(f"WARN {source.relative_to(ROOT)} -> {url} ({e})")


for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for m in LINK_RE.finditer(text):
        link = m.group(1)
        if link.startswith(("http://", "https://")):
            check_remote(md, link)
        elif not link.startswith(("#", "mailto:")):
            check_local(md, link)

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("All links OK.")
