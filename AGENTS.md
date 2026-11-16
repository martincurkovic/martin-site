# AGENTS.md

Static website for Martin Curkovic (DJ/producer) at https://martincurkovic.com: a home page, a landing
page per song (Meta ads point at these) and a link-in-bio page for Instagram. It replaced a GoDaddy
site-builder site and ToneDen smart links.

## Goals and constraints

- **Lightweight above all.** Many visitors are on slow connections. No frameworks, no web fonts, no
  animations, no third-party scripts except the Meta Pixel. Keep pages small.
- Plain HTML and CSS plus three tiny vanilla JS files (`pixel.js`, `app-links.js`, `previews.js`), loaded
  only on song pages and `links/`. The home page loads none.
- Mobile first and responsive. Test narrow widths.
- Use **relative paths** (`../style.css`, `img/...`). The one exception is `404.html` (see below).
- No contact form (there is no backend) and no email address on the site. Contact is social links only;
  enquiries go via Instagram DM.

## Layout

- `index.html`: home page (hero, About, music, label, contact). The hero and Music section show only the
  **latest release** (`RELEASES[0]`) plus a "Full discography" link.
- One folder per release (`middle/`, `putitdown/`, `believe/`, ...): a landing page per song. Folder names
  are the old ToneDen paths; a new slug can be any short lowercase word.
- `discog/`: the Spotify/Apple playlist page plus a list of **every release**. It is how visitors reach older
  songs, since the home page only shows the latest.
- `links/`: link-in-bio hub for Instagram (latest release, plus links to the discography and the site).
- `404.html`, `robots.txt`, `sitemap.xml`: generated. GitHub Pages serves `404.html` for any unknown URL,
  even a nested one like `/a/b/`, so it alone uses **root-based** paths (`/style.css`). `robots.txt` allows
  everything: `/links/` is kept out of search by its `noindex` tag, and blocking it would hide that tag.
  `sitemap.xml` lists the public pages (not `/links/`, not 404).
- `style.css`; `pixel.js` (Meta Pixel and click tracking); `app-links.js` (inside Instagram/Facebook/TikTok
  in-app browsers, opens Spotify in the app: tries `data-app="spotify:track:ID"`, falls back to the web link
  after 1.5 s; regular browsers are untouched); `previews.js` and `previews/` (tap the cover art to hear
  a clip).
- `img/`: WebP images the site serves. `img/og/`: JPEG share-card images (some chat apps reject WebP).
  `src-images/`: originals, not served.
- `tools/releases.py`: **the release data. Edit this.** `tools/build.py`: generates the release pages,
  `discog/`, `links/`, `404.html`, `robots.txt`, `sitemap.xml` and the hero, music and share-card blocks of
  `index.html`. `tools/optimize-images.py`: `src-images/` to `img/`. `tools/icons/`: Simple Icons logos
  (CC0), inlined as decorative `<svg>` next to each button label (the text label always stays). The social
  links (Contact buttons, song-page footers) are the `SOCIAL_LINKS` list in `build.py`.

## Generated files: do not hand-edit

The release pages, `discog/index.html`, `links/index.html`, `404.html`, `robots.txt`, `sitemap.xml` and the
blocks between the `hero-release`, `releases`, `socials` and `share-card` start/end markers in
`index.html` are written
by `tools/build.py`. Change the data in `tools/releases.py` (or the templates in `build.py`), run
`python3 tools/build.py`, and commit the output. Everything else in `index.html` and `style.css` is edited
by hand.

## Commands

```
python3 tools/build.py              # regenerate pages from the release data
python3 tools/optimize-images.py    # regenerate img/ and img/og/ from src-images/ (needs Pillow)
python3 -m http.server 8000         # preview at http://localhost:8000
```

Preview with the local server, not by opening files directly: folder links like `middle/` do not
resolve to `index.html` under `file://`. A browser may cache `style.css` while you preview; hard reload.

## Hosting and domain

- GitHub Pages from `martincurkovic/martin-site` (branch `master`, root), domain `martincurkovic.com`. The
  `CNAME` file holds the domain, and `SITE_URL` in `tools/build.py` is `https://martincurkovic.com` (it
  drives the og:url/og:image/canonical tags, the sitemap and the `Sitemap:` line). Changing domain means
  editing both and rebuilding.
