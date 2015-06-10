import csv


def get_all_inspections():
    csv_path = './static/failed_inspections.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    return list(csv_obj)

def get_school_list():
    inspections = get_all_inspections()
    school_names = set([i['aka_name'] for i in inspections])
    schools = []

    for akaname in school_names:
        sch_inspections = [r for r in inspections if r['aka_name'] == akaname]
        school = sch_inspections[0]
        school['inspection_date_list'] = [i['inspection_date'] for i in sch_inspections]
        school['inspection_count'] = len(sch_inspections)
        schools.append(school)

    return schools



def get_inspections_list_for_school(schoolid):
    inspections = get_all_inspections()
    xlist = []
    for row in inspections:
        if row['aka_name'] == schoolid:
            row['parsed_violations'] = parse_violations(row['violations'])
            xlist.append(row)

    return xlist


def parse_violations(txt):
    violations = []
    for v in txt.split('|'):
        d = {}
        d['comments'] = v.split('- Comments:')[1]
        t = v.split('- Comments:')[0].strip()
        d['number'] = t.split('.')[0].strip()
        d['category'] = '.'.join(t.split('.')[1:]).strip()

        violations.append(d)

    return violations

    # headlist = []
    # for row in mylist:
    #     head = row.split("- Comments:")
    #     headlist.append(head)


#why the heck can't i get it to also separate by comments? the list wont break?









