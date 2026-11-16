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
- No contact form (deliberate, there is no backend). Contact is a `mailto:` link plus social links.

## Layout

- `index.html`: home page (hero, music, label, contact).
- `middle/ smalltalk/ kneedeep/ discog/`: one landing page per release, for Meta ads. The folder
  names match the old ToneDen URLs on purpose.
- `links/`: link-in-bio hub for the Instagram bio (latest release plus links to the others).
- `style.css`: the only stylesheet. `pixel.js`: Meta Pixel and click tracking (Pixel ID set at the top).
- `img/`: optimised WebP images used by the site. `src-images/`: originals, not served.
- `tools/build.py`: generates the release pages, `links/index.html` and the music section of `index.html`.
- `tools/optimize-images.py`: turns `src-images/` into `img/`.

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

## Open items

- `SITE_URL` in `tools/build.py` is empty (set it once the domain is live, for og:url and og:image).
- The Meta Pixel is live in `pixel.js` (ID 759056146233741) but no consent banner exists yet; check
  whether one is needed for the regions Martin advertises in.
- VIP email signup was dropped; undecided whether to link to a hosted signup page.
- GitHub repo, Pages and DNS are not set up yet.

## Git

Martin makes the commits. Stage changes with `git add` and suggest a commit message; do not commit
or push unless asked.
