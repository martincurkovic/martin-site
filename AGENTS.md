# AGENTS.md

Static website for Martin Curkovic (DJ/producer). It replaces a GoDaddy site builder site and the
ToneDen smart links that were used for Instagram and Meta ads. Hosted free as static files
(GitHub Pages is the plan) with Martin's own domain pointed at it.

## Goals and constraints

- **Lightweight above all.** Many visitors are on slow connections. No frameworks, no web fonts,
  no animations, no third-party scripts except the optional Meta Pixel. Keep pages small.
- Plain HTML and CSS. The only JavaScript is `pixel.js`, and it does nothing until a Pixel ID is set.
- Mobile first and responsive. Test narrow widths.
- Use **relative paths** (`../style.css`, `img/...`) so the site works from any base URL.
- No contact form (deliberate, there is no backend). Contact is social links only
  (Instagram DMs for enquiries); Martin chose to keep his email off the site for now.

## Layout

- `index.html`: home page (hero, music, label, contact).
- `middle/ smalltalk/ kneedeep/ discog/`: one landing page per release, for Meta ads. The folder
  names match the old ToneDen URLs on purpose.
- `links/`: link-in-bio hub for the Instagram bio (latest release plus links to the others).
- `style.css`: the only stylesheet. `pixel.js`: Meta Pixel and click tracking (Pixel ID set at the top).
- `app-links.js`: inside Instagram/Facebook/TikTok in-app browsers, opens Spotify in the app (tries the
  `data-app="spotify:track:ID"` link, falls back to the web link after 1.5 s). Regular browsers are untouched.
  `build.py` adds `data-app` to Spotify buttons automatically.
- `img/`: optimised WebP images used by the site. `src-images/`: originals, not served.
- `tools/build.py`: generates the release pages, `links/index.html` and the music section of `index.html`.
- `tools/optimize-images.py`: turns `src-images/` into `img/`.
- `tools/icons/`: platform logo SVGs from Simple Icons (CC0), inlined as `<svg>` next to each streaming
  button label by `build.py`. Icons are decorative (`aria-hidden`); the text label always stays.

## Generated files: do not hand-edit

The release pages, `links/index.html` and the block between `<!-- releases:start -->` and
`<!-- releases:end -->` in `index.html` are written by `tools/build.py`. Change the `RELEASES` list
(or the templates) in that script, run `python3 tools/build.py`, and commit the output. Everything
else in `index.html` and `style.css` is edited by hand.

## Commands

```
python3 tools/build.py              # regenerate pages from the release data
python3 tools/optimize-images.py    # regenerate img/ from src-images/ (needs Pillow)
python3 -m http.server 8000         # preview at http://localhost:8000
```

Preview with the local server, not by opening files directly: folder links like `middle/` do not
resolve to `index.html` under `file://`.

## Adding a new release

**What Martin needs to provide** (ask for anything that is missing):

1. **Title and credited artists**, exactly as shown on Apple Music/Spotify. Check collaborators.
2. **Cover art**: square, at least 640x640 (the distributor's 3000x3000 original is ideal), JPG or PNG.
3. **Streaming links**, only for platforms where it is actually out: Spotify, Apple Music, Beatport,
   Bandcamp, SoundCloud, YouTube (or YouTube Music), Tidal, Deezer, Amazon Music. Use clean URLs:
   strip tracking parameters (`at=`, `ct=`, `utm_*`, affiliate `tag=`). Spotify's `?si=` share token
   is also left off. Martin suspects it helps links open the app, which is untested; if that proves
   true, add it to the Spotify URLs in `RELEASES`.
4. **Optional 30-second preview** (planned, not built yet): a master or WAV plus the start time of the
   30 seconds. Plan: AAC 96 kbps with 1 s fades (about 360 KB), a play button on the artwork, loaded
   only on tap. A release with no clip simply has no play button.

**Steps**

1. Save the cover as `src-images/<key>.jpg`, add a line for it to `JOBS` in `tools/optimize-images.py`
   (480 px wide WebP, quality 78) and run `python3 tools/optimize-images.py`.
2. Add an entry to `RELEASES` in `tools/build.py`, **newest first** (`RELEASES[0]` drives the `links/`
   hub). Fields: `key` (anchor id; also the pixel `release` name), `slug` (folder name: short,
   lowercase, no hyphens, like the old ToneDen URLs), `title`, `artists`, optional `tagline`,
   `cover`, `cover_size`, `desc`, and `platforms` as `(pixel key, label, url)` tuples. Put Spotify first
   (it is the highlighted button); then Apple Music, Beatport, Bandcamp, SoundCloud, YouTube, Tidal,
   Deezer, Amazon. Pixel keys with icons: `spotify apple-music beatport soundcloud youtube
   youtube-music tidal deezer bandcamp amazon-music` (an unknown key just has no icon).
3. Update the hand-written "New release" block in the hero of `index.html` (title, credit, `#anchor`).
4. Run `python3 tools/build.py`, preview with `python3 -m http.server 8000`, and click every link.
5. `git add` and suggest a commit message. The ad URL is `/<slug>/` on the live domain; the pixel
   reports `release=<key>` on each click.

## Open items

- `SITE_URL` in `tools/build.py` is empty (set it once the domain is live, for og:url and og:image).
- The Meta Pixel is live in `pixel.js` (ID 759056146233741) but no consent banner exists yet; check
  whether one is needed for the regions Martin advertises in.
- VIP email signup was dropped; undecided whether to link to a hosted signup page.
- GitHub repo, Pages and DNS are not set up yet.

## Git

Martin makes the commits. Stage changes with `git add` and suggest a commit message; do not commit
or push unless asked.
