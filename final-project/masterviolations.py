import csv
import json
csvfile = open('failed_inspections.csv', 'r')
all_failed = []
for row in csv.DictReader(csvfile):
    all_failed.append(row)

masterviolations = []
for row in all_failed:
    vx = [v.strip() for v in row['Violations'].split('|')]
    for v in vx:
        if v != '':
            txt, comments = v.split('- Comments:')
            num = txt.split('.')[0].strip()
            category = ' '.join(txt.split('.')[1:])
            d = {"number": int(num.strip()), "category": category.strip()}
            masterviolations.append(d)
 
viols = set((m['number'], m['category']) for m in masterviolations)
 
vfinal = []
for v in viols:
    
    vfinal.append(list(v))

f = open("masterviolations.json", "w")
j = json.dumps(vfinal, indent = 2)
f.write(j)
f.close()
 
