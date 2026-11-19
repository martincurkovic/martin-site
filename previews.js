/* Tap the cover art to hear a short preview. Nothing is downloaded until the first tap.
   Markup comes from tools/build.py: <button class="cover-wrap" data-src="..." data-title="...">. */
(function () {
  var btn = document.querySelector('.cover-wrap[data-src]');
  if (!btn) return;

  var title = btn.getAttribute('data-title');
  var audio;

  function state(playing) {
    btn.classList.toggle('playing', playing);
    btn.setAttribute('aria-label', (playing ? 'Pause' : 'Play') + ' preview of ' + title);
  }

  function create() {
    audio = new Audio(btn.getAttribute('data-src'));
    audio.addEventListener('play', function () { state(true); });
    audio.addEventListener('pause', function () { state(false); });
    audio.addEventListener('ended', function () { btn.style.setProperty('--p', 0); state(false); });
    audio.addEventListener('timeupdate', function () {
      if (audio.duration) btn.style.setProperty('--p', audio.currentTime / audio.duration);
    });
    audio.addEventListener('error', function () { state(false); });
    // Meta Pixel and Umami (only if they have loaded): count the first play of the preview.
    var props = { release: document.body.getAttribute('data-release') };
    if (window.fbq) fbq('trackCustom', 'PreviewPlay', props);
    if (window.umami) umami.track('PreviewPlay', props);
  }

  btn.addEventListener('click', function () {
    if (!audio) create();
    if (audio.paused) {
      var p = audio.play();
      if (p && p.catch) p.catch(function () { state(false); });
    } else {
      audio.pause();
    }
  });
})();
