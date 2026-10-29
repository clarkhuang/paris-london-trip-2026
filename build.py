import json,html,re
src=open('build_paris_ref.py').read()
exec(src[:src.index('CHECK=')])  # Paris days Nov 28 - Dec 4 exactly as written
C=json.load(open('img/credits.json'))
PARIS=[d for d in DAYS if d[0]!='dec5']
NEW=[
('dec5','Sat Dec 5','Paris → Mont-Saint-Michel','Arrive at the Mont by sunset.','msm',[
 ('Morning','Slow breakfast and check out of Le Cinq Codet (~10:30). Taxi to Paris-Montparnasse for a late-morning TGV to Rennes (~1 hr 30, book on '+L('SNCF Connect','https://www.sncf-connect.com/en-en/train/timetables/paris/rennes')+'). Ready to book: trains open well ahead.'),
 ('Afternoon','Pick up a premium sedan (the car makes Sunday\'s D-Day coast easy; the no-car fallback is the '+L('Keolis Rennes → Mont-Saint-Michel bus','https://keolis-armor.com/en/5ey-Timetables-of-the-lines.html')+', daily and timed to the Paris TGVs) or SUV at '+L('SIXT Rennes station','https://www.sixt.com/car-rental/france/rennes/')+' (one-way, returned in Caen on Monday). Easy, toll-free drive to the Mont (~1 hr 15). Check in at '+L('Le Relais Saint-Michel','https://www.mymontsaintmichel.com/en/our-establishments/hotel-le-relais-saint-michel/')+' — ask for a room facing the Mont.'),
 ('Evening','Sunset (~4:55 PM) from the hotel terrace, then the free shuttle across and a quiet walk up the lit, empty village. Dinner at the '+L('Relais Saint-Michel restaurant','https://www.ot-montsaintmichel.com/restaurant/le-relais-saint-michel/')+' facing the lit Mont (open nightly 7–9:30 PM). Jenny: local fish of the day; Normandy is shellfish country, so flag the allergy every time.')]),
('dec6','Sun Dec 6','The abbey + the D-Day coast','Late-morning abbey, afternoon at the American Cemetery.','omaha',[
 ('Morning','Breakfast with the view. ~10:30 '+L('Mont-Saint-Michel Abbey','https://www.abbaye-mont-saint-michel.fr')+' (~1 hr 30, many steps; dress warm, the wind is sharp).'),
 ('Afternoon','Light lunch, then drive to the D-Day coast (~1 hr 45 on the A84). '+L('Normandy American Cemetery','https://www.abmc.gov/normandy-american-cemetery')+' above Omaha Beach; arrive by ~2:30 to have daylight, the site closes at 5 PM.'),
 ('Evening','~20 min to Bayeux. Check in at '+L('Château de Bellefontaine','https://www.chateau-hotel-bayeux.com/')+'. Walk to the lit cathedral. Dinner at '+L('Le Pommier','https://www.restaurantlepommier.com/en/reservation-2')+' (open Sunday evenings in winter, 6:30–8:30 PM; Normandy produce with real vegetarian and fish choices). La Rapière is closed on Sundays. Early-ish night.')]),
('dec7','Mon Dec 7','Birthday · Normandy → London','A gentle travel day, then the birthday dinner.','london',[
 ('Morning','Sleep in. Late breakfast and a stroll through old Bayeux (the Tapestry itself is in London this year — see Tuesday). ~11:00 drive 30 min to Caen and return the car at the station.'),
 ('Afternoon','Midday '+L('Nomad train','https://www.sncf-connect.com/en-en/train/timetables/caen/paris')+' Caen → Paris-Saint-Lazare (~2 hrs), 15-min taxi to Gare du Nord, then the 4:12 PM '+L('Eurostar','https://www.eurostar.com/us-en')+' (Business Premier for lounge and a meal) arriving St Pancras ~5:35 PM London time. Car to Mayfair, time to dress for dinner. The ferry is not a good fit: the afternoon Ouistreham sailing lands in Portsmouth ~9:30 PM, still two hours from London. Check in at '+L("Claridge's","https://www.claridges.co.uk")+', Mayfair.'),
 ('Evening','Birthday dinner, ~8 PM. Top pick: '+L('Core by Clare Smyth','https://www.corebyclaresmyth.com')+' (request a pescatarian, shellfish-free menu at booking). Alternatives: '+L('Hélène Darroze at The Connaught','https://www.the-connaught.co.uk/mayfair-restaurants/helene-darroze/')+' (3 stars, a short walk from Claridge\'s) or '+L('Claridge\'s Restaurant','https://www.claridges.co.uk/restaurants-bars/claridges-restaurant/')+' (no taxi at all). Old Fashioned first in the hotel bar; Champagne or English sparkling for Jenny; crème brûlée if it is on.')]),
('dec8','Tue Dec 8','The Bayeux Tapestry in London','One timed museum visit.','stpancras',[
 ('Morning','Slow morning. 11 AM timed entry to '+L('The Bayeux Tapestry at the British Museum','https://www.britishmuseum.org/exhibitions/bayeux-tapestry')+' — on loan from Normandy for the first time in nearly 1,000 years, a perfect bookend to the trip. <strong>Tickets through March 2027 are sold out</strong>: watch for returns, or join as a Member for access.'),
 ('Afternoon','Lunch nearby, then rest at the hotel.'),
 ('Evening','Christmas lights on Regent Street and Bond Street on foot from Mayfair. Relaxed dinner.')]),
('dec9','Wed Dec 9','London at Christmas','Winter Wonderland at dusk.','mayfair',[
 ('Morning','Late breakfast. Wander Mayfair and Burlington Arcade.'),
 ('Afternoon','Afternoon tea or a long lunch. Rest and pack.'),
 ('Evening','Stroll into '+L('Hyde Park Winter Wonderland','https://www.hydeparkwinterwonderland.com')+' after dark (open Nov 19 – Jan 3). Farewell dinner; early night.')]),
('dec10','Thu Dec 10','Fly home from Heathrow','A relaxed last morning, then Polaris home.','heathrow',[
 ('Morning','Late breakfast at Claridge\'s and a slow pack. Leave around 10:30 AM by car (about an hour), or take a taxi to Paddington and the '+L('Heathrow Express','https://www.heathrowexpress.com')+' (15 min). Reach Heathrow Terminal 2 about 11:30.'),
 ('Afternoon','<strong>UA928</strong> Heathrow T2 1:35 PM → Chicago O\'Hare 4:55 PM, United Polaris (Boeing 767-300). Seats: Clark 4D, Jenny 5F (center seats, one diagonally behind the other).'),
 ('Evening','2h50 connection at O\'Hare: clear passport control and customs, re-check bags and re-screen, then a sit-down dinner in the '+L('United Polaris lounge','https://www.united.com/en/us/fly/travel/airport/lounge-access.html')+' (Terminal 1, near gate C18). <strong>UA2304</strong> O\'Hare 7:45 PM → Traverse City 9:59 PM, First, seats 2E/2F.')]),
]
PARIS=[(a,b,c,d,e,[(t,v.replace('<em>Flight details in the United app.</em>','<strong>UA987</strong> O\'Hare 6:45 PM → Paris CDG 9:55 AM Sun Nov 29 (seats 3D/3F).') if t=='Evening' else v.replace('Short hop from','<strong>UA5867</strong> 2:18 PM → O\'Hare 2:55 PM (seats 2C/2D), short hop from') if t=='Afternoon' else v) for t,v in r]) if a=='nov28' else (a,b,c,d,e,r) for a,b,c,d,e,r in PARIS]
ALL=PARIS+NEW
nav=''.join(f'<a href="#{d[0]}">{d[1][:3]} {d[1].split()[-1]}</a>' for d in ALL)
EXTRA={'nov30':'<figure><img src="img/sacre.jpg" alt="Sacré-Cœur"><figcaption>Sacré-Cœur, Montmartre</figcaption></figure>',
'dec1':'<figure><img src="img/montorgueil.jpg" alt="Rue Montorgueil"><figcaption>The Montorgueil quarter, home of Baguette</figcaption></figure>',
'dec2':'<figure><img src="img/trianon.jpg" alt="Trianon Palace"><figcaption>Trianon Palace, home of Gordon Ramsay au Trianon</figcaption></figure>',
'dec6':'<figure><img src="img/bayeux.jpg" alt="Bayeux"><figcaption>Old Bayeux</figcaption></figure>'}
days=''
for i,(id_,date,title,anchor,img,rows) in enumerate(ALL):
  new=id_ in [d[0] for d in NEW]
  ban='<p class="proposed">Ready to book</p>' if new and id_!='dec10' else ('<p class="proposed">Flights booked</p>' if id_=='dec10' else '')
  tr=''.join(f'<tr><th>{t}</th><td>{v}</td></tr>' for t,v in rows)
  days+=f'<section class="day{" new" if new else ""}" id="{id_}"><div class="dhead"><span class="num">Day {i}</span>{ban}<h2>{date} · {title}</h2><p class="anchor">Anchor: {anchor}</p></div><figure class="lead"><img src="img/{img}.jpg" alt="{title}"></figure><table>{tr}</table><div class="extra">{EXTRA.get(id_,"")}</div></section>'
