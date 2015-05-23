import json
import requests
import os
from datetime import datetime
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, "w")
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']

def cleanmoney(val):
    x = val.replace("$", "").replace(",","")
    return float(x)

over_90k = []

for job in jobs:
    if cleanmoney(job['SalaryMin']) > 90000:
        over_90k.append(job)


collection_date = datetime.strptime(jdata['date_collected'], '%Y-%m-%dT%H:%M:%S')

def daysonlist(job):
    postdate = datetime.strptime(job['StartDate'], '%m/%d/%Y')
    return (collection_date - postdate).days

for job in sorted(over_90k, key = daysonlist): 
    days = daysonlist(job)
    if days < 5:
        print('%s,%s,%s' % (job['JobTitle'], days, job['ApplyOnlineURL']))
