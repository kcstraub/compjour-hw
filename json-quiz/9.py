import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/instagram-aaron-schock.json'
data = json.loads(requests.get(data_url).text)

items = data['data']


ix = len([i for i in items if i['type'] == 'image'])
vx = len([i for i in items if i['type'] == 'video'])
print("A.", "%s|%s" % (ix, vx))


from operator import itemgetter
filter_dict = {}
for i in items:
    fname = i['filter']
    if filter_dict.get(fname):
        filter_dict[fname] += 1
    else:
        filter_dict[fname] = 1



filter_list = list(filter_dict.items())

top3 = sorted(filter_list, key = itemgetter(1), reverse = True)[0:3]
top3_strs = []
for t in top3:
    x = str(t[0]) + ':' + str(t[1])
    top3_strs.append(x)


print("B.", '|'.join(top3_strs))


located_items = [i for i in items if i['location']]
geocoded_items = [i for i in located_items if i['location'].get('latitude')]
print("C.", len(geocoded_items))


capitol_items = [i for i in geocoded_items if i['location'].get('name') == 'United States Capitol']
print("D.", len(capitol_items))


from collections import Counter
locations = [i['location']['name'] for i in located_items if i['location'].get('name')]
top_locs = Counter(locations).most_common(3)
top_loc_strs = ["%s:%s" % t for t in top_locs]

print("E.", '|'.join(top_loc_strs))


cap = capitol_items[0]
cap_lat = cap['location']['latitude']
cap_lng = cap['location']['longitude']

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 
    return c * r

def distance_to_cap(item):
    lng = item['location']['longitude']
    lat = item['location']['latitude']
    return haversine(lng, lat, cap_lng, cap_lat)

i = max(geocoded_items, key = distance_to_cap )
print('F.', i['location']['name'])

def sum_likes_and_comments(item):
    return item['comments']['count'] + item['likes']['count']

i = max(items, key = sum_likes_and_comments)
print('G.', '|'.join([i['caption']['text'][0:19],
  i['images']['thumbnail']['url'],
  str(i['likes']['count']),
  str(i['comments']['count'])
]))

from operator import itemgetter
y = max(items, key = itemgetter('created_time'))
x = min(items, key = itemgetter('created_time'))
span_seconds = int(y['created_time']) - int(x['created_time'])
span_days = span_seconds / (60 * 60 * 24)
print('H.', round(span_days))

span_weeks = span_seconds / (7 * 60 * 60 * 24)
print('I.', round(len(items) / span_weeks, 1))


prev_time = int(items[-1]['created_time'])
max_diff = 0
for i in reversed(items):

    this_time = int(i['created_time'])
    max_diff = max(max_diff, this_time - prev_time)
    prev_time = this_time

max_days = round(max_diff / (60 * 60 * 24))
print('J.', max_days)


pv = int(items[-1]['comments']['count'])
mdiff = 0
for i in reversed(items):

    nv = int(i['comments']['count'])
    mdiff = max(mdiff, abs(nv - pv))
    pv = nv

print('K.', mdiff)


import time
x = int(items[0]['created_time'])
timeobj = time.localtime(x)
print('L.', timeobj.tm_mon)

import time
from collections import Counter
def footime(item):
    s = int(item['created_time'])
    return time.localtime(s)

w = [footime(i).tm_wday for i in items]
ct = Counter(w)
weekend_count = ct[5] + ct[6]
print("M.", round(weekend_count / len(items), 2))


dayslist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
d = ct.most_common(1)[0]
dayname = dayslist[d[0]]
dpct = round(d[1] / len(items), 2)
print("N.", '%s|%s' % (dayname, dpct))