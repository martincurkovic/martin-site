#!/usr/bin/env python3
"""Generate the release pages, the discography page, the link-in-bio hub and parts of index.html.

Run from the project root:  python3 tools/build.py
Standard library only. The output is plain HTML that is committed to git, so the live site itself
needs no build step. The release data lives in tools/releases.py: edit that, re-run this, commit.

Generated (do not hand-edit):  one folder per release (middle/, putitdown/, ...), discog/, links/,
                               404.html, robots.txt, and sitemap.xml (only once SITE_URL is set)
Partly generated:              index.html, between the hero-release and releases start/end markers
"""
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from releases import DISCOGRAPHY, RELEASES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Set this once the domain is live (no trailing slash), e.g. "https://martincurkovic.com".
# Used for og:url / og:image so Facebook and Instagram show a proper preview card.
SITE_URL = ""

ICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' fill='%230a0a0a'/%3E%3Ctext x='16' y='23' "
    "font-family='Arial,sans-serif' font-size='20' font-weight='900' fill='%23ececec' "
    "text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E"
)

e = escape

# Platform key -> file in tools/icons/ (Simple Icons, CC0). Keys not listed use their own name.
ICON_FILES = {"apple-music": "applemusic", "youtube-music": "youtubemusic", "amazon-music": "amazonmusic"}


def platform_icon(key):
    """Inline SVG for a platform, or '' if there isn't one. Decorative: the text label stays."""
    f = ROOT / "tools" / "icons" / f"{ICON_FILES.get(key, key)}.svg"
    if not f.exists():
        return ""
    paths = "".join(f'<path d="{d}"/>' for d in re.findall(r' d="([^"]+)"', f.read_text(encoding="utf-8")))
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{paths}</svg>'


def head(title, desc, prefix, path, cover=None, noindex=False):
    """<head> for a page one folder deep (prefix '../') or at the root (prefix '')."""
    og = [
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        '<meta property="og:type" content="music.song">',
    ]
    if SITE_URL:
        og.append(f'<meta property="og:url" content="{e(SITE_URL + path)}">')
        if cover:
            og.append(f'<meta property="og:image" content="{e(SITE_URL)}/img/{e(cover)}">')
    lines = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{e(title)}</title>",
        f'<meta name="description" content="{e(desc)}">',
        '<meta name="theme-color" content="#0a0a0a">',
    ]
    if noindex:
        lines.append('<meta name="robots" content="noindex">')
    lines += og
    lines += [f'<link rel="icon" href="{ICON}">', f'<link rel="stylesheet" href="{prefix}style.css">']
    return "\n".join(lines)


def app_uri(key, url):
    """App deep link (spotify:track:ID) for in-app browsers, which ignore normal app handoff. Else ''."""
    m = re.match(r"https://open\.spotify\.com/(track|album|playlist|artist)/(\w+)", url) if key == "spotify" else None
    return f"spotify:{m.group(1)}:{m.group(2)}" if m else ""


def button_items(items, highlight_first):
    out = []
    for i, (key, label, url) in enumerate(items):
        cls = ' class="primary"' if highlight_first and i == 0 else ""
        app = app_uri(key, url)
        data_app = f' data-app="{app}"' if app else ""
        out.append(
            f'    <li><a{cls} data-platform="{key}"{data_app} href="{e(url)}">{platform_icon(key)}{e(label)}</a></li>'
        )
    return "\n".join(out)


def buttons(rel):
    """The streaming buttons, plus a separate 'Extended mix' group (Beatport, Bandcamp) when there is one."""
    html = f'  <ul class="stack">\n{button_items(rel["platforms"], True)}\n  </ul>'
    if rel.get("extended"):
        html += f'\n\n  <h2>Extended mix</h2>\n  <ul class="stack">\n{button_items(rel["extended"], False)}\n  </ul>'
    return html


SOCIALS = (
    '  <p class="more">\n'
    '    <a href="https://www.instagram.com/martincurkovic.mp3">Instagram</a>\n'
    '    <a href="https://www.tiktok.com/@martincurkovic">TikTok</a>\n'
    '    <a href="https://www.youtube.com/@martin_curkovic/">YouTube</a>\n'
    "  </p>"
)

