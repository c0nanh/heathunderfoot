/* Heath Underfoot — offline shell + map tiles */
/* Bump BUILD on every content change so installed phones pick it up. */
var BUILD = 3;
var SHELL = 'heath-shell-v' + BUILD;
var TILES = 'heath-tiles-v1';   /* keep tiles across builds - they never change */
var LIBS  = 'heath-libs-v1';

var CORE = [
  './', './index.html', './manifest.webmanifest',
  './icon-180.png', './icon-192.png', './icon-512.png',
  './img/s01-oak-village.jpg',
  './img/s02-octavia-hill.jpg',
  './img/s03-constable-london.jpg',
  './img/s04-boudica.jpg',
  './img/s04-tumulus.jpg',
  './img/s05-viaduct.jpg',
  './img/s06-sham-bridge.jpg',
  './img/s07-dido-belle.jpg',
  './img/s07-kenwood.jpg',
  './img/s07-library.jpg',
  './img/s08-constable-spaniards.jpg',
  './img/s08-spaniards-1914.jpg',
  './img/s09-branch-hill.jpg',
  './img/s09-spaniards-road.jpg',
  './img/s10-sandy-heath.jpg',
  './img/s11-bull-bush.jpg',
  './img/s11-pitt-arch.jpg',
  './img/s11-pitt.jpg',
  './img/s12-leg-of-mutton.jpg',
  './img/s13-lever.jpg',
  './img/s13-pergola.jpg',
  './img/s14-jack-straws.jpg',
  './img/s14-whitestone.jpg',
  './img/s15-cloud-study.jpg',
  './img/s16-admirals-house.jpg',
  './img/s16-constable-admirals.jpg',
  './img/s16-fenton-house.jpg',
  './img/s17-burgh-house.jpg',
  './img/s17-flask-walk.jpg',
  './img/s17-well-walk-fountain.jpg',
  './img/s18-east-heath-mcintyre.jpg',
  './img/s18-leigh-hunt.jpg',
  './img/s19-bathing-pond-mcintyre.jpg',
  './img/s19-mixed-pond.jpg',
  './img/s20-lido.jpg'
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(SHELL).then(function (c) { return c.addAll(CORE); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k !== SHELL && k !== TILES && k !== LIBS) return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

function cacheFirst(req, cacheName) {
  return caches.open(cacheName).then(function (cache) {
    return cache.match(req).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        if (res && (res.ok || res.type === 'opaque')) cache.put(req, res.clone());
        return res;
      });
    });
  });
}

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);

  // map tiles
  if (/tile\.openstreetmap\.org$/.test(url.hostname)) {
    e.respondWith(
      cacheFirst(req, TILES).catch(function () {
        return caches.open(TILES).then(function (c) { return c.match(req); });
      })
    );
    return;
  }

  // Leaflet + fonts
  if (url.hostname === 'cdnjs.cloudflare.com' ||
      url.hostname === 'fonts.googleapis.com' ||
      url.hostname === 'fonts.gstatic.com') {
    e.respondWith(cacheFirst(req, LIBS));
    return;
  }

  // app shell: network first, fall back to cache when offline
  if (url.origin === self.location.origin) {
    e.respondWith(
      fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(SHELL).then(function (c) { c.put(req, copy); });
        return res;
      }).catch(function () {
        return caches.match(req).then(function (hit) {
          return hit || caches.match('./index.html');
        });
      })
    );
  }
});
