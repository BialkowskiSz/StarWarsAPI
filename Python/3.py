#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/vehicles'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))

flying = ["starfighter", "airspeeder", "space", "gunship", "cruiser", "solar", "battleship", "cloud", "fighter"]
vehicles = []

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            for j in range(len(flying)):
                if flying[j] in data['results'][i]['vehicle_class']:
                    vehicles.append(data['results'][i])
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

# Put all capacitys in list for sorting
capacitys = []
for i in range(len(vehicles)):
    try:
        capacitys.append(int(vehicles[i]['cargo_capacity']))
    except:
        pass

capacitys.sort()
# Print capacitys of none
for i in range(len(vehicles)):
    if vehicles[i]['cargo_capacity'] == "none":
        print(vehicles[i]['name'] + " " + vehicles[i]['cargo_capacity'])

# Print capacitys unknown
for i in range(len(vehicles)):
    if vehicles[i]['cargo_capacity'] == "unknown":
        print(vehicles[i]['name'] + " " + vehicles[i]['cargo_capacity'])

# Print sorted capacitys
for i in range(len(capacitys)):
    for j in range(len(vehicles)):
        try:
            if capacitys[i] == int(vehicles[j]['cargo_capacity']):
                print(vehicles[j]['name'] + " " + vehicles[j]['cargo_capacity'])
                vehicles.pop(j)
                break
        except:
            pass
