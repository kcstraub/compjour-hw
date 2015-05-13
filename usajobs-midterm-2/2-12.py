import json
import requests
import os
CA_FILE = "data-hold/california.json"
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching a remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs.california-all.json")
    f = open(CA_FILE, "w")
    f.write = (resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
    x = val.replace("$", "").replace(",","")
    return float(x)

def cleansalarymax(job):
    return cleanmoney(job['SalaryMax'])

sortedjobs = sorted(jobs, key = cleansalarymax, reverse = True)

def diff_val(job):
    return cleanmoney(job['SalaryMax']) - cleanmoney(job['SalaryMin'])

under_100k = []

for job in sortedjobs:
    if cleanmoney(job['SalaryMax']) < 100000:
        under_100k.append(job)

max_under_100k = sorted(under_100k, key = diff_val, reverse = True)

new_job = max_under_100k[0]

print(new_job['JobTitle'], ",", cleanmoney(new_job['SalaryMin']), ",", cleanmoney(new_job['SalaryMax']))
