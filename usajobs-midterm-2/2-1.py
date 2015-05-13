import json
import os
import requests
BASE_JOBS_URL = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/CountryCode.json"
cdata = requests.get(CODES_URL).json()
mylist = []
for d in cdata['CountryCodes']:
    if d['Code'] != 'US' and d['Value'] != 'Undefined':
        cname = d['Value']
        print("Getting:", cname)
        atts = {'Country': cname, 'NumberOfJobs': 1}
        resp = requests.get(BASE_JOBS_URL, params = atts)
        data = resp.json()
        jobcount = int(data['TotalJobs'])
        mylist.append([cname, jobcount])

os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/intl-jobcount.json", "w")
f.write(json.dumps(mylist, indent = 2))
f.close()
