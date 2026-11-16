#!/usr/bin/env python3
"""Generate the release pages, the link-in-bio hub and the Music section of index.html.

Run from the project root:  python3 tools/build.py
Standard library only. The output is plain HTML that is committed to git, so
the live site itself needs no build step. Edit RELEASES below, re-run, commit.

Generated (do not hand-edit):  middle/ smalltalk/ kneedeep/ discog/  links/
Partly generated:              index.html  (between the releases:start/end markers)
"""
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Set this once the domain is live (no trailing slash), e.g. "https://martincurkovic.com".
# Used for og:url / og:image so Facebook and Instagram show a proper preview card.
SITE_URL = ""

# key      : id used for the #anchor on the home page and as the pixel "release" name
# slug     : folder name, so the page lives at /<slug>/ (matches the old ToneDen URLs)
# platforms: (pixel key, button label, url). First one is the highlighted button.
RELEASES = [
    dict(
        key="in-the-middle", slug="middle", title="In The Middle",
        artists="Martin Curkovic & Gaazii", cover="in-the-middle.webp", cover_size=(480, 480),
        desc="Listen to In The Middle by Martin Curkovic & Gaazii on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/0uEKLND614J1nU1ST71xpA"),
            ("apple-music", "Apple Music", "https://music.apple.com/album/in-the-middle/1787778352?i=1787778353"),
            ("beatport", "Beatport", "https://www.beatport.com/release/in-the-middle-extended-mix/4873192"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/inthemiddle"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=mpKRmB7B1kQ"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/408027668"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3162056011"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0DRJF27Y5?trackAsin=B0DRJDM3BF"),
        ],
    ),
    dict(
        key="small-talk", slug="smalltalk", title="Small Talk",
        artists="Martin Curkovic", cover="small-talk.webp", cover_size=(480, 480),
        desc="Listen to Small Talk by Martin Curkovic on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/5OrZALCmQXs52e5lRuC1S5"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/small-talk-extended-mix/1768560013?i=1768560014"),
            ("beatport", "Beatport", "https://www.beatport.com/release/small-talk-extended-mix/4732288"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/small-talk"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/small-talk"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=V22WMzOspn8"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/386688343"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2991078581"),
        ],
    ),
    dict(
        key="knee-deep", slug="kneedeep", title="Knee Deep",
        artists="Martin Curkovic", cover="knee-deep.webp", cover_size=(480, 480),
        desc="Listen to Knee Deep by Martin Curkovic on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/2FrPnMaB911IgMFmcD3Qer"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/knee-deep-single/1720538789"),
            ("beatport", "Beatport", "https://www.beatport.com/release/knee-deep/4469795"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/track/knee-deep"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/knee-deep"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=czrIx3_e6IE"),
            ("tidal", "Tidal", "https://tidal.com/browse/album/334195246"),
        ],
    ),
    dict(
        key="discography", slug="discog", title="Discography",
        artists="Martin Curkovic", tagline="Everything in one playlist",
        cover="discography.webp", cover_size=(295, 300),
        desc="Listen to the Martin Curkovic discography on Spotify and Apple Music.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/playlist/5ODxnUDmVhGXAK0OC3dpHv"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/playlist/this-is-martin-curkovic/pl.u-06oxpqbs914Beq"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com"),
        ],
    ),
]

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


def buttons(rel):
    items = []
    for i, (key, label, url) in enumerate(rel["platforms"]):
        cls = ' class="primary"' if i == 0 else ""
        app = app_uri(key, url)
        data_app = f' data-app="{app}"' if app else ""
        items.append(
            f'    <li><a{cls} data-platform="{key}"{data_app} href="{e(url)}">{platform_icon(key)}{e(label)}</a></li>'
        )
    return "\n".join(items)


SOCIALS = (
    '  <p class="more">\n'
    '    <a href="https://www.instagram.com/martincurkovic.mp3">Instagram</a>\n'
    '    <a href="https://www.tiktok.com/@martincurkovic">TikTok</a>\n'
    '    <a href="https://www.youtube.com/@martin_curkovic/">YouTube</a>\n'
    "  </p>"
)

SCRIPT_TAGS = '<script src="../pixel.js" defer></script>\n<script src="../app-links.js" defer></script>'


def release_page(rel):
    w, h = rel["cover_size"]
    tagline = rel.get("tagline")
    by = f'{e(rel["artists"])}' if not tagline else f'{e(tagline)}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f'{rel["title"]} | Martin Curkovic', rel["desc"], "../", f'/{rel["slug"]}/', rel["cover"])}
</head>
<body data-release="{rel["key"]}">

<main class="bio">
  <img class="cover" src="../img/{rel["cover"]}" width="{w}" height="{h}" alt="{e(rel["title"])} cover art">
  <h1>{e(rel["title"])}</h1>
  <p class="by">{by}</p>

  <ul class="stack">
{buttons(rel)}
  </ul>

{SOCIALS}
  <p class="more"><a href="../">More from Martin Curkovic</a></p>
</main>

{SCRIPT_TAGS}

</body>
</html>
"""


def links_page():
    latest = RELEASES[0]
    w, h = latest["cover_size"]
    more = "\n".join(
        f'    <li><a href="../{r["slug"]}/">{e(r["title"])}</a></li>' for r in RELEASES[1:]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f'Martin Curkovic: {latest["title"]}', latest["desc"], "../", "/links/", latest["cover"], noindex=True)}
</head>
<body data-release="{latest["key"]}">

<main class="bio">
  <img class="cover" src="../img/{latest["cover"]}" width="{w}" height="{h}" alt="{e(latest["title"])} cover art">
  <h1>{e(latest["title"])}</h1>
  <p class="by">{e(latest["artists"])}</p>

  <ul class="stack">
{buttons(latest)}
  </ul>

  <h2>More music</h2>
  <ul class="stack">
{more}
    <li><a href="../#music">All releases</a></li>
  </ul>

{SOCIALS}
</main>

{SCRIPT_TAGS}

</body>
</html>
"""


def index_cards():
    out = []
    for r in RELEASES:
        w, h = r["cover_size"]
        sub = r.get("tagline") or r["artists"]
        chips = "\n".join(
            f'              <li><a href="{e(url)}">{e(label)}</a></li>' for _, label, url in r["platforms"]
        )
        out.append(f"""        <article class="release-card" id="{r["key"]}">
          <img src="img/{r["cover"]}" width="{w}" height="{h}" loading="lazy" alt="{e(r["title"])} cover art">
          <div>
            <h3><a href="{r["slug"]}/">{e(r["title"])}</a></h3>
            <p class="by">{e(sub)}</p>
            <ul class="chips">
{chips}
            </ul>
          </div>
        </article>""")
    return "\n\n".join(out)


def write(path, text):
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main():
    for rel in RELEASES:
        write(ROOT / rel["slug"] / "index.html", release_page(rel))
    write(ROOT / "links" / "index.html", links_page())

    index = ROOT / "index.html"
    src = index.read_text(encoding="utf-8")
    pattern = re.compile(r"(<!-- releases:start -->\n).*?(\n\s*<!-- releases:end -->)", re.S)
    if not pattern.search(src):
        raise SystemExit("index.html is missing the releases:start / releases:end markers")
    index.write_text(pattern.sub(lambda m: m.group(1) + index_cards() + m.group(2), src), encoding="utf-8")
    print("updated index.html (music section)")


if __name__ == "__main__":
    main()
