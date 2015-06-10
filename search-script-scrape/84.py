import json
import requests
data_url = "https://www.federalregister.gov/api/v1/articles?conditions%5Bpublication_date%5D%5Bis%5D=06%2F09%2F2015&conditions%5Btype%5D=NOTICE"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
print(data["count"])