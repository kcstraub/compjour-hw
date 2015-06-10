import json
import requests
data_url = "https://data.cityofchicago.org/resource/n379-5uzu.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
len(data)