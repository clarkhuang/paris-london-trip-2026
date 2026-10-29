import json,html,re
src=open('build_paris_ref.py').read()
exec(src[:src.index('CHECK=')])  # Paris days Nov 28 - Dec 4 exactly as written
C=json.load(open('img/credits.json'))
PARIS=[d for d in DAYS if d[0]!='dec5']
NEW=[
('dec5','Sat Dec 5','Paris → Mont-Saint-Michel','Arrive at the Mont by sunset.','msm',[
 ('Morning','Slow breakfast and check out of Le Cinq Codet (~10:30). Taxi to Paris-Montparnasse, late-morning TGV to Rennes (~1 hr 30) via '+L('SNCF','https://www.sncf-connect.com/en-en/')+'.'),
 ('Afternoon','Pick up a premium sedan or SUV at '+L('SIXT Rennes station','https://www.sixt.com/car-rental/france/rennes/')+' (one-way, returned in Caen on Monday). Easy, toll-free drive to the Mont (~1 hr 15). Check in at '+L('Le Relais Saint-Michel','https://www.mymontsaintmichel.com/en/our-establishments/hotel-le-relais-saint-michel/')+' — ask for a room facing the Mont.'),
 ('Evening','Sunset (~4:55 PM) from the hotel terrace, then the free shuttle across and a quiet walk up the lit, empty village. Dinner at the hotel restaurant facing the bay. Jenny: local fish of the day; Normandy is shellfish country, so flag the allergy every time.')]),
('dec6','Sun Dec 6','The abbey + the D-Day coast','Late-morning abbey, afternoon at the American Cemetery.','omaha',[
 ('Morning','Breakfast with the view. ~10:30 '+L('Mont-Saint-Michel Abbey','https://www.abbaye-mont-saint-michel.fr')+' (~1 hr 30, many steps; dress warm, the wind is sharp).'),
 ('Afternoon','Light lunch, then drive to the D-Day coast (~1 hr 45 on the A84). '+L('Normandy American Cemetery','https://www.abmc.gov/normandy-american-cemetery')+' above Omaha Beach; arrive by ~2:30 to have daylight, the site closes at 5 PM.'),
 ('Evening','~20 min to Bayeux. Check in at '+L('Château de Bellefontaine','https://www.hotel-bellefontaine.com/')+'. Walk to the lit cathedral; easy dinner in town. Early-ish night.')]),
('dec7','Mon Dec 7','Birthday · Normandy → London','A gentle travel day, then the birthday dinner.','london',[
 ('Morning','Sleep in. Late breakfast and a stroll through old Bayeux (the Tapestry itself is in London this year — see Tuesday). ~11:30 drive 30 min to Caen and return the car at the station.'),
 ('Afternoon','Midday train Caen → Paris-Saint-Lazare (~2 hrs), short taxi to Gare du Nord, mid-afternoon '+L('Eurostar','https://www.eurostar.com')+' to London St Pancras (~2 hrs 20; London is one hour behind). Check in at '+L("Claridge's","https://www.claridges.co.uk")+', Mayfair.'),
 ('Evening','Birthday dinner, ~8 PM. Top pick: '+L('Core by Clare Smyth','https://www.corebyclaresmyth.com')+' (request a pescatarian, shellfish-free menu at booking). Fish-forward alternative: '+L("Scott's Mayfair","https://www.scotts-mayfair.com")+'. Old Fashioned first in the hotel bar; Champagne or English sparkling for Jenny; crème brûlée if it is on.')]),
('dec8','Tue Dec 8','The Bayeux Tapestry in London','One timed museum visit.','stpancras',[
 ('Morning','Slow morning. Late-morning timed entry to '+L('The Bayeux Tapestry at the British Museum','https://www.britishmuseum.org/exhibitions/bayeux-tapestry')+' — on loan from Normandy for the first time in nearly 1,000 years, a perfect bookend to the trip.'),
 ('Afternoon','Lunch nearby, then rest at the hotel.'),
 ('Evening','Christmas lights on Regent Street and Bond Street on foot from Mayfair. Relaxed dinner.')]),
('dec9','Wed Dec 9','London at Christmas','Winter Wonderland at dusk.','mayfair',[
 ('Morning','Late breakfast. Wander Mayfair and Burlington Arcade.'),
 ('Afternoon','Afternoon tea or a long lunch. Rest and pack.'),
 ('Evening','Stroll into '+L('Hyde Park Winter Wonderland','https://www.hydeparkwinterwonderland.com')+' after dark (open Nov 19 – Jan 3). Farewell dinner; early night.')]),
('dec10','Thu Dec 10','Fly home from Heathrow','An easy trip home.','heathrow',[
 ('Morning','Breakfast, then a car to Heathrow Terminal 2. United Polaris London → Chicago late morning.'),
 ('Afternoon','Chicago: passport control, re-check bags, Polaris lounge.'),
 ('Evening','United to Traverse City. <em>Times in the United app.</em>')]),
]
ALL=PARIS+NEW
nav=''.join(f'<a href="#{d[0]}">{d[1][:3]} {d[1].split()[-1]}</a>' for d in ALL)
EXTRA={'nov30':'<figure><img src="img/sacre.jpg" alt="Sacré-Cœur"><figcaption>Sacré-Cœur, Montmartre</figcaption></figure>',
'dec1':'<figure><img src="img/montorgueil.jpg" alt="Rue Montorgueil"><figcaption>The Montorgueil quarter, home of Baguette</figcaption></figure>',
'dec2':'<figure><img src="img/trianon.jpg" alt="Trianon Palace"><figcaption>Trianon Palace, home of Gordon Ramsay au Trianon</figcaption></figure>',
'dec6':'<figure><img src="img/bayeux.jpg" alt="Bayeux"><figcaption>Old Bayeux</figcaption></figure>'}
days=''
for i,(id_,date,title,anchor,img,rows) in enumerate(ALL):
  new=id_ in [d[0] for d in NEW]
  ban='<p class="proposed">Proposed, not booked</p>' if new else ''
  tr=''.join(f'<tr><th>{t}</th><td>{v}</td></tr>' for t,v in rows)
  days+=f'<section class="day{" new" if new else ""}" id="{id_}"><div class="dhead"><span class="num">Day {i}</span>{ban}<h2>{date} · {title}</h2><p class="anchor">Anchor: {anchor}</p></div><figure class="lead"><img src="img/{img}.jpg" alt="{title}"></figure><table>{tr}</table><div class="extra">{EXTRA.get(id_,"")}</div></section>'