- DNS is at GoDaddy: four `A` records for `@` (185.199.108.153, 185.199.109.153, 185.199.110.153,
  185.199.111.153) and a `www` `CNAME` to `martincurkovic.github.io`. Martin's email is on iCloud, so
  **never touch the MX or TXT records, the `sig1._domainkey` CNAME, or the `_atproto` TXT record.**
- The Meta Pixel ID (759056146233741) is set at the top of `pixel.js`.

## Adding a new release

**What Martin needs to provide** (ask for anything that is missing):

1. **Title and credited artists**, exactly as shown on Apple Music/Spotify. Check collaborators.
2. **Cover art**: square, at least 640x640 (the distributor's 3000x3000 original is ideal), JPG or PNG.
3. **Streaming links**, only for platforms where it is actually out: Spotify, Apple Music, Beatport,
   Bandcamp, SoundCloud, YouTube (or YouTube Music), Tidal, Deezer, Amazon Music. Beatport and Bandcamp
   are the **extended mix** links (their own group on the page). Use clean URLs: strip tracking parameters
   (`at=`, `ct=`, `utm_*`, affiliate `tag=`) but **keep Spotify's `?si=` share token** (Spotify's Share,
   Copy link). Without it, desktop Safari opens the web player instead of offering the app.
4. **Optional preview clip**: `previews/<slug>.mp3`, set as `preview="previews/<slug>.mp3"` on the release.
   Preferred is a clip cut from Martin's master (a WAV plus the start time is enough; about 96 kbps with
   short fades is roughly 360 KB for 30 s). The current clips are Spotify's own previews: fetch
   `https://open.spotify.com/embed/track/<id>`, read `audioPreview.url` from the page's `__NEXT_DATA__`
   JSON, and download that mp3. A release with no `preview` just shows a plain cover. The Discography has
   none (it is a playlist). Nothing downloads until someone taps.

**Steps**

1. Save the cover as `src-images/<key>.jpg` and run `python3 tools/optimize-images.py` (every jpg there
   becomes a 480 px WebP in `img/` and a JPEG share image in `img/og/`).
2. Add an entry to `RELEASES` in `tools/releases.py`, **newest first**: `RELEASES[0]` is what the home page
   hero, the home page card and the `/links/` hub show, so a new entry becomes the "new release"
   everywhere automatically. Fields are documented at the top of that file. `platforms` are the main
   streaming buttons (Spotify first, it is the highlighted one; then Apple Music, YouTube Music, YouTube,
   SoundCloud, Tidal, Deezer, Amazon Music, Audiomack). `extended` holds Beatport and Bandcamp. Pixel keys
   with icons: `spotify apple-music beatport soundcloud youtube youtube-music tidal deezer bandcamp
   amazon-music audiomack`.
3. Run `python3 tools/build.py`, preview, and click every link.
4. `git add` and suggest a commit message. The ad URL is `/<slug>/` on the live domain; the pixel reports
   `release=<key>` on each click. The release also appears in the Discography list automatically.

## Open items

- `u better believe` (the latest release) was filled in by hand: no YouTube, Tidal, Deezer or Amazon links
  were found. Add them to `tools/releases.py` if they exist.
- `Mixtape Vol.1 [Lo-Fi House]` (`mixtape/`) is not a song: a Bandcamp-only release on 2025-05-09. The old
  ToneDen page also had a SoundCloud link, kept for now.
- Three releases on Apple Music have no page because they never had a ToneDen link: Feel You In My Mind,
  Hey Mr. Postman, Body All Bangin'. They need their links from Martin.
- The Meta Pixel has no consent banner. Decide whether one is needed for the regions Martin advertises in.
- The VIP email signup was dropped. Undecided whether to link to a hosted signup page.
- The preview clips are Spotify's own (five are only about 15 s). Replacing them with clips cut from
  Martin's masters is optional.

## Git

Martin makes the commits. Stage changes with `git add` and suggest a commit message; do not commit
or push unless asked.
