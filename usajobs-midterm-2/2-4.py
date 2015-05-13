import json 
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

sorted_dd = sorted(domestic_data)

filtered_dd = []
for s in sorted_dd:
    if s[1] < 100:
        y = (s[0], s[1])
        filtered_dd.append(y)
        print(s[0],",",s[1])