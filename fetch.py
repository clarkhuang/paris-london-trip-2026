import json,urllib.request,urllib.parse,sys
UA={'User-Agent':'GrokBot-ParisTrip/1.0 (personal itinerary)'}
Q={'omaha':'Omaha Beach Normandy'}
out={}
for k,q in Q.items():
  u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrsearch':q+' filetype:bitmap','gsrnamespace':6,'gsrlimit':5,'prop':'imageinfo','iiprop':'url|extmetadata|size','iiurlwidth':1200})
  d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
  pages=sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',9))
  for p in pages:
    ii=p['imageinfo'][0]; m=ii['extmetadata']
    if ii['width']<ii['height']*1.1: continue
    lic=m.get('LicenseShortName',{}).get('value','')
    if not any(x in lic for x in ['CC','Public','PD']): continue
    import re
    art=re.sub('<[^>]+>','',m.get('Artist',{}).get('value','')).strip()
    data=urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=UA)).read()
    open(f'/workspace/paris-london-site/img/{k}.src','wb').write(data)
    out[k]={'title':p['title'],'page':ii['descriptionurl'],'artist':art[:80],'license':lic}
    print(k,p['title'],lic,art[:40]);break
json.dump(out,open('/workspace/paris-london-site/img/credits_omaha.json','w'),indent=1)
