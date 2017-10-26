#!/usr/bin/python3

from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/people'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

# Number of people using count value
print(data['count'])

# Number of people using iterative loop through pages
counter = 0
while True:
    for i in range(10):
        try:
            if data['results'][i] is not None:
                counter += 1
        except:
            break
    if data['next'] == None:
        break
    # Connect to next page
    url = data['next']
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req).read().decode("utf-8"))
print(counter)
