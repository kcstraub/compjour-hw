from lxml import html
import requests
response = requests.get("http://catalog.data.gov/dataset?q=university&sort=score+desc%2C+name+asc")
doc = html.fromstring(response.text)
link = doc.cssselect('.new-results') [0]
print(link.text)