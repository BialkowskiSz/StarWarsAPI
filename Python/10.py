#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/films'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

producer = {}

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            if data['results'][i]['producer'] in producer:
                producer[data['results'][i]['producer']] += 1
            else:
                producer[data['results'][i]['producer']] = 1
        except:
            break
    # Check for next page
    if data['next'] is None:
        break
    # Load next page
    url = data['next']
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    data = loads(urlopen(req).read().decode("utf-8"))

producers = {}
highest = 0

for key, value in producer.items():
    temp = key.split(', ')
    for i in range(len(temp)):
        if temp[i] in producers:
            producers[temp[i]] += producer[key]
        else:
            producers[temp[i]] = producer[key]

for key, value in producers.items():
    if value > highest:
        highest = value

for key, value in producers.items():
    if value == highest:
        print("{} has produced {} movies, the most out of all the producers.".format(key, value))
        break
