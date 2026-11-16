# Martin Curkovic: website

A small, fast, static site: a home page, a landing page for each song, and a link-in-bio page.
No frameworks and no build step for the live site, just HTML, CSS and optimised images.

## What's in the folder

```
index.html            Home page (hero, music, label, contact). Shows only the latest release.
middle/ putitdown/ believe/ ...   One landing page per song (use these for Meta ads)
discog/               Discography page: the playlist, plus a list of every release
links/                Link-in-bio page for the Instagram profile
404.html              "Page not found" page (GitHub Pages shows it automatically)
robots.txt            Tells search engines everything is fine to crawl (and where the sitemap is)
sitemap.xml           List of public pages for search engines (appears once SITE_URL is set)
style.css             All the styling
pixel.js              Meta Pixel + streaming-button click tracking
app-links.js          Opens Spotify in the app from Instagram/Facebook/TikTok in-app browsers
previews.js           Tap-to-play preview on the cover art
previews/             The short preview clips played when you tap the cover art
img/                  Optimised WebP images used on the site
src-images/           Original images (not served, used to make img/)
tools/releases.py     The release data: titles, credits, links, covers. Edit this to change a song.
tools/build.py        Generates every song page, discog/, links/ and the home page's hero and music block
tools/optimize-images.py   Makes img/ from src-images/
tools/icons/          Platform logos (Simple Icons, public domain), inlined into the pages by build.py
AGENTS.md / CLAUDE.md Notes for AI coding assistants
```

## Previewing locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Opening the files directly also works, but links to folders such
as `middle/` won't open correctly that way.

## Common tasks

**Change a streaming link, or add a release:** edit the list in `tools/releases.py`, then run

```
python3 tools/build.py
```

This rewrites every song page, `discog/`, `links/` and the home page's hero and music block, so
they always agree. Commit the result. (The generated files are marked in `AGENTS.md`; don't edit
them by hand, as the next build will overwrite your changes.) Releases are listed newest first, and
the first one is automatically the "new release" on the home page, in the hero and on the link-in-bio
page. The steps for a new release (what to gather, in what order) are in `AGENTS.md`.

**Extended mix links:** each song's Beatport and Bandcamp links sit under their own "Extended mix"
heading on its page. That is the `extended` list in `tools/releases.py`.

**Change text, the label or contact sections, or the styling:** edit `index.html` or `style.css`
directly. Anything outside the `hero-release` and `releases` markers in `index.html` is hand-written.

**Swap an image:** replace the original in `src-images/` (keep the file name), then run

```
python3 tools/optimize-images.py
```

It needs Pillow (`pip install pillow`).

**Meta Pixel:** the Pixel ID is set in `PIXEL_ID` at the top of `pixel.js` (clear it to switch the
pixel off). Every release page and `links/` sends a PageView, plus a custom `StreamingLinkClick` event
(with `platform` and `release`) whenever a streaming button is clicked. If you advertise in the
EU, UK or similar regions, check whether you need a consent banner first.

**The domain:** `SITE_URL` in `tools/build.py` is `https://martincurkovic.com` (no trailing slash). It
adds the share-card tags (og:url, og:image, canonical), writes `sitemap.xml` and adds the `Sitemap:`
line to `robots.txt`. Share images are small JPEGs in `img/og/` (made by `tools/optimize-images.py`):
some chat apps reject WebP share images, so the site's own WebP images aren't used for that. If you
change domain, edit `SITE_URL`, edit the `CNAME` file, and rebuild.

## Still to do

- Decide whether a consent banner is needed for the Meta Pixel (see below).
- Decide whether to add a VIP email signup (needs a hosted service; a static site can't store emails).

## Going live (GitHub Pages)

The repo is `martincurkovic/martin-site`. The `CNAME` file in the repo root tells GitHub Pages the
domain is `martincurkovic.com`.

1. Repo Settings, Pages: deploy from the branch you pushed (`master` is fine), folder `/ (root)`.
2. Same page, Custom domain: `martincurkovic.com`.
3. At GoDaddy (DNS for the domain lives there), change **only** these records:
   - the four `A` records for `@` (the apex) become `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153` and `185.199.111.153` (replacing the two GoDaddy site-builder addresses);
   - the `CNAME` for `www` becomes `martincurkovic.github.io`.
   **Leave everything else alone**: the `MX` records (iCloud mail), the `TXT` records (SPF, Apple
   verification) and the `sig1._domainkey` `CNAME` (iCloud DKIM) are what keep your
   `@martincurkovic.com` email working.
4. Wait for DNS to settle, then tick **Enforce HTTPS** in Pages settings (the certificate can take up
   to an hour to appear).
5. Check the site, the song pages, share previews and the Meta Pixel on the live domain **before**
   cancelling the GoDaddy website plan, and keep the domain registration itself renewed.

GitHub Pages on a free personal account needs a public repository. Cloudflare Pages and Netlify
can host the same files from a private repo.