OPEN=[('Change the United return','Return becomes an open-jaw from London Heathrow (LHR) on Thu Dec 10. Change in the United app; the Paris → Chicago return is replaced.'),
('Rental car','Premium sedan or SUV, Rennes station Sat Dec 5 → Caen station Mon Dec 7 (one-way, same country).'),
('Hotels','Le Relais Saint-Michel (Dec 5), Château de Bellefontaine, Bayeux (Dec 6), Claridge\'s, London (Dec 7–10). Le Cinq Codet is unchanged (check-out Dec 5).'),
('Trains','Paris → Rennes TGV (Dec 5); Caen → Paris and Eurostar Paris → London (Dec 7). Ferry from Caen to Portsmouth is the alternative.'),
('Birthday dinner','Core by Clare Smyth or Scott\'s Mayfair, Mon Dec 7 ~8 PM — pescatarian, no shellfish.'),
('British Museum','Bayeux Tapestry timed entry, Tue Dec 8 (autumn tickets are listed as sold out — check for returns or member slots).')]
op=''.join(f'<tr><td class="by">{a}</td><td>{b}</td></tr>' for a,b in OPEN)
cred=''.join(f'<li>{k}: <a href="{v["page"]}">{html.escape(v["title"][5:])}</a> — {html.escape(v["artist"]) or "Wikimedia Commons"}, {v["license"]}</li>' for k,v in C.items() if not k.startswith('site_'))
cred+='<li>Restaurant images are screenshots of each venue\'s own website.</li>'
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Paris, Normandy &amp; London · Nov 28 – Dec 10, 2026</title><link rel="stylesheet" href="style.css"></head><body>
<header class="hero"><div><p class="kicker">Clark &amp; Jenny</p><h1>Paris, Normandy &amp; London</h1><p>Sat Nov 28 – Thu Dec 10, 2026 · a birthday in London</p><p class="pdf"><a href="paris-london-trip-2026.pdf">Download the PDF</a></p></div></header>
<nav class="days">{nav}<a href="#open">Open</a></nav><main>
<section class="intro"><p class="proposed">Proposed, not booked: everything from Sat Dec 5 on</p><p>The Paris week is unchanged. Then five extra days: a night facing Mont-Saint-Michel, a night in Bayeux by the D-Day coast, and three nights in London with the birthday dinner on Mon Dec 7. Same rhythm: slow mornings, one light anchor a day, one proper dinner.</p>
<p>Weather: Normandy and London in December are cool, grey and damp, highs around 45–48 °F, windy on the coast; sunset ~4:55 PM in Normandy and ~3:50 PM in London. Pack layers, a waterproof jacket and good shoes.</p>
<p>Flights: United via Chicago, details in the United app. The return changes to an open-jaw from London Heathrow (LHR).</p></section>
{days}
<section class="day" id="open"><p class="proposed">Proposed, not booked</p><h2>Open items</h2><table class="chk"><tr><th>Item</th><th>What</th></tr>{op}</table></section>
<section class="day notes"><h2>Dining notes</h2><h3>Jenny: pescatarian, shellfish allergy</h3><blockquote><strong>Je suis allergique aux fruits de mer et crustacés. Je mange du poisson mais pas de fruits de mer.</strong><br><em>In London: "Pescatarian, with a shellfish allergy — no prawns, crab, lobster, scallops, mussels or oysters, and no shellfish stock."</em></blockquote>
<p>Normandy menus lean on oysters, mussels and scallops; ask for the fish of the day (sole, bar, cabillaud, saumon). Jenny: Crémant or Champagne in France, English sparkling in London. Clark: bold reds, an Old Fashioned in the hotel bar, crème brûlée when it appears.</p></section>
<section class="credits"><h2>Photo credits</h2><ul>{cred}</ul></section></main><footer>Bon voyage · Paris, Normandy &amp; London 2026</footer></body></html>'''
open('index.html','w').write(page)
