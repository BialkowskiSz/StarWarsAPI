#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/vehicles'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

# List of ground vehicles, not hardcoded
vehicles = ["tank", "speeder", "wheeled", "walker"]
fastest = data['results'][0]
# 39 = 4 loops
for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            for j in range(len(vehicles)):
                if vehicles[j] in data['results'][i]['vehicle_class'] and data['results'][i]['vehicle_class'] != "airspeeder":
                    if int(data['results'][i]['max_atmosphering_speed']) > int(fastest['max_atmosphering_speed']):
                        fastest = data['results'][i]
                    break
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

print("{} is the fastest ground vehicle with a speed of {}".format(fastest['model'], fastest['max_atmosphering_speed'] ))
