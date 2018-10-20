import urllib.request,json
with urllib.request.urlopen("http://data.unhcr.org/api/population/settlements.json?instance_id=liberia") as url:
    data = json.loads(url.read().decode())
    print(data)
