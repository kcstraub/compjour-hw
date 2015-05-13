import requests
BASE_JOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_JOBS_URL, params = {"CountrySubdivision": 'California', "NumberOfJobs": 250})
data = resp.json()

mydict = {org_name: 0}

for job in data['JobData']:
    org_name = job["OrganizationName"]
    mydict[org_name] += 1
    print(mydict)