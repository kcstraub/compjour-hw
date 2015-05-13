import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def myloo(intl_data):
    return intl_data[1]
ilist = sorted(intl_data, key = myloo)

filtered_intld = []
for s in ilist:
    if s[1] > 10:
        y = (s[0], s[1])
        filtered_intld.append(y)
        print(s[0],",",s[1])