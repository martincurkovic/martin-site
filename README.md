# Martin Curkovic: website

A small, fast, static site: a home page, a landing page for each release, and a link-in-bio page.
No frameworks and no build step for the live site, just HTML, CSS and optimised images.

## What's in the folder

```
index.html            Home page (hero, music, label, contact)
middle/               In The Middle landing page   (use these for Meta ads)
smalltalk/            Small Talk landing page
kneedeep/             Knee Deep landing page
discog/               Discography landing page
links/                Link-in-bio page for the Instagram profile
style.css             All the styling
pixel.js              Meta Pixel + streaming-button click tracking (off until an ID is set)
img/                  Optimised WebP images used on the site
src-images/           Original images (not served, used to make img/)
tools/build.py        Generates the release pages, links/ and the music section of index.html
tools/optimize-images.py   Makes img/ from src-images/
AGENTS.md / CLAUDE.md Notes for AI coding assistants
```

## Previewing locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Opening the files directly also works, but links to folders such
as `middle/` won't open correctly that way.

## Common tasks

**Change a streaming link, or add a release:** edit the `RELEASES` list in `tools/build.py`, then run

```
python3 tools/build.py
```

This rewrites every release page, `links/index.html` and the music section of the home page, so
they always agree. Commit the result. (The generated files are marked in `AGENTS.md`; don't edit
them by hand, as the next build will overwrite your changes.)

**Change text, the hero, label or contact sections, or the styling:** edit `index.html` or
`style.css` directly. Anything outside the `releases:start` / `releases:end` markers in
`index.html` is hand-written.

**Swap an image:** replace the original in `src-images/` (keep the file name), then run

```
python3 tools/optimize-images.py
```

It needs Pillow (`pip install pillow`).

**Meta Pixel:** the Pixel ID is set in `PIXEL_ID` at the top of `pixel.js` (clear it to switch the
pixel off). Every release page and `links/` sends a PageView, plus a custom `StreamingLinkClick` event
(with `platform` and `release`) whenever a streaming button is clicked. If you advertise in the
EU, UK or similar regions, check whether you need a consent banner first.

**Set the domain for share previews:** put the live address in `SITE_URL` in `tools/build.py`
(for example `"https://yourdomain.com"`) and rebuild. This adds og:url and og:image tags.

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