PLAY_ICONS = (
    '<span class="play-icon" aria-hidden="true">'
    '<svg class="i-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'
    '<svg class="i-pause" viewBox="0 0 24 24"><path d="M6 5h4v14H6zm8 0h4v14h-4z"/></svg>'
    '</span><span class="progress" aria-hidden="true"></span>'
)


def scripts(rel):
    tags = ['<script src="../pixel.js" defer></script>', '<script src="../app-links.js" defer></script>']
    if rel.get("preview"):
        tags.append('<script src="../previews.js" defer></script>')
    return "\n".join(tags)


def cover_html(rel):
    """Cover art. With a preview clip it becomes a tap-to-play button (see previews.js)."""
    w, h = rel["cover_size"]
    img = f'<img class="cover" src="../img/{rel["cover"]}" width="{w}" height="{h}" alt="{e(rel["title"])} cover art">'
    if not rel.get("preview"):
        return img
    return (
        f'<button class="cover-wrap" type="button" data-src="../{rel["preview"]}" '
        f'data-title="{e(rel["title"])}" aria-label="Play preview of {e(rel["title"])}">\n'
        f"    {img}\n    {PLAY_ICONS}\n  </button>"
    )


def release_page(rel, extra=""):
    by = e(rel.get("tagline") or rel["artists"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f'{rel["title"]} | Martin Curkovic', rel["desc"], "../", f'/{rel["slug"]}/', rel["cover"])}
</head>
<body data-release="{rel["key"]}">

<main class="bio">
  {cover_html(rel)}
  <h1>{e(rel["title"])}</h1>
  <p class="by">{by}</p>

{buttons(rel)}
{extra}
{SOCIALS}
  <p class="more"><a href="../">More from Martin Curkovic</a></p>
</main>

{scripts(rel)}

</body>
</html>
"""


def all_releases_list():
    """Every release, newest first, as a plain text list (the discography page is the way to reach them all)."""
    rows = []
    for r in RELEASES:
        meta = " · ".join(x for x in (hero_credit(r["artists"]), (r.get("date") or "")[:4]) if x)
        rows.append(
            f'    <li><a href="../{r["slug"]}/"><span class="t">{e(r["title"])}</span>'
            f'<span class="m">{e(meta)}</span></a></li>'
        )
    return "\n  <h2>All releases</h2>\n  <ul class=\"list\">\n" + "\n".join(rows) + "\n  </ul>\n"


def links_page():
    latest = RELEASES[0]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f'Martin Curkovic: {latest["title"]}', latest["desc"], "../", "/links/", latest["cover"], noindex=True)}
</head>
<body data-release="{latest["key"]}">

<main class="bio">
  {cover_html(latest)}
  <h1>{e(latest["title"])}</h1>
  <p class="by">{e(latest["artists"])}</p>

{buttons(latest)}

  <h2>More music</h2>
  <ul class="stack">
    <li><a href="../{DISCOGRAPHY["slug"]}/">Discography</a></li>
    <li><a href="../">Website</a></li>
  </ul>

{SOCIALS}
</main>

{scripts(latest)}

</body>
</html>
"""


def hero_credit(artists):
    """Short credit: 'with Gaazii', or '' for a solo release (the page already says Martin Curkovic)."""
    others = [a.strip() for a in artists.split(" & ") if a.strip() != "Martin Curkovic"]
    return "with " + " & ".join(others) if others else ""


def hero_block():
    r = RELEASES[0]
    credit = hero_credit(r["artists"])
    credit_html = f"\n        <span>{e(credit)}</span>" if credit else ""
    return f"""      <p class="release">
        <span class="eyebrow">New release</span>
        <strong>{e(r["title"])}</strong>{credit_html}
      </p>
      <a class="btn" href="#{r["key"]}">Listen now</a>"""


