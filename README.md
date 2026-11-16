# Martin Curkovic: website

A small, fast, static site: a home page, a landing page for each song, and a link-in-bio page.
No frameworks and no build step for the live site, just HTML, CSS and optimised images.
Hosted on GitHub Pages at <https://martincurkovic.com>.

## What's in the folder

```
index.html            Home page (hero, About, music, label, contact). Shows only the latest release.
middle/ putitdown/ believe/ ...   One landing page per song (use these for Meta ads)
discog/               Discography page: the playlist, plus a list of every release
links/                Link-in-bio page for the Instagram profile
404.html              "Page not found" page (GitHub Pages shows it automatically)
robots.txt            Tells search engines everything is fine to crawl, and where the sitemap is
sitemap.xml           List of public pages for search engines
CNAME                 Tells GitHub Pages the domain (martincurkovic.com)
style.css             All the styling
pixel.js              Meta Pixel + streaming-button click tracking
app-links.js          Opens Spotify in the app from Instagram/Facebook/TikTok in-app browsers
previews.js           Tap-to-play preview on the cover art
previews/             The short preview clips played when you tap the cover art
img/                  Optimised WebP images used on the site (img/og/ holds the JPEG share-card images)
src-images/           Original images (not served, used to make img/)
tools/releases.py     The release data: titles, credits, links, covers. Edit this to change a song.
tools/build.py        Generates every song page, discog/, links/, 404, sitemap, and parts of index.html
tools/optimize-images.py   Makes img/ from src-images/
tools/icons/          Platform logos (Simple Icons, public domain), inlined into the pages by build.py
AGENTS.md / CLAUDE.md Notes for AI coding assistants
```

## Previewing locally

```
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Opening the files directly also works, but links to folders such
as `middle/` won't open correctly that way. Your browser may cache the stylesheet: hard reload
(Cmd+Shift+R) if a change doesn't show.

## Common tasks

**Change a streaming link, or add a release:** edit the list in `tools/releases.py`, then run

```
python3 tools/build.py
```

This rewrites every song page, `discog/`, `links/`, the sitemap and the home page's generated blocks, so
they always agree. Commit the result. (Generated files are listed in `AGENTS.md`; don't edit them by
hand, as the next build overwrites your changes.) Releases are listed newest first, and the first one
is automatically the "new release" on the home page and the link-in-bio page. Each song's Beatport and
Bandcamp links sit under an "Extended mix" heading: that's the `extended` list in `releases.py`. The
steps for a new release are in `AGENTS.md`.

**Change text, the About, label or contact sections, or the styling:** edit `index.html` or
`style.css` directly. Anything outside the generated markers in `index.html` is hand-written.
The Contact buttons are the exception: they come from `SOCIAL_LINKS` in `tools/build.py`, so to
change or add a social link, edit that list and rebuild.

**Swap an image:** replace the original in `src-images/` (keep the file name), then run

```
python3 tools/optimize-images.py
```

It needs Pillow (`pip install pillow`).

**Meta Pixel:** the Pixel ID is set in `PIXEL_ID` at the top of `pixel.js` (clear it to switch the
pixel off). Every release page and `links/` sends a PageView, plus a custom `StreamingLinkClick` event
(with `platform` and `release`) whenever a streaming button is clicked, and `PreviewPlay` when a
preview is played.

**The domain:** `SITE_URL` in `tools/build.py` is `https://martincurkovic.com` (no trailing slash). It
adds the share-card tags (og:url, og:image, canonical), writes `sitemap.xml` and adds the `Sitemap:`
line to `robots.txt`. If you change domain, edit `SITE_URL` and the `CNAME` file, and rebuild.

## Still to do

- Decide whether the Meta Pixel needs a consent banner (if you advertise in the EU, UK or similar).
- Decide whether to add a VIP email signup (needs a hosted service; a static site can't store emails).
