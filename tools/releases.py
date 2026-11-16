"""Release data for the site. Edit this file, then run:  python3 tools/build.py

Each entry becomes a landing page at /<slug>/. Newest first: RELEASES[0] is the release shown in the
home-page hero and card, and on the /links/ hub.

  key       anchor id, and the "release" name reported to the Meta Pixel
  slug      folder name / URL path (these match the old ToneDen URLs)
  title, artists, date (YYYY-MM-DD, or None)
  cover     file in img/ (made from src-images/<name>.jpg by tools/optimize-images.py)
  preview   optional: clip played when the cover is tapped (file in previews/)
  platforms (pixel key, button label, url): the main streaming buttons. The first is highlighted.
  extended  same shape: the extended-mix links (Beatport, Bandcamp), shown in their own group
"""

RELEASES = [
    dict(
        key="u-better-believe", slug="believe", title="u better believe",
        artists="Martin Curkovic", date="2026-05-29",
        cover="u-better-believe.webp", cover_size=(480, 480), preview="previews/believe.mp3",
        desc="Listen to u better believe by Martin Curkovic on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/697uoGrBWmKdjpuztTXP7Y?si=776f9983584741e9"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/u-better-believe/6770198423?i=6770198424"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/u-better-believe"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/u-better-believe-extended-mix/6934953"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/u-better-believe"),
        ],
    ),
    dict(
        key="put-it-down", slug="putitdown", title="Put It Down EP",
        artists="Martin Curkovic & Gaazii", date="2026-03-27",
        cover="put-it-down.webp", cover_size=(480, 480), preview="previews/putitdown.mp3",
        desc="Listen to Put It Down EP by Martin Curkovic & Gaazii on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/5TH0EFfpFLaYJVaSOU9tLZ?si=7c770a39628e408a"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/put-it-down/1882152527?i=1882152531&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/playlist?list=OLAK5uy_lJOCFSnSmsFcfzzeXarkhruQxeH-Yv9oM"),
            ("youtube", "YouTube", "https://youtube.com/playlist?list=OLAK5uy_kBhrZW3JeQ5KL7dT89b40zFoteZ5MJXwU"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/sets/put-it-down-ep"),
            ("tidal", "Tidal", "https://tidal.com/track/503616697/u"),
            ("deezer", "Deezer", "https://link.deezer.com/s/32PzxuY58GVC0EMJIzFhn"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0GQWK3CNJ"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/put-it-down-extended/6405395"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/put-it-down-ep"),
        ],
    ),
    dict(
        key="flowers", slug="flowers", title="Flowers",
        artists="Martin Curkovic", date="2025-12-19",
        cover="flowers.webp", cover_size=(480, 480), preview="previews/flowers.mp3",
        desc="Listen to Flowers by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/1jFtlZUviLfIpBZWq4sNFi?si=a2b854530a61423b"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/flowers/1882152527?i=1882152534"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=yqw-KSp8TyM"),
            ("youtube", "YouTube", "https://youtube.com/playlist?list=OLAK5uy_kBhrZW3JeQ5KL7dT89b40zFoteZ5MJXwU"),
            ("tidal", "Tidal", "https://tidal.com/track/503616698/u"),
            ("deezer", "Deezer", "https://link.deezer.com/s/32P8Qn1UCHP3wol1UrRgq"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0GQWK3CNJ?trackAsin=B0GQWFVQHY"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/put-it-down-extended/6405395"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/put-it-down-ep"),
        ],
    ),
    dict(
        key="i-remember", slug="i-remember", title="I Remember",
        artists="Martin Curkovic", date="2025-11-28",
        cover="i-remember.webp", cover_size=(480, 480), preview="previews/i-remember.mp3",
        desc="Listen to I Remember by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/741OL26sDrfQkf3dQvuLKM?si=831ee5f86b9748ee"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/i-remember-radio-edit/1854935197?i=1854935198&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=GHKzPexXPog"),
            ("youtube", "YouTube", "https://youtu.be/GHKzPexXPog"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/i-remember"),
            ("tidal", "Tidal", "https://tidal.com/track/474537469/u"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3660080632"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0G2L9P279?trackAsin=B0G2L9523K"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/i-remember-extended-mix/5624386"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/i-remember"),
        ],
    ),
    dict(
        key="no-sleep", slug="nosleep", title="NO SLEEP",
        artists="Martin Curkovic", date="2025-08-29",
        cover="no-sleep.webp", cover_size=(480, 480), preview="previews/nosleep.mp3",
        desc="Listen to NO SLEEP by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/1nA4eyoUXFFAoRU3roVnAA?si=13d588c0bec24d4b"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/no-sleep/1825853778?i=1825853779&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=8QhgTaWZEbc"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=8QhgTaWZEbc"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/no-sleep"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/446895636"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3451061761"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0FH4FW3P7?trackAsin=B0FH4CKMWB"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/no-sleep-extended-mix/5170212"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/no-sleep"),
        ],
    ),
    dict(
        key="go-silly", slug="go-silly", title="Go Silly",
        artists="Martin Curkovic", date="2025-07-25",
        cover="go-silly.webp", cover_size=(480, 480), preview="previews/go-silly.mp3",
        desc="Listen to Go Silly by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/1JDWXoSZCHMoC3oQ0dBCWY?si=0b44bb965aac454e"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/go-silly/1825845437?i=1825845441&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=JwykdDM8i-A"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=JwykdDM8i-A"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/go-silly"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/446888527"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3451011241"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0FH433B3T?trackAsin=B0FH4HBHV3"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/go-silly-extended-mix/5170191"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/go-silly"),
        ],
    ),
    dict(
        key="ocean", slug="ocean", title="Ocean",
        artists="Martin Curkovic", date="2025-06-27",
        cover="ocean.webp", cover_size=(480, 480), preview="previews/ocean.mp3",
        desc="Listen to Ocean by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/7uYSs5LykltPYa4mtaRcfD?si=c6a0d1d3a0e145c4"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/ocean-radio-edit/1818918141?i=1818918142&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=vFpAIYesppA"),
            ("youtube", "YouTube", "https://youtu.be/vFpAIYesppA"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/ocean"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/440254182"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3400192531"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0FC21BC5L?trackAsin=B0FC1HRHZ9"),
            ("audiomack", "Audiomack", "https://audiomack.com/martincurkovic/song/ocean-radio-edit-radio-edit"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/ocean-extended-mix/5119812"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/ocean"),
        ],
    ),
    dict(
        key="touch-the-sky", slug="touchthesky", title="Touch The Sky",
        artists="Martin Curkovic", date="2025-05-23",
        cover="touch-the-sky.webp", cover_size=(480, 480), preview="previews/touchthesky.mp3",
        desc="Listen to Touch The Sky by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/00uZR5eJfiCTn6U526ihTj?si=995aec6cb8c5430a"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/touch-the-sky-extended-mix/1810997969?i=1810997970"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=cAaJ-Q91Axs"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=cAaJ-Q91Axs"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/touch-the-sky"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/432487046"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3342121991"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0F6LJMTGR?trackAsin=B0F6LXJ1F8"),
            ("audiomack", "Audiomack", "https://audiomack.com/martincurkovic/song/touch-the-sky"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/touch-the-sky-extended-mix/5058572"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/touch-the-sky"),
        ],
    ),
    dict(
        key="mixtape-vol-1", slug="mixtape", title="Mixtape Vol.1 [Lo-Fi House]",
        artists="Martin Curkovic", date="2025-05-09",
        cover="mixtape-vol-1.webp", cover_size=(480, 480),
        desc="Listen to Mixtape Vol.1 [Lo-Fi House] by Martin Curkovic on SoundCloud and Bandcamp.",
        platforms=[
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/sets/mixtape-vol1-lo-fi-house"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/mixtape-vol-1-lo-fi-house"),
        ],
    ),
    dict(
        key="bend-and-break", slug="bendbreak", title="Bend & Break",
        artists="Martin Curkovic", date="2025-02-28",
        cover="bend-and-break.webp", cover_size=(480, 480), preview="previews/bendbreak.mp3",
        desc="Listen to Bend & Break by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/6lB3GTKblDGIND7yQMFtRI?si=ff2add2e087047a5"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/bend-break-radio-edit/1792107109?i=1792107112&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=_QlAtDA1ODw"),
            ("youtube", "YouTube", "https://youtu.be/_QlAtDA1ODw"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/bend-break"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/412898745"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3195519171"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0DTKHRWHX?trackAsin=B0DTKHWTDY"),
            ("audiomack", "Audiomack", "https://audiomack.com/martincurkovic/song/bend-break-radio-edit-radio-edit"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/bend-break-extended-mix/4905884"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/bend-break"),
        ],
    ),
    dict(
        key="in-the-middle", slug="middle", title="In The Middle",
        artists="Martin Curkovic & Gaazii", date="2025-01-31",
        cover="in-the-middle.webp", cover_size=(480, 480), preview="previews/middle.mp3",
        desc="Listen to In The Middle by Martin Curkovic & Gaazii on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/0uEKLND614J1nU1ST71xpA?si=05c18918eeda486d"),
            ("apple-music", "Apple Music", "https://music.apple.com/album/in-the-middle/1787778352?i=1787778353"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/inthemiddle"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=mpKRmB7B1kQ"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/408027668"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3162056011"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0DRJF27Y5?trackAsin=B0DRJDM3BF"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/in-the-middle-extended-mix/4873192"),
        ],
    ),
    dict(
        key="knee-deep", slug="kneedeep", title="Knee Deep",
        artists="22DEADROSES & Martin Curkovic", date="2025-01-17",
        cover="knee-deep.webp", cover_size=(480, 480), preview="previews/kneedeep.mp3",
        desc="Listen to Knee Deep by 22DEADROSES & Martin Curkovic on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/2FrPnMaB911IgMFmcD3Qer?si=07298021ca5e4d07"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/knee-deep-single/1720538789"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/knee-deep"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=czrIx3_e6IE"),
            ("tidal", "Tidal", "https://tidal.com/browse/album/334195246"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/knee-deep/4469795"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/track/knee-deep"),
        ],
    ),
    dict(
        key="tulum", slug="tulum", title="Tulum",
        artists="Martin Curkovic & Gaazii", date="2024-10-18",
        cover="tulum.webp", cover_size=(480, 480), preview="previews/tulum.mp3",
        desc="Listen to Tulum by Martin Curkovic & Gaazii on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/0ZqhxCU88lnkU9u9x3RWJk?si=2017add8f3aa4f09"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/tulum-radio-edit/1772836237?i=1772836239&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=uB76ThmUEOU"),
            ("youtube", "YouTube", "https://youtu.be/uB76ThmUEOU"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/391888121"),
            ("deezer", "Deezer", "https://www.deezer.com/track/3040786211"),
            ("amazon-music", "Amazon Music", "https://music.amazon.com.au/albums/B0DJN3TGZ2?trackAsin=B0DJN4PQQR"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/tulum-feat-gaazii-extended-mix/4768652"),
        ],
    ),
    dict(
        key="small-talk", slug="smalltalk", title="Small Talk",
        artists="Martin Curkovic", date="2024-10-11",
        cover="small-talk.webp", cover_size=(480, 480), preview="previews/smalltalk.mp3",
        desc="Listen to Small Talk by Martin Curkovic on Spotify, Apple Music, Beatport and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/5OrZALCmQXs52e5lRuC1S5?si=869d1cbf24234592"),
            ("apple-music", "Apple Music", "https://music.apple.com/au/album/small-talk-extended-mix/1768560013?i=1768560014"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/small-talk"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=V22WMzOspn8"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/386688343"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2991078581"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/small-talk-extended-mix/4732288"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/small-talk"),
        ],
    ),
    dict(
        key="pick-up-the-phone", slug="phone", title="Pick Up The Phone",
        artists="Martin Curkovic", date="2024-09-09",
        cover="pick-up-the-phone.webp", cover_size=(480, 480), preview="previews/phone.mp3",
        desc="Listen to Pick Up The Phone by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/0k82jVlQbbsAvJbbuR8zyf?si=e6a5e138bba642ad"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/pick-up-the-phone/1762563304?i=1762563305&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=OBjZ-pDBg64"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=OBjZ-pDBg64"),
            ("soundcloud", "SoundCloud", "https://on.soundcloud.com/Y4nXHfqWXTqJyrHh9"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/380699867"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2943613441"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/pick-up-the-phone-extended-mix/4690451"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/pick-up-the-phone"),
        ],
    ),
    dict(
        key="find-a-place", slug="findaplace", title="Find a Place",
        artists="Martin Curkovic", date="2024-08-02",
        cover="find-a-place.webp", cover_size=(480, 480), preview="previews/findaplace.mp3",
        desc="Listen to Find a Place by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/4AJrmLS7BOprUlPTlppyfF?si=69f58886dfe04d95"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/find-a-place/1756026928?i=1756026929&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=5AF3lsA0xYA"),
            ("youtube", "YouTube", "https://youtu.be/5AF3lsA0xYA"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/find-a-place"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/373710951"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2879580212"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/release/find-a-place-extended-mix/4642571"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/find-a-place"),
        ],
    ),
    dict(
        key="disco-biscuits", slug="discobiscuits", title="Disco Biscuits",
        artists="Martin Curkovic", date="2024-07-05",
        cover="disco-biscuits.webp", cover_size=(480, 480), preview="previews/discobiscuits.mp3",
        desc="Listen to Disco Biscuits by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/63FGN3zovtEllOBr6dQA9w?si=cdb79712b06a4496"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/disco-biscuits-radio-edit/1744239346?i=1744239559&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=o_d7Pk_AXLs"),
            ("youtube", "YouTube", "https://youtu.be/o_d7Pk_AXLs"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/disco-biscuits"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/360883186"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2783304252"),
        ],
        extended=[
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/disco-biscuits"),
        ],
    ),
    dict(
        key="back-again", slug="backagain", title="Back Again",
        artists="Martin Curkovic", date="2024-06-07",
        cover="back-again.webp", cover_size=(480, 480), preview="previews/backagain.mp3",
        desc="Listen to Back Again by Martin Curkovic on Spotify, Apple Music and more.",
        platforms=[
            ("spotify", "Spotify", "https://open.spotify.com/track/08H6MiO9Qg4tI089BpaDZZ?si=ff4baec852be4c77"),
            ("apple-music", "Apple Music", "https://geo.music.apple.com/album/back-again-radio-edit/1744231020?i=1744231021&app=music"),
            ("youtube-music", "YouTube Music", "https://music.youtube.com/watch?v=r0a8SgNWdEc"),
            ("youtube", "YouTube", "https://www.youtube.com/watch?v=r0a8SgNWdEc"),
            ("soundcloud", "SoundCloud", "https://soundcloud.com/martincurkovic/back-again"),
            ("tidal", "Tidal", "https://tidal.com/browse/track/360640005"),
            ("deezer", "Deezer", "https://www.deezer.com/track/2783589732"),
        ],
        extended=[
            ("beatport", "Beatport", "https://www.beatport.com/track/back-again-extended-mix/18993758"),
            ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com/album/back-again"),
        ],
    ),
]

# The playlist landing page at /discog/ (also lists every release above).
DISCOGRAPHY = dict(
    key="discography", slug="discog", title="Discography", artists="Martin Curkovic",
    tagline="Everything in one playlist",
    cover="discography.webp", cover_size=(295, 300),
    desc="Listen to the Martin Curkovic discography on Spotify and Apple Music.",
    platforms=[
        ("spotify", "Spotify", "https://open.spotify.com/playlist/5ODxnUDmVhGXAK0OC3dpHv?si=46c93064630e4881"),
        ("apple-music", "Apple Music", "https://music.apple.com/au/playlist/this-is-martin-curkovic/pl.u-06oxpqbs914Beq"),
        ("bandcamp", "Bandcamp", "https://martincurkovic.bandcamp.com"),
    ],
)
