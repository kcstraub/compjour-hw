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