def index_cards():
    """Home page: only the latest release, then a link to the full discography."""
    r = RELEASES[0]
    w, h = r["cover_size"]
    chips = "\n".join(f'              <li><a href="{e(url)}">{e(label)}</a></li>' for _, label, url in r["platforms"])
    return f"""        <article class="release-card" id="{r["key"]}">
          <img src="img/{r["cover"]}" width="{w}" height="{h}" alt="{e(r["title"])} cover art">
          <div>
            <h3><a href="{r["slug"]}/">{e(r["title"])}</a></h3>
            <p class="by">{e(r.get("tagline") or r["artists"])}</p>
            <ul class="chips">
{chips}
            </ul>
          </div>
        </article>

        <p class="all-releases"><a class="all-link" href="{DISCOGRAPHY["slug"]}/">Full discography</a></p>"""


def not_found_page():
    """404.html. GitHub Pages serves it for any unknown URL, even a nested one like /a/b/, so unlike the
    other pages it uses root-based paths (/style.css, /discog/) instead of relative ones."""
    latest = RELEASES[0]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head("Page not found | Martin Curkovic", "That page doesn't exist.", "/", "/404.html", noindex=True)}
</head>
<body class="nf">

<main class="bio">
  <p class="eyebrow">Martin Curkovic</p>
  <h1>Page not found</h1>
  <p class="by">That link doesn't go anywhere.</p>

  <ul class="stack">
    <li><a class="primary" href="/{latest["slug"]}/">Latest release: {e(latest["title"])}</a></li>
    <li><a href="/{DISCOGRAPHY["slug"]}/">Discography</a></li>
    <li><a href="/">Home</a></li>
  </ul>
</main>

</body>
</html>
"""


def sitemap_xml():
    """Public pages only (not /links/, which is noindex, and not 404). Needs absolute URLs, so SITE_URL."""
    paths = ["/"] + [f"/{r['slug']}/" for r in RELEASES] + [f"/{DISCOGRAPHY['slug']}/"]
    urls = "\n".join(f"  <url><loc>{e(SITE_URL + p)}</loc></url>" for p in paths)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n"
    )


def robots_txt():
    # Allow everything. /links/ is kept out of search results by its noindex tag; blocking it here would
    # stop crawlers from ever seeing that tag.
    lines = ["User-agent: *", "Allow: /"]
    if SITE_URL:
        lines.append(f"Sitemap: {SITE_URL}/sitemap.xml")
    return "\n".join(lines) + "\n"


def fill(src, name, content):
    pattern = re.compile(rf"(<!-- {name}:start -->\n).*?(\n[ \t]*<!-- {name}:end -->)", re.S)
    if not pattern.search(src):
        raise SystemExit(f"index.html is missing the {name}:start / {name}:end markers")
    return pattern.sub(lambda m: m.group(1) + content + m.group(2), src)


def write(path, text):
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main():
    slugs = [r["slug"] for r in RELEASES] + [DISCOGRAPHY["slug"]]
    if len(set(slugs)) != len(slugs):
        raise SystemExit("duplicate slug in tools/releases.py")

    for rel in RELEASES:
        write(ROOT / rel["slug"] / "index.html", release_page(rel))
    write(ROOT / DISCOGRAPHY["slug"] / "index.html", release_page(DISCOGRAPHY, extra=all_releases_list()))
    write(ROOT / "links" / "index.html", links_page())
    write(ROOT / "404.html", not_found_page())
    write(ROOT / "robots.txt", robots_txt())
    sitemap = ROOT / "sitemap.xml"
    if SITE_URL:
        write(sitemap, sitemap_xml())
    else:
        sitemap.unlink(missing_ok=True)
        print("skipped sitemap.xml: set SITE_URL in tools/build.py first (sitemaps need full URLs)")

    index = ROOT / "index.html"
    src = index.read_text(encoding="utf-8")
    src = fill(src, "hero-release", hero_block())
    src = fill(src, "releases", index_cards())
    index.write_text(src, encoding="utf-8")
    print("updated index.html (hero and music section)")


if __name__ == "__main__":
    main()
