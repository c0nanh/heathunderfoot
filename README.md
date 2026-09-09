# The Heath Underfoot

A walking guide to Hampstead Heath as an installable web app: the 9.45 km
circular route, twenty stops with the full written history of each, eighteen
named features, and your live position on the map.

**Live:** https://theheathunderfoot.netlify.app

Built from a GPX recording of the walk. The written history is researched and
cited; where a well-loved story is legend rather than record, it says so.

## Repository layout

```
public/                 what Netlify serves
  index.html            the app — generated, do not hand-edit
  sw.js                 service worker: offline shell, tiles, libraries
  manifest.webmanifest  Home Screen metadata
  icon-*.png            app icons
src/                    the sources index.html is generated from
  app_template.html     markup, CSS and all the JavaScript
  gen_app.py            injects the data into the template
  route.json            741 [lat, lon] points, simplified from the GPX at 12 m
  stoptext.json         the twenty stops: title, location, distance, elevation,
                        and the full HTML of the history text
netlify.toml            publish directory and cache headers
```

## Editing

| To change | Edit |
| --- | --- |
| The writing | `src/stoptext.json` — the `html` field of a stop |
| Design, layout, behaviour | `src/app_template.html` |
| Features on the map | the `FEATS` list near the top of `src/gen_app.py` |
| The route | `src/route.json` — an array of `[lat, lon]` pairs |

Then regenerate and bump the build number:

```bash
python3 src/gen_app.py          # rewrites public/index.html
# then increase  var BUILD = N;  in public/sw.js
git commit -am "…" && git push
```

### Why the build number matters

The service worker caches the app so it works without a signal. If `BUILD` is
not increased, an iPhone that already has the app on its Home Screen can keep
serving the old copy indefinitely. Bump it and the next online launch updates
itself, briefly showing "Updated — reloading". Saved map tiles survive the
update; only the app shell is replaced.

## Deploying

Netlify is set to publish `public/`. With the repository linked (Site
configuration → Build & deploy → Continuous deployment), every push to `main`
deploys itself. No build command is needed — `gen_app.py` is run locally and
its output is committed.

Rollback: Deploys tab → pick an earlier deploy → Publish deploy.

## Using it

- **Locate** — follows your position; a blue dot with an accuracy ring. Drag
  the map and the button becomes Recentre; tap again to stop tracking.
- **Stops** — all twenty, with live distances from wherever you are standing.
- **Markers** — numbered circles are stops, diamonds are features. Tap either
  for a summary, then Read for the full text.
- **Save map** — pre-downloads about 280 OpenStreetMap tiles across four zoom
  levels, so the map works with no signal. Do it on wi-fi before setting out.

Geolocation requires an `https://` origin. Opening `public/index.html` from the
filesystem will not locate you.

## Credits and licensing

- Map data © OpenStreetMap contributors, [ODbL](https://www.openstreetmap.org/copyright).
  Tiles from the public OSM tile servers; personal use at this scale is within
  their usage policy.
- [Leaflet](https://leafletjs.com/) 1.9.4, loaded from cdnjs and then cached.
- Typefaces: Newsreader and Archivo Narrow, via Google Fonts.
- Route recorded by Conan Hales, 10 January 2026.

Sources for the history are listed at the foot of the companion web guide.

## Accuracy notes

Stop and feature coordinates are good to a few tens of metres. The four pond
markers were derived from mapped water rather than estimated, and are better
than that. Elevations are barometric readings from the watch.
