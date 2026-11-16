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

**Set the domain:** put the live address in `SITE_URL` in `tools/build.py` (for example
`"https://yourdomain.com"`, no trailing slash) and rebuild. This adds og:url and og:image tags for
share previews, and writes `sitemap.xml` (it is skipped while `SITE_URL` is empty, because sitemaps
need full addresses) and adds a `Sitemap:` line to `robots.txt`.

## Still to do

- Set `SITE_URL` once the domain is live (above).
- Decide whether a consent banner is needed for the Meta Pixel (see below).
- Decide whether to add a VIP email signup (needs a hosted service; a static site can't store emails).

## Going live (GitHub Pages)

1. Create a GitHub repo and push this folder. The default branch should be `main`.
2. In the repo: Settings, then Pages, then deploy from the `main` branch, `/ (root)`.
3. Add your domain under Settings, Pages, Custom domain. GitHub creates a `CNAME` file for you.
4. At your domain registrar, point DNS at GitHub Pages (GitHub's docs list the current records).
5. Check that the site and the release pages work on the new domain **before** cancelling GoDaddy,
   and keep the domain itself renewed. (Your email is on iCloud, not GoDaddy, so moving the DNS
   won't affect it.)

GitHub Pages on a free personal account needs a public repository. Cloudflare Pages and Netlify
can host the same files from a private repo.
