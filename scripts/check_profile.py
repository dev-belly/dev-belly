"""Check generated graphics and local profile navigation without network access."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from build_profile_assets import PROJECTS, card, hero, stack

ROOT = Path(__file__).resolve().parents[1]
DOCS = ("README.md", "PROJECT_BRIEFS.md", "PROJECT_REVIEW.md")
CARDS = {f"assets/{project[0]}.svg": project for project in PROJECTS}


class ProfileHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.images = []
        self.card_rows = []
        self.links = []
        self.row = None

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "a":
            target = attrs.get("href", "")
            self.links.append(target)
            self.references.append(target)
        elif tag == "tr":
            self.row = []
        elif tag == "img":
            source = attrs.get("src", "")
            if not source or not attrs.get("alt", "").strip():
                raise ValueError("Every profile image needs a source and useful alt text")
            self.references.append(source)
            self.images.append(source)
            if source in CARDS:
                if self.row is None:
                    raise ValueError(f"Project card is outside a table row: {source}")
                self.row.append(source)
                expected = f"https://github.com/dev-belly/{CARDS[source][2]}"
                if not self.links or self.links[-1].casefold() != expected.casefold():
                    raise ValueError(f"Project card links to the wrong repository: {source}")

    def handle_startendtag(self, tag, attributes):
        self.handle_starttag(tag, attributes)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "a" and self.links:
            self.links.pop()
        elif tag == "tr":
            if self.row:
                self.card_rows.append(self.row)
            self.row = None


def heading_anchors(markdown):
    """Recognize the ordinary Markdown headings used by these three documents."""
    anchors, occurrences = set(), Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", markdown, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = occurrences[slug]
        anchors.add(f"{slug}-{count}" if count else slug)
        occurrences[slug] += 1
    return anchors


def check_local_reference(target, document, contents):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc:
        return False  # Published websites are verified separately, not by this offline check.
    path = (document.parent / unquote(parts.path)).resolve() if parts.path else document
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Local link leaves the repository: {target}")
    if not path.is_file():
        raise ValueError(f"Missing local link target in {document.name}: {target}")
    if parts.fragment and path.suffix == ".md":
        text = contents.get(path) or path.read_text(encoding="utf-8")
        if unquote(parts.fragment) not in heading_anchors(text):
            raise ValueError(f"Missing heading target in {document.name}: {target}")
    return True


def check():
    expected = {"profile-hero.svg": hero(), "stack.svg": stack()}
    expected.update({f"{project[0]}.svg": card(project) for project in PROJECTS})
    assets = ROOT / "assets"
    if {path.name for path in assets.glob("*.svg")} != set(expected):
        raise ValueError("SVG file set differs from the generator's expected outputs")
    for name, content in expected.items():
        path = assets / name
        if path.read_text(encoding="utf-8") != content:
            raise ValueError(f"Generated SVG is stale: {name}; run build_profile_assets.py")
        element = ET.parse(path).getroot()
        if element.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"Invalid SVG root: {name}")
        title = element.find("{http://www.w3.org/2000/svg}title")
        if not element.get("viewBox") or title is None or not title.text:
            raise ValueError(f"SVG needs a viewBox and title: {name}")

    contents = {ROOT / name: (ROOT / name).read_text(encoding="utf-8") for name in DOCS}
    parsed = {}
    local_links = 0
    for document, text in contents.items():
        parser = ProfileHTML()
        parser.feed(text)
        parser.close()
        parsed[document.name] = parser
        # The portfolio uses inline Markdown links without parentheses in their targets.
        references = parser.references + re.findall(r"!?\[[^\]\n]+\]\(([^\s)]+)\)", text)
        for target in references:
            if not target:
                raise ValueError(f"Empty link target in {document.name}")
            local_links += check_local_reference(target, document, contents)

    profile = parsed["README.md"]
    if Counter(source for source in profile.images if source in CARDS) != Counter(CARDS.keys()):
        raise ValueError("Each generated project card must appear exactly once in README.md")
    if any(len(row) != 2 for row in profile.card_rows):
        raise ValueError("Every project-card row must contain two cards")
    print(
        f"Profile checks passed: {len(expected)} deterministic SVGs, "
        f"{len(CARDS)} linked cards in {len(profile.card_rows)} pairs, "
        f"{len(DOCS)} documents and {local_links} local references."
    )


if __name__ == "__main__":
    try:
        check()
    except (ValueError, OSError, ET.ParseError) as error:
        raise SystemExit(f"Profile check failed: {error}")
