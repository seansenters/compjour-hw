import requests

import json

durl = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'

data = json.loads(requests.get(durl).text)

quakes = data['features']

print('A.', data['metadata']['title'])
('A.', u'USGS Significant Earthquakes, Past Month')

print('B.', data['metadata']['count'])
('B.', 6)

print('C.', max([q['properties']['mag'] for q in quakes]))
('C.', 7.5)

x = 0

for q in quakes:
    if q['properties']['tsunami'] > 0:
        x += 1

print("D.", x)
('D.', 3)

def get_mag(quake):
    return quake['properties']['mag']


q = min(quakes, key = get_mag)

print("E.", q['properties']['title'])
('E.', u'M 3.6 - 1km NNW of San Ramon, California')

def get_felt(quake):
    return quake['properties']['felt']


q = max(quakes, key = get_felt)

print("F.", q['properties']['title'])
('F.', u'M 3.6 - 1km NNW of San Ramon, California')

import time

qsecs = [q['properties']['time'] / 1000 for q in quakes]

qsecs = sorted(qsecs, reverse = True)

tsec = qsecs[0]

timeobj = time.gmtime(tsec)

print('G.', time.strftime('%Y-%m-%d %H:%M', timeobj))
('G.', '2015-04-02 07:06')

lsec = qsecs[5]

timeobj = time.gmtime(lsec)

print('H.', time.strftime('%A %B %d', timeobj))
('H.', 'Wednesday March 18')

tobjs = [time.gmtime(s) for s in qsecs]

wdays = [s.tm_wday for s in tobjs]

x = [d for d in wdays if d in range (0, 6)]

print ('I.', len(x))
('I.', 5)

tobjs = [time.gmtime(s) for s in qsecs]

hours = [s.tm_hour for s in tobjs]

x = [h for h in hours if h in range (5, 9)]

print ('J.', len(x))
('J.', 3)

from math import radians, cos, sin, asin, sqrt

def haversine (lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map( radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat /2) ** 2 + cos(lat1) * cos(lat2) *sin(dlon/2) ** 2
    c = 2 * asin (sqrt(a))
    r = 6371
    return c * r


def distance_from_stanford(quake):
    stanford_lng = -122.166
    stanford_lat = 37.424
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, stanford_lng, stanford_lat)


q = max(quakes, key = distance_from_stanford)

print ('K.', q['properties']['title'])
('K.', u'M 7.5 - 56km SE of Kokopo, Papua New Guinea')

def distance_from_paris(quake):
    paris_lng = 2.351
    paris_lat = 48.857
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine (lng, lat, paris_lng, paris_lat)


q = max(quakes, key = distance_from_paris)

print ('L.', q['properties']['title'])
('L.', u'M 6.5 - 99km ENE of Hihifo, Tonga')

basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'

markers_str = 'markers=color:orange'

for q in quakes:
    coords = q['geometry']['coordinates']
    lng = str(coords[0])
    lat = str(coords[1])
    s = '%7C' + lat + ',' + lng
    markers_str += s
    

print('M.', basemap_url + '&' + markers_str)
('M.', 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400&markers=color:orange%7C37.792,-121.9868333%7C-15.5149,-172.9402%7C-15.388,-172.9038%7C-4.7632,152.5606%7C-18.3534,-69.1663%7C-36.0967,-73.6259')

COME BACK TO N
