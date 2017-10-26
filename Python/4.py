#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/people'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

starships = []
urls = []
counter = 0

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            if data['results'][i]['name'] == "Luke Skywalker" or data['results'][i]['name'] == "Darth Vader":
               urls.append(data['results'][i]['url'])
        except:
            break
    # Check for next page
    if data['next'] is None or len(urls) == 2:
        break
    # Load next page
    url = data['next']
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req).read().decode("utf-8"))

url = 'https://swapi.co/api/starships'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

for i in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            if urls[0] in data['results'][i]['pilots'] and urls[1] in data['results'][i]['pilots']:
                counter += 1
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

print(counter)
