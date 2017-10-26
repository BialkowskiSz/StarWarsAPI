#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/people'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

most = []
most.append(data['results'][0])

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            if len(most[0]['films']) < len(data['results'][i]['films']):
                most.pop()
                most.append(data['results'][i])
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


url = 'https://swapi.co/api/films'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

latest = earliest = data['results'][0]['release_date']

for i in range(len(most[0]['films'])):
    for j in range(data['count']):
        if int(latest[:4:]) < int(data['results'][j]['release_date'][:4:]):
            latest = data['results'][j]['release_date']
        if int(earliest[:4:]) > int(data['results'][j]['release_date'][:4:]):
            earliest = data['results'][j]['release_date']

print("{}s Earliest appearance: {}\n{}s Latest appearance: {}".format(most[0]['name'], earliest, most[0]['name'], latest))
