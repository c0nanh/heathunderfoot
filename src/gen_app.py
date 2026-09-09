import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'src'
route=json.load(open(SRC/'route.json'))
stops=json.load(open(SRC/'stoptext.json'))
ART="https://claude.ai/code/artifact/cacebbfc-b935-4210-8014-4fba681b975c"

COORD={1:(51.55388,-0.1514),2:(51.55787,-0.15189),3:(51.55967,-0.15969),4:(51.5626,-0.1610),
5:(51.56535,-0.16983),6:(51.5693,-0.16917),7:(51.57155,-0.1679),8:(51.57158,-0.1729),
9:(51.57005,-0.17411),10:(51.56788,-0.17792),11:(51.5675,-0.18293),12:(51.56455,-0.18231),
13:(51.56187,-0.18055),14:(51.5606,-0.1783),15:(51.55933,-0.17942),16:(51.55782,-0.17932),
17:(51.55729,-0.17658),18:(51.56038,-0.17198),19:(51.55974,-0.16544),20:(51.55561,-0.15796)}
for s in stops:
    s['lat'],s['lon']=COORD[s['n']]
    s['detour']= s['n'] in (4,14)

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

tpl=open(SRC/'app_template.html').read()
html=(tpl.replace('/*__ROUTE__*/','ROUTE='+json.dumps(route)+';')
        .replace('/*__STOPS__*/','STOPS='+json.dumps(stops)+';')
        .replace('/*__FEATS__*/','FEATS='+json.dumps(feats)+';')
        .replace('__ART__',ART))
open(ROOT/'public'/'index.html','w').write(html)
print('wrote', ROOT/'public'/'index.html', len(html), 'bytes')
print('Remember to bump BUILD in public/sw.js before deploying.')
