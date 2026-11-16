/* Meta (Facebook) Pixel, shared by every release page and the links page.
   The Pixel ID is set below. Clear it (empty quotes) to switch the pixel off:
   while PIXEL_ID is empty, nothing is loaded and nothing is sent.

   Events:
     PageView                    on every page load
     StreamingLinkClick (custom) on every streaming button, with
                                 { platform: 'spotify', release: 'in-the-middle' } */
(function () {
  var PIXEL_ID = '759056146233741';
  if (!PIXEL_ID) return;

  var release = document.body.getAttribute('data-release') || '';

  window.addEventListener('load', function () {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');

    fbq('init', PIXEL_ID);
    fbq('track', 'PageView');
  });

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-platform]');
    if (a && window.fbq) {
      fbq('trackCustom', 'StreamingLinkClick', { platform: a.getAttribute('data-platform'), release: release });
    }
  });
})();
