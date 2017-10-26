#!/usr/bin/python3

from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/films'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

species = {}


# First movie
for j in range(len(data['results'][0]['characters'])):
    url = data['results'][0]['characters'][j]
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data_in = loads(urlopen(req).read().decode("utf-8"))
    if data_in['species'][0] in species:
        species[data_in['species'][0]] += 1
    else:
        species[data_in['species'][0]] = 1

highest = []
for key, value in species.items():
    highest.append(value)

highest.sort()
for key, value in species.items():
    if highest[len(highest)-2] == value:
        url = key
        req = Request(url, None, {
            'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data_in = loads(urlopen(req).read().decode("utf-8"))
        print(data_in['name'])
