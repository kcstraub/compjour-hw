import csv


def get_school_list():
    csv_path = './static/Schools_Failed.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

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


def parse_violations(txt):
    mylist = []
    mylist.append(txt.split('|'))
    return mylist[0]
    headlist = []
    for row in mylist:
        head = row.split("- Comments:")
        headlist.append(head)
        

#why the heck can't i get it to also separate by comments? the list wont break?




    
    
    


