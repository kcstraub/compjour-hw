import json 
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())
    
def myloo(intl_data):
    return intl_data[1]

ilist = sorted(intl_data, key = myloo, reverse = True)[:10]

ecount = 0 
for e in ilist:
    ecount += e[1]
    print(e[0], ",", e[1])

jcount = sum([e[1] for e in ilist])

dcount = 0
for d in intl_data:
    dcount += d[1]

icount = sum([d[1] for d in intl_data])

final_count = icount - jcount

print("Others", ",", final_count)