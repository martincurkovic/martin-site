/* Open Spotify in the app from in-app browsers (Instagram, Facebook, TikTok).
   Those web views load links inside themselves instead of handing off to the Spotify app, so a
   plain open.spotify.com link ends up in the browser. Here we try the app link first
   (a[data-app], e.g. spotify:track:ID) and fall back to the normal web link if the app does not
   take over. Regular browsers are left alone: iOS and Android already open the app from a plain
   open.spotify.com link there. */
(function () {
  if (!/Instagram|FBAN|FBAV|FB_IAB|musical_ly|TikTok|BytedanceWebview/i.test(navigator.userAgent)) return;

  var timer;
  // If the app took over the page is hidden: cancel the fallback so we don't navigate on return.
  document.addEventListener('visibilitychange', function () { if (document.hidden) clearTimeout(timer); });
  window.addEventListener('pagehide', function () { clearTimeout(timer); });

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-app]');
    if (!a || ev.defaultPrevented || ev.button || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
    ev.preventDefault();
    var web = a.href;
    location.href = a.getAttribute('data-app');
    timer = setTimeout(function () { if (!document.hidden) location.href = web; }, 1500);
  });
})();
