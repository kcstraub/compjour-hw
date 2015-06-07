from lxml import html
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc&ext_location=&ext_bbox=&ext_prev_extent=-213.046875%2C-22.593726063929296%2C-47.109375%2C75.32002523220804')
doc = html.fromstring(response.text)
link = doc.cssselect('.dataset-heading a') [0] 
print(link.text)
