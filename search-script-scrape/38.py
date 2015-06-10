
import requests
import json
response = requests.get('https://analytics.usa.gov/data/live/top-pages-realtime.json')
data = response.json()
print(data['data'][0]['page'])
