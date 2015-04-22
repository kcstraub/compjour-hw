import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
print('A.', data['results'][0]['formatted_address'])
print('B.', data['status'])
print('C.', data['results'][0]['geometry']['location_type'])
print('D.', data['results'][0]['geometry']['location']['lat'])
print('E.', data['results'][0]['geometry']['viewport']['southwest']['lng'])
print('F.', data['results'][0]['address_components'][0]['long_name'], ', ', data['results'][0]['address_components'][1]['long_name'])
