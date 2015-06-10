import csv
import requests
CSVURL= "http://www.census.gov/quickfacts/download.php?fips=00,2622000&type=csv"
response = requests.get(CSVURL)
f = open("fips=00,2622000.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("fips=00,2622000.csv"))
rows = list(data)
print(rows)[6]