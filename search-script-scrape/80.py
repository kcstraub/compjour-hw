import shutil
import requests
url = "http://www.ssa.gov/OACT/babynames/state/namesbystate.zip"
resp = requests.get(url)
f = open("/tmp/ssastates.zip", "wb")
f.write(resp.content)
f.close

shutil.unpack_archive("/tmp/ssastates.zip", "/tmp")

rows = open("/tmp/CO.TXT").readlines()
totes = 0
for r in rows:
    if "Odin" in r:
        totes += int(r.split(",")[4])
print(totes)
