# Sources

`public/index.html` is generated, not hand-written. Editing it directly works
but the next `gen_app.py` run overwrites it.

## Regenerate

```bash
python3 src/gen_app.py
```

Run from anywhere — paths resolve relative to the repository root.

## How the generation works

`app_template.html` contains three placeholder comments:

```
/*__ROUTE__*/   ->  ROUTE = [[lat, lon], ...]        (741 points)
/*__STOPS__*/   ->  STOPS = [{n, title, where, km, ele, html, lat, lon, detour}]
/*__FEATS__*/   ->  FEATS = [{id, lat, lon, stop, name, blurb}]
```

`gen_app.py` reads `route.json` and `stoptext.json`, holds the eighteen
features inline in its `FEATS` list, substitutes all three, and writes
`public/index.html`.

`route.json` was simplified from the original Strava GPX by keeping a point
every 12 m — 741 of the original 11,650. The GPX itself is not in the
repository.
