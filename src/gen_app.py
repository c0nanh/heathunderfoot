"""Build public/index.html from the sources in src/, and keep sw.js's
precache list in step with the images in public/img/."""
import json, re, struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'src'
PUB=ROOT/'public'
route=json.load(open(SRC/'route.json'))
stops=json.load(open(SRC/'stoptext.json'))
ART="https://claude.ai/code/artifact/cacebbfc-b935-4210-8014-4fba681b975c"

from illustrations import SVG

COORD={1:(51.55388,-0.1514),2:(51.55787,-0.15189),3:(51.55967,-0.15969),4:(51.5626,-0.1610),
5:(51.56535,-0.16983),6:(51.5693,-0.16917),7:(51.57155,-0.1679),8:(51.57158,-0.1729),
9:(51.57005,-0.17411),10:(51.56788,-0.17792),11:(51.5675,-0.18293),12:(51.56455,-0.18231),
13:(51.56187,-0.18055),14:(51.5606,-0.1783),15:(51.55933,-0.17942),16:(51.55782,-0.17932),
17:(51.55729,-0.17658),18:(51.56038,-0.17198),19:(51.55974,-0.16544),20:(51.55561,-0.15796)}

def jpeg_size(p):
    """Width and height from a JPEG's SOF marker; PNG from IHDR."""
    b=open(p,'rb').read()
    if b[:8]==b'\x89PNG\r\n\x1a\n':
        w,h=struct.unpack('>II',b[16:24]); return w,h
    i=2
    while i<len(b):
        if b[i]!=0xFF: i+=1; continue
        m=b[i+1]
        if m in (0xD8,0x01) or 0xD0<=m<=0xD7: i+=2; continue
        L=struct.unpack('>H',b[i+2:i+4])[0]
        if m in (0xC0,0xC1,0xC2):
            h,w=struct.unpack('>HH',b[i+5:i+9]); return w,h
        i+=2+L
    return 1200,800

def fig(im,cls):
    return ('<figure class="%s"><img src="img/%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async">'
            '<figcaption>%s%s</figcaption></figure>')%(cls,im['src'],im.get('alt','').replace('"','&quot;'),im['w'],im['h'],
            im.get('caption',''),' <span>%s</span>'%im['credit'] if im.get('credit') else '')

credits=[]
for s in stops:
    s['lat'],s['lon']=COORD[s['n']]
    s['detour']= s['n'] in (4,14)
    imgs=s.get('img',[])
    for im in imgs:
        p=PUB/'img'/im['src']
        if not p.exists():
            raise SystemExit('missing image public/img/%s (stop %d)'%(im['src'],s['n']))
        im['w'],im['h']=jpeg_size(p)
        if im.get('credit'):
            credits.append('Stop %d, %s: %s'%(s['n'],im.get('caption','').rstrip('.'),im['credit']))
    html=s['html']
    # {{img:1}} -> the second image in the stop's list, inline
    html=re.sub(r'\{\{img:(\d+)\}\}',lambda m:fig(imgs[int(m.group(1))],'fig'),html)
    # {{svg:name}} -> an inline illustration
    def svg(m):
        name=m.group(1)
        if name not in SVG: raise SystemExit('no illustration named '+name)
        return SVG[name]
    html=re.sub(r'\{\{svg:([a-z-]+)\}\}',svg,html)
    s['html']=html

