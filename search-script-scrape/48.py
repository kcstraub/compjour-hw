import requests
import csv
url = "https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text

f = open("/tmp/salaries2014.csv", "w")
f.write(txt)
f.close()

f = open("/tmp/salaries2014.csv", "r")
rows = list(csv.DictReader(f))
totes = 0
for r in rows:
    salval = float(r['Salary'].replace('$', ''))
    totes += salval

print(totes)

urll = "https://open.whitehouse.gov/api/views/rcp4-3y7g/rows.csv?accessType=DOWNLOAD"
txtt = requests.get(urll).text

f = open("/tmp/salaries2010.csv", "w")
f.write(txtt)
f.close()

f = open("/tmp/salaries2010.csv", "r")
rows = list(csv.DictReader(f))
totess = 0
for r in rows:
    salval = float(r['Salary'].replace('$', ''))
    totess += salval

print(totess)

diff = totess - totes
print(diff)
