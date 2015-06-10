import csv
import requests
CSVURL = "http://www.fda.gov/downloads/ICECI/Inspections/UCM346093.csv"
response = requests.get(CSVURL)
f = open("UCM346093.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("UCM346093.csv"))
rows = list(data)