FEATS=[
("viaduct",51.5629,-0.17006,5,"The Viaduct","Maryon Wilson's brick bridge of 1844, thrown across the valley to serve 28 villas that were never finished."),
("sham-bridge",51.56938,-0.16665,6,"The Sham Bridge","A painted wooden screen shaped like a three-arched bridge. Repton wanted it gone and was overruled."),
("spaniards",51.5722,-0.1779,8,"The Spaniards Inn & tollhouse","The inn claims 1585; the tollhouse opposite is of about 1710 and still pinches the road to a single lane."),
("bull-bush",51.5680,-0.1846,11,"The Old Bull and Bush","A farmhouse by 1645, licensed for ale in 1721, and the subject of the music-hall song."),
("old-wyldes",51.5697,-0.1867,11,"The Old Wyldes","Eton College's farm from 1449. Linnell lived here and Blake visited; Dickens stayed in 1837."),
("leg-of-mutton",51.5638,-0.1837,12,"Leg of Mutton Pond","Dug about 1816, almost certainly as relief work after the Napoleonic wars."),
("inverforth",51.5617,-0.1802,13,"Inverforth House","Leverhulme's house, The Hill, renamed when Lord Inverforth bought it in 1925."),
("jack-straws",51.5602,-0.1786,14,"Jack Straw's Castle","Named for the 1381 rebel, though no building is recorded here before the 1700s. Rebuilt 1964; now flats."),
("admirals-house",51.5583,-0.1795,16,"Admiral's House","Built 1700. The quarterdeck on the roof is Captain Fountain North's. No admiral ever lived here."),
("fenton-house",51.5578,-0.1797,16,"Fenton House","1693, the oldest surviving mansion in Hampstead. Walled garden, orchard and early keyboards kept in playing order."),
("burgh-house",51.5573,-0.1763,17,"Burgh House","Built 1704; the spa's physician enlarged it in 1720. Now Hampstead Museum."),
("the-flask",51.5566,-0.1768,17,"The Flask, Flask Walk","Where the spa water was bottled, in flasks sealed with a wolf rampant and seven crosslets."),
("well-walk-40",51.5572,-0.1757,17,"40 Well Walk","Constable lived here from 1827 until his death in 1837. The chalybeate fountain of 1882 is a few doors along."),
("st-john",51.5559,-0.1798,17,"St John-at-Hampstead","Constable is buried in the churchyard, five minutes west of Well Walk."),
("keats-house",51.5551,-0.1685,18,"Keats House","Wentworth Place, where Keats wrote the 1819 odes and met Fanny Brawne."),
("ladies-pond",51.56575,-0.15872,19,"Kenwood Ladies' Pond","Opened June 1926 and still the only women-only open-water bathing pond in Europe."),
("mens-pond",51.56298,-0.15624,19,"Highgate Men's Pond","Opened on 1 May 1893, on the Highgate chain."),
("lido",51.5565,-0.1573,20,"Parliament Hill Lido","Opened 20 August 1938, the most expensive of the LCC's thirteen lidos. Unheated."),
]
feats=[dict(id=i,lat=la,lon=lo,stop=st,name=nm,blurb=bl) for i,la,lo,st,nm,bl in FEATS]

base_credits=[
 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors.',
 'Maps drawn with <a href="https://leafletjs.com/">Leaflet</a>. Type: Newsreader and Archivo Narrow.',
 'Route recorded on 10 January 2026. History researched and cited; <a href="%s">sources</a>.'%ART,
]
credits=base_credits+credits

intro=open(SRC/'intro.html').read()
tpl=open(SRC/'app_template.html').read()
html=(tpl.replace('/*__ROUTE__*/','ROUTE='+json.dumps(route)+';')
        .replace('/*__STOPS__*/','STOPS='+json.dumps(stops)+';')
        .replace('/*__FEATS__*/','FEATS='+json.dumps(feats)+';')
        .replace('/*__CREDITS__*/','CREDITS='+json.dumps(credits)+';')
        .replace('/*__INTRO__*/',intro)
        .replace('__ART__',ART))
open(PUB/'index.html','w').write(html)
print('wrote', PUB/'index.html', len(html), 'bytes')

# keep the service worker's precache list in step with public/img
imgs=sorted(p.name for p in (PUB/'img').glob('*') if p.suffix.lower() in ('.jpg','.jpeg','.png','.webp')) if (PUB/'img').exists() else []
sw=open(PUB/'sw.js').read()
core="var CORE = [\n  './', './index.html', './manifest.webmanifest',\n  './icon-180.png', './icon-192.png', './icon-512.png'"
if imgs:
    core+=",\n"+",\n".join("  './img/%s'"%n for n in imgs)
core+="\n];"
sw2=re.sub(r"var CORE = \[.*?\];",core,sw,flags=re.S)
if sw2!=sw:
    open(PUB/'sw.js','w').write(sw2); print('updated CORE in sw.js:',len(imgs),'images')
print('Remember to bump BUILD in public/sw.js before deploying.')
