import csv
import requests
CSVURL = 'https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv'
response = requests.get(CSVURL)
# f = open("fy15_federal-state_summaries.csv", "w")
# f.write(response.text)
# f.close()
data = csv.DictReader(open("fy15_federal-state_summaries.csv"))
rows = list(data)
len(rows)
print (rows)