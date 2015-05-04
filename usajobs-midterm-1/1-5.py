import requests
url = "https://data.usajobs.gov/api/jobs"
states = ["California", "New York", "Maryland", "Florida"]
mylist = []

for state in states:
    atts = {"CountrySubdivision": state, "NumberOfJobs": 1}
    resp = requests.get(url, params = atts)
    data = resp.json()
    jobcount = resp.json()['TotalJobs']
    mylist.append([state, jobcount])
  
print(mylist)