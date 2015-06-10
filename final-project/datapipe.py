import csv
import requests
import os

DATA_DIR = './datastash'
ORIGINAL_DATA_URL = 'https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD'


# saves file to datastash/original-data.csv
def get_original_data():
    print("Downloading from", ORIGINAL_DATA_URL)
    resp = requests.get(ORIGINAL_DATA_URL)
    fname = os.path.join(DATA_DIR, 'original-data.csv')
    print("Saving to", fname)
    f = open(fname, 'w')
    f.write(resp.text)
    f.close()




def justdoit():
    print("filtering")
    filter_data()
    print("pushing")
    push_data()
    print("yea!")

# creates "datastash/schools.csv"
# filters for school and for rows that have x,y
def filter_data():
    data_fname = os.path.join(DATA_DIR, 'original-data.csv')
    f = open(data_fname)
    filteredrows = []
    rows = list(csv.DictReader(f))
    for r in rows:
        if( r['Facility Type'] == 'School' and
            r['Latitude'].strip() != '' and
            r['Longitude'].strip() != '' and
            r['AKA Name'].strip() != '' and
            r['AKA Name'] == r['AKA Name'].replace("/", " ") and
            'Fail' in r['Results']
        ):
            filteredrows.append(r)

    filtered_fname = os.path.join(DATA_DIR, 'filtered-data.csv')
    o = open(filtered_fname, 'w')
    writer = csv.DictWriter(o, fieldnames = filteredrows[0].keys())
    writer.writeheader()
    writer.writerows(filteredrows)
    o.close()


# just pushes to
def push_data():
    filtered_fname = os.path.join(DATA_DIR, 'filtered-data.csv')
    txt = open(filtered_fname).readlines()
    # fix up the headers
    txt[0] = txt[0].lower().replace(' ', '_').replace('#', 'number')

    final_fname = "./static/failed_inspections.csv"
    f = open(final_fname, "w")
    f.writelines(txt)
    f.close()


# from collections import defaultdict
# def group_data():
#     filtered_fname = os.path.join(DATA_DIR, 'filtered-data.csv')
#     f = open(filtered_fname)
#     dates = defaultdict(list)
#     rows = list(csv.DictReader(f))
#     for r in rows:
#         dates[r['AKA Name']].append(r['Inspection Date'])






