import json
import requests
data_url = "http://api.data.gov:80/regulations/v3/docket.json?api_key=DEMO_KEY&docketId=APHIS-2014-0098"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
print(data["numberOfComments"])