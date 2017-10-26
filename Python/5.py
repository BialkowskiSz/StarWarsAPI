#!/usr/bin/python3


from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.co/api/planets'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})
data = loads(urlopen(req).read().decode("utf-8"))
# print(data)

planets = []

for j in range(int(data['count']/10) + 1):
    for i in range(10):
        try:
            planets.append([data['results'][i]['name'],  data['results'][i]['diameter'], data['results'][i]['population']])
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

for i in range(len(planets)):
    if planets[i][2] == 'none' or planets[i][2] == 'unknown':
        planets[i][2] = 0
    if planets[i][1] == 'none' or planets[i][1] == 'unknown':
        planets[i][1] = 0
    if planets[i][2] == 'none' or planets[i][2] == 'unknown':
        planets[i][2] = 0

planets.sort(key=lambda x: int(x[1]))
names_diameter = [planets[i][0] for i in range(len(planets))]
for i in names_diameter:
    print(i)
print("\n\n****SECOND LIST****\n\n")
planets.sort(key=lambda x: int(x[2]))
names_population_rev = [planets[i][0] for i in range(len(planets))]
for i in reversed(names_population_rev):
    print(i)
