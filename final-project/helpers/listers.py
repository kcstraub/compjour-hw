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
        d['number'] = (t.split('.')[0].strip())
        d['category'] = '.'.join(t.split('.')[1:]).strip()

        violations.append(d)

    return violations

def calculate_pie_chart():
    return [['Failed_Times', 'Schools'], ['One Failed Inspection', 328], ['Two Failed Inspections', 174], ['Three Failed Inspections', 78], ['4+ Failed Inspections', 49]]


def pull_worst_performers():
    inspections = get_all_inspections()
    school_names = set([i['aka_name'] for i in inspections])
    schools = []

    for akaname in school_names:
        sch_inspections = [r for r in inspections if r['aka_name'] == akaname]
        school = sch_inspections[0]
        school['inspection_date_list'] = [i['inspection_date'] for i in sch_inspections]
        school['inspection_count'] = len(sch_inspections)
        schools.append(school)
        if school['inspection_count'] == 6 or school['inspection_count'] == 7:
            return (school['aka_name'], ", ", school['inspection_count'])

# I can't seem to get the following function to output in a list! If I could, I would then plug those into a neat bar 
# chart and chart the worst schools (see the "calculate bar chart" below).... or I even would like a way to just input this function to html text...

def calculate_bar_chart():
    return [['School Name', 'Number of Failed Inspections'], ["ANTON DVORAK ELEMENTARY", 7], ['CICS LONGWOOD', 6], ['HENRY O. TANNER ELEMENTARY', 6], ['NIXON ELEMENTARY', 6], ['TABERNACLE CHRISTIAN ACADEMY', 6], ['WILLAM TAFT HIGH SCHOOL', 6]]










