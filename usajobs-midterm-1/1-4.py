import requests
url = "https://data.usajobs.gov/api/jobs"

def get_total_jobs(state_name):
    atts = {"CountrySubdivision": state_name, "NumberOfJobs": 1}
    resp = requests.get(url, params = atts)
    data = resp.json()
    return int(data["TotalJobs"])

states = ["California", "New York", "Maryland", "Florida"]

d = {}

d = dict([(state, get_total_jobs(state)) for state in states])