import json
import requests
data_url = 'http://congress.api.sunlightfoundation.com/bills?history.vetoed=true&sponsor_id=P000197&apikey=1b08f3ed3a9441939f82d87a6ba85a49'
response = requests.get(data_url)
text = response.text
data = json.loads(text)
print(data['count'])