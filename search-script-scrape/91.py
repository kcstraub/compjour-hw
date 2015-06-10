import shutil
import requests
url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2014_sqf_csv.zip'
resp = requests.get(url)
# save to hard drive
f = open("/tmp/frisks.zip", "wb")
f.write(resp.content)
f.close()

shutil.unpack_archive("/tmp/frisks.zip", "/tmp")

rows = open("/tmp/2014.csv").readlines()
totes = 0
for r in rows:
    totes += 1
print(totes)
