import requests
import csv
url = "http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/2012Q4-detail.csv"
txt = requests.get(url).text

f = open("/tmp/expenditures.csv", "w")
f.write(txt)
f.close()

f = open("/tmp/expenditures.csv", "r")
rows = list(csv.DictReader(f))

totes = 0

for r in rows:
    if r['PAYEE'] == 'LOBAIR LLC':
        if r ['OFFICE'] == 'HON. AARON SCHOCK':
            totes += float(r['AMOUNT'].replace('$', ''))

print(totes)