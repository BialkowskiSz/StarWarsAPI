#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/people'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

most = {}

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            if data['results'][i]['species'][0] in most:
                most[data['results'][i]['species'][0]] += 1
            else:
                most[data['results'][i]['species'][0]] = 1
        except:
            break
    # Check for next page
    if data['next'] is None:
        break
    # Load next page
    url = data['next']
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req).read().decode("utf-8"))

highest = 0
for key, value in most.items():
    if value > highest:
        highest = value

for key, value in most.items():
    if value == highest:
        url = key
        req = Request(url, None, {
            'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        print(data['name'])

        url = data['homeworld']
        req = Request(url, None, {
            'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        print(data['name'])