OPEN=[('Hotels to book (top pick, then alternatives)','Mont-Saint-Michel Dec 5: '+L('Le Relais Saint-Michel','https://www.mymontsaintmichel.com/en/our-establishments/hotel-le-relais-saint-michel/')+' (open all year, rooms and restaurant facing the Mont; ask for a Mont-view room). Alternatives: '+L('La Mère Poulard','https://www.mymontsaintmichel.com/en/our-establishments/hotel-la-mere-poulard/')+' (historic inn inside the walls, open all year) or '+L('Les Terrasses Poulard / La Confiance','https://www.mymontsaintmichel.com/en/our-establishments/')+' (in the village; many steps with bags). Avoid Hôtel Gabriel and Relais du Roy: closed in winter.<br>Bayeux Dec 6: '+L('Château de Bellefontaine','https://www.chateau-hotel-bayeux.com/')+' (18th-century château in a park, a walk from the cathedral). Alternative: '+L("Hôtel d'Argouges",'https://www.hotel-dargouges.com/')+' (18th-century mansion in town). Villa Lara is closed from Nov 30 to Dec 31.<br>London Dec 7–10: '+L("Claridge's",'https://www.claridges.co.uk')+' (Art Deco Mayfair, famous Christmas tree). Alternatives: '+L('The Connaught','https://www.the-connaught.co.uk')+' (quiet Mayfair, Hélène Darroze downstairs) or '+L('Rosewood London','https://www.rosewoodhotels.com/en/london')+' (Holborn, a walk to the British Museum).'),
('Rental car','Premium sedan or SUV, Rennes station Sat Dec 5 → Caen station Mon Dec 7 (one-way, same country).'),
('Trains','Paris → Rennes TGV (Dec 5); Caen → Paris and Eurostar Paris → London (Dec 7). Ferry from Caen to Portsmouth is the alternative.'),
('Birthday dinner','Core by Clare Smyth (top pick), Hélène Darroze at The Connaught, or Claridge\'s Restaurant, Mon Dec 7 ~8 PM — pescatarian, no shellfish.'),
('British Museum','Bayeux Tapestry timed entry, Tue Dec 8 (autumn tickets are listed as sold out — check for returns or member slots).')]
op=''.join(f'<tr><td class="by">{a}</td><td>{b}</td></tr>' for a,b in OPEN)
cred=''.join(f'<li>{k}: <a href="{v["page"]}">{html.escape(v["title"][5:])}</a> — {html.escape(v["artist"]) or "Wikimedia Commons"}, {v["license"]}</li>' for k,v in C.items() if not k.startswith('site_'))
cred+='<li>Restaurant images are screenshots of each venue\'s own website.</li>'
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Paris, Normandy &amp; London · Nov 28 – Dec 10, 2026</title><link rel="stylesheet" href="style.css"></head><body>
<header class="hero"><div><p class="kicker">Clark &amp; Jenny · the current plan</p><h1>Paris, Normandy &amp; London</h1><p>Sat Nov 28 – Thu Dec 10, 2026 · a birthday in London</p><p class="pdf"><a href="paris-london-trip-2026.pdf">Download the PDF</a></p></div></header>
<nav class="days">{nav}<a href="#open">Open</a></nav><main>
<section class="intro"><p class="proposed">Flights booked. Hotels, trains and dinners from Sat Dec 5 on are ready to book soon, not booked yet.</p><p>The Paris week is unchanged. Then five extra days: a night facing Mont-Saint-Michel, a night in Bayeux by the D-Day coast, and three nights in London with the birthday dinner on Mon Dec 7. Same rhythm: slow mornings, one light anchor a day, one proper dinner.</p>
<p>Weather: Normandy and London in December are cool, grey and damp, highs around 45–48 °F, windy on the coast; sunset ~4:55 PM in Normandy and ~3:50 PM in London. Pack layers, a waterproof jacket and good shoes.</p>
<p><strong>Flights (booked, United Polaris via Chicago):</strong> Out Sat Nov 28: UA5867 Traverse City 2:18 PM → O'Hare 2:55 PM, then UA987 O'Hare 6:45 PM → Paris CDG 9:55 AM Nov 29. Home Thu Dec 10 (open-jaw from London Heathrow T2): UA928 1:35 PM → O'Hare 4:55 PM (seats 4D/5F), then UA2304 O'Hare 7:45 PM → Traverse City 9:59 PM (First, 2E/2F).</p></section>
{days}
<section class="day" id="open"><p class="proposed">Ready to book</p><h2>Open items</h2><table class="chk"><tr><th>Item</th><th>What</th></tr>{op}</table></section>
<section class="day notes"><h2>Dining notes</h2><h3>Jenny: pescatarian, shellfish allergy</h3><blockquote><strong>Je suis allergique aux fruits de mer et crustacés. Je mange du poisson mais pas de fruits de mer.</strong><br><em>In London: "Pescatarian, with a shellfish allergy — no prawns, crab, lobster, scallops, mussels or oysters, and no shellfish stock."</em></blockquote>
<p>Normandy menus lean on oysters, mussels and scallops; ask for the fish of the day (sole, bar, cabillaud, saumon). Jenny: Crémant or Champagne in France, English sparkling in London. Clark: bold reds, an Old Fashioned in the hotel bar, crème brûlée when it appears.</p></section>
<section class="credits"><h2>Photo credits</h2><ul>{cred}</ul></section></main><footer>Bon voyage · Paris, Normandy &amp; London 2026</footer></body></html>'''
open('index.html','w').write(page)
