import requests
import json
durl = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(durl).text)
quakes = data['features']

print("A.", data['metadata']['title'])
print("B.", len(quakes))

print("C.", max([q['properties']['mag'] for q in quakes]))

x = 0 
for t in quakes:
	if t['properties']['tsunami'] == 1:
		x += 1
print("D.", x)	

#from operator import itemgetter
#y = sorted(quakes, key = itemgetter(['properties']['mag']))
#x = y[0]
#print("E.", x['title'])

def get_mag(quake):
	return quake['properties']['mag']

q = min(quakes, key = get_mag)
print("E.", q['properties']['title'])

def get_mag(quake):
	return quake['properties']['felt']

q = max(quakes, key = get_mag)
print("F.", q['properties']['title'])

import time 

qsecs = [q['properties']['time'] / 1000 for q in quakes]
qsecs = sorted(qsecs, reverse = True)
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
print('G.', time.strftime('%Y-%m-%d %H:%M', timeobj))

import time 
qsecs = [q['properties']['time'] / 1000 for q in quakes]
qsecs = sorted(qsecs)
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
print("H.", time.strftime('%A, %B %d', timeobj)) 

import time 
qsecs = [q['properties']['time'] / 1000 for q in quakes]
tobjs = [time.gmtime(s) for s in qsecs]
wdays = [s.tm_wday for s in tobjs]
x = [d for d in wdays for d in range(0, 6)]
print('I.', len(x))

hrs = [s.tm_hour for s in tobjs]
print('J.', len([h for h in hrs if h in range(5,9)]))

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2 
	c = 2 * asin(sqrt(a))
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
print('K.', q['properties']['title'])

def d_paris(quake):
	paris_lng = -0.8655079
	paris_lat = 44.562918
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, paris_lng, paris_lat)

q = max(quakes, key = d_paris)
print("L.", q['properties']['title'])

basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500X400'
markers_str = 'markers=color:orange'
for q in quakes:
	coords = q['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	markers_str += s

print('M.', basemap_url + '&' + markers_str)

orange_str = 'markers=color:orange'
red_str = 'markers=color:red'

for q in quakes:
		coords = q['geometry']['coordinates']
		lng = str(coords[0])
		lat = str(coords[1])
		s = '%7C' + lat + ',' + lng

		if q['properties']['mag'] >= 6:
			red_str += s
		else:
			orange_str += s
print('N.', basemap_url + '&' + orange_str + '&' + red_str)

