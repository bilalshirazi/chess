"""Generate a static version of the site for GitHub Pages."""

import json
import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

from openings_data import OPENINGS

# GitHub Pages serves project repos at /repo-name/
REPO = os.environ.get("GITHUB_REPOSITORY", "")
BASE = f"/{REPO.split('/')[-1]}" if REPO else ""

OUT = Path("site")


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    shutil.copytree("static", OUT / "static")

    env = Environment(loader=FileSystemLoader("templates"), autoescape=True)
    env.policies["json.dumps_kwargs"] = {"ensure_ascii": False}

    def tojson_filter(value):
        # Markup prevents double-escaping inside <script> tags
        return Markup(json.dumps(value, ensure_ascii=False))

    env.filters["tojson"] = tojson_filter

    ctx_base = {"base": BASE, "request": None}

    # index
    tmpl = env.get_template("index.html")
    html = tmpl.render(**ctx_base, openings=list(OPENINGS.values()))
    (OUT / "index.html").write_text(html, encoding="utf-8")

    # one page per opening
    for opening in OPENINGS.values():
        out_dir = OUT / "opening" / opening["id"]
        out_dir.mkdir(parents=True)
        tmpl = env.get_template("opening.html")
        html = tmpl.render(**ctx_base, opening=opening)
        (out_dir / "index.html").write_text(html, encoding="utf-8")

    # GitHub Pages needs a .nojekyll file to serve files starting with _
    (OUT / ".nojekyll").touch()

    print(f"Built {2 + len(OPENINGS)} pages → {OUT}/")
    if BASE:
        print(f"Base path: {BASE}")


if __name__ == "__main__":
    build()
