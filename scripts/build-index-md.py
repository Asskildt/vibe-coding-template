#!/usr/bin/env python3
"""Generate web/index.md from web/index.html (stdlib only).

Usage:
  python3 scripts/build-index-md.py          write web/index.md
  python3 scripts/build-index-md.py --check  exit 1 if web/index.md is out of date
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "web" / "index.html"
OUT = ROOT / "web" / "index.md"

HEADER = "<!-- Generated from index.html by scripts/build-index-md.py. Do not edit by hand. -->"
SKIP_TAGS = {"head", "script", "style", "svg", "button"}
VOID_TAGS = {"meta", "link", "img", "br", "hr", "input", "path"}


def squash(text):
    return re.sub(r"[ \t\r\n\xa0]+", " ", text).strip()


class Converter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical = ""
        self.blocks = []
        self.stack = []  # (tag, classes) of open elements
        self.skip_depth = 0
        self.buf = None  # inline text of the current block
        self.prefix = ""
        self.heading_level = 1
        self.list_counter = None
        self.links = []
        self.in_pre = False
        self.pre_text = ""
        self.label = None
        self.repo_link = None

    def in_class(self, name):
        return any(name in c for _, c in self.stack)

    def start_block(self, prefix=""):
        self.buf = []
        self.prefix = prefix

    def end_block(self):
        if self.buf is None:
            return
        text = squash("".join(self.buf))
        if text:
            self.blocks.append(self.prefix + text)
        self.buf = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href", "")
        if tag in VOID_TAGS:
            return
        self.stack.append((tag, classes))
        if self.skip_depth:
            self.skip_depth += 1
            return
        if tag in SKIP_TAGS or "eyebrow" in classes:
            self.skip_depth = 1
            return
        if tag in ("h1", "h2", "h3", "h4"):
            self.heading_level = int(tag[1])
            n = a.get("data-n")
            self.start_block("#" * self.heading_level + " " + (n + " " if n else ""))
        elif tag == "p":
            self.start_block()
        elif tag == "ol":
            self.list_counter = 0
        elif tag == "ul":
            self.list_counter = None
        elif tag == "li":
            if self.list_counter is None:
                self.start_block("- ")
            else:
                self.list_counter += 1
                self.start_block(f"{self.list_counter}. ")
        elif tag == "div" and "item" in classes:
            self.start_block("- ")
        elif tag == "span" and "prompt-label" in classes:
            self.label = []
        elif tag == "pre":
            self.in_pre = True
            self.pre_text = ""
        elif tag == "a":
            if "cta" in classes:
                if self.in_class("hero"):
                    self.repo_link = a.get("href", "")
                    self.skip_depth = 1
                    return
                self.start_block()
            self.links.append(a.get("href", ""))
            self.put("[")
        elif tag == "code":
            self.put("`")
        elif tag == "strong":
            self.put("**")

    def handle_endtag(self, tag):
        if tag in VOID_TAGS or not self.stack:
            return
        _, classes = self.stack.pop()
        if self.skip_depth:
            self.skip_depth -= 1
            if self.skip_depth == 0 and self.repo_link is not None:
                self.blocks.append("Repository: " + self.repo_link)
                self.repo_link = None
            return
        if tag in ("h1", "h2", "h3", "h4", "p", "li") or (tag == "div" and "item" in classes):
            self.end_block()
        elif tag == "span" and "prompt-label" in classes:
            level = min(self.heading_level + 1, 6)
            self.blocks.append("#" * level + " " + squash("".join(self.label)))
            self.label = None
        elif tag == "pre":
            self.in_pre = False
            text = self.pre_text
            fence = "```"
            while fence in text:
                fence += "`"
            self.blocks.append(f"{fence}text\n{text}\n{fence}")
        elif tag == "a":
            href = self.links.pop()
            self.put(f"]({href})")
            self.buf = [re.sub(r"\s+\]\(", "](", "".join(self.buf))] if self.buf else self.buf
            if "cta" in classes:
                self.end_block()
        elif tag == "code":
            self.put("`")
        elif tag == "strong":
            # Grid items read "**Label:** text".
            self.put(":** " if self.in_class("item") else "**")

    def put(self, s):
        if self.buf is not None:
            self.buf.append(s)

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_pre:
            self.pre_text += data
        elif self.label is not None:
            self.label.append(data)
        else:
            self.put(data)


def build():
    conv = Converter()
    conv.feed(SRC.read_text(encoding="utf-8"))
    conv.close()
    head = [HEADER, f"Canonical page: {conv.canonical}"]
    return "\n\n".join(head + conv.blocks) + "\n"


def main():
    content = build()
    if "--check" in sys.argv[1:]:
        current = OUT.read_bytes().decode("utf-8") if OUT.exists() else None
        if current != content:
            print("web/index.md is out of date. Run: python3 scripts/build-index-md.py")
            return 1
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
