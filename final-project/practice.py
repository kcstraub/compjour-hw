import csv

def get_inspections_list(schoolid):
    csv_path2 = './static/Failed_Schools_2.csv'
    csv_file2 = open(csv_path2, 'r')
    csv_obj2 = csv.DictReader(csv_file2)
    inspections = list(csv_obj2)
    xlist = []
    for row in inspections:
        if row['AKA_Name'] == schoolid:
            row['parsed_violations'] = parse_violations(row['Violations'])
            xlist.append(row) 

    return xlist

mylist = get_inspections_list()
highest_offenders = []
for row in mylist:
    highest_offenders.append([row.AKA_Name, row.Failed_Times])
    print(highest_offenders)