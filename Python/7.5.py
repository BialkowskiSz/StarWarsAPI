#!/usr/bin/python3

from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/films'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

species = {}
# PRINTS SECOND MOST FEATURED SPECIES IN ALL THE MOVIES

for i in range(data['count']):
    try:
        for j in range(len(data['results'][i]['species'])):
            if data['results'][i]['species'][j] in species:
                species[data['results'][i]['species'][j]] += 1
            else:
                species[data['results'][i]['species'][j]] = 1
    except:
        pass

highest = list(set(species.values()))
highest = highest[len(highest)-2]

for key, value in species.items():
    if value == highest:
        url = key
        req = Request(url, None, {
            'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        print(data['name'])
