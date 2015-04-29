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

