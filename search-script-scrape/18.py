import csv
import requests
CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
response = requests.get(CSVURL)
f = open("legislators.csv", "w")
f.write(response.text.encode('ascii', 'ignore').decode('ascii'))
f.close()
data = csv.DictReader(open("legislators.csv"))
rows = list(data)
print(len([i for i in rows if i['twitter_id'] and i['in_office'] == '1']))