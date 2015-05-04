import requests
url = "https://data.usajobs.gov/api/jobs"

def get_total_jobs(place):
    atts = {"Country": place, "NumberOfJobs": 1}
    resp = requests.get(url, params = atts)
    data = resp.json()
    print("%s has %s job listings." % (place, data['TotalJobs']))
    return int(data["TotalJobs"])


countries = ["China", "South Africa", "Tajikistan"]
total = 0
for country in countries:
    total += get_total_jobs(country)

print("Together, they have", total, "total job listings.")