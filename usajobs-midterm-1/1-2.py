import requests
url = "https://data.usajobs.gov/api/jobs"
state_name = "Alaska"
atts = {"CountrySubdivision": state_name, "NumberOfJobs": 1}
resp = requests.get(url, params = atts)
data = resp.json()
alaska_jobs = data['TotalJobs']
print("%s has %s job listings." % (state_name, data['TotalJobs']))

import requests
url = "https://data.usajobs.gov/api/jobs"
state_name = "Hawaii"
atts = {"CountrySubdivision": state_name, "NumberOfJobs": 1}
resp = requests.get(url, params = atts)
data = resp.json()
hawaii_jobs = data['TotalJobs']
print("%s has %s job listings." % (state_name, data['TotalJobs']))

print("Together, they have", int(alaska_jobs)+int(hawaii_jobs), "total jobs listings.")
