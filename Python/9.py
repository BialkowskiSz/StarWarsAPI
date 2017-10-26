#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/starships'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            for z in range(len(data['results'][i]['pilots'])):
                url = data['results'][i]['pilots'][z]
                req = Request(url, None, {
                    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
                })
                data_in = loads(urlopen(req).read().decode("utf-8"))
                print("{} piloted the {} which costs: {}.".format(data_in['name'], data['results'][i]['name'], data['results'][i]['cost_in_credits']))
        except:
            break
    # Check for next page
    if data['next'] is None:
        break
    # Load next page
    url = data['next']
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    data
    data = loads(urlopen(req).read().decode("utf-8"))
