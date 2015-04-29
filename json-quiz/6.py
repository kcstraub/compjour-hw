import requests
import json
import os
data_url = "http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json"
tempfilename = "/tmp/congresslist.json"
if os.path.exists(tempfilename): 
	tfile = open(tempfilename, "r")
	j = tfile.read()
else:
	j = requests.get(data_url).text
	tfile = open(tempfilename, "w")
	tfile.write(j)

tfile.close()
accounts = json.loads(j)

print("A.", len(accounts[0:]))

x = 0
for a in accounts:
	if a['followers_count'] > 10000:
		x += 1
print("B.", x)

v = 0
for b in accounts:
	if b['verified'] == True:
		v += 1
print("C.", v)

counts = []
for a in accounts:
	counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]

print("D.", maxval)

status_counts = []
for a in accounts:
	status_counts.append(a['statuses_count'])
maxval = sorted(status_counts, reverse = True)[0]

print("E.", maxval)

from operator import itemgetter
y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
x = y[0]
print("F.", x['screen_name'], 'has', x['followers_count'], 'followers.')

print("I'm confused on G. for now, will get back to it later.")

total = list(accounts['followers_count'][0:])
print(total)
