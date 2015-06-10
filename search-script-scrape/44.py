
import requests
import json
response = requests.get('https://analytics.usa.gov/data/live/realtime.json')
data = response.json()
print(data['data'][0]['active_visitors'])
