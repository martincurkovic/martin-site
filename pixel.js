/* Analytics, shared by every release page and the links page: the Meta (Facebook) Pixel and
   Umami Cloud (cloud.umami.is, cookie-free stats dashboard).
   The IDs are set below. Clear one (empty quotes) to switch that tool off: while an ID is empty,
   nothing is loaded and nothing is sent. Both IDs are public by design (they appear in the page
   source), so they are safe to commit. Umami only reports from UMAMI_DOMAIN, so localhost previews
   and copies of the ID on other sites are ignored.

   Events (same names and properties in both tools):
     PageView                    on every page load (Umami: automatic)
     StreamingLinkClick (custom) on every streaming button, with
                                 { platform: 'spotify', release: 'in-the-middle' }
     PreviewPlay (custom)        sent by previews.js */
(function () {
  var PIXEL_ID = '759056146233741';
  var UMAMI_ID = '4b3b379b-1177-45c5-9f25-00fe955f7637';
  var UMAMI_DOMAIN = 'martincurkovic.com';

  var release = document.body.getAttribute('data-release') || '';

  if (UMAMI_ID) {
    var u = document.createElement('script');
    u.defer = true;
    u.src = 'https://cloud.umami.is/script.js';
    u.setAttribute('data-website-id', UMAMI_ID);
    u.setAttribute('data-domains', UMAMI_DOMAIN);
    document.head.appendChild(u);
  }

  if (PIXEL_ID) {
    window.addEventListener('load', function () {
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
      document,'script','https://connect.facebook.net/en_US/fbevents.js');

      fbq('init', PIXEL_ID);
      fbq('track', 'PageView');
    });
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-platform]');
    if (!a) return;
    var props = { platform: a.getAttribute('data-platform'), release: release };
    if (window.fbq) fbq('trackCustom', 'StreamingLinkClick', props);
    if (window.umami) umami.track('StreamingLinkClick', props);
  });
})();
