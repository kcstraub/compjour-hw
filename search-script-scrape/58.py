from lxml import html
import requests
response = requests.get("https://www.nsa.gov/research/publications/")
doc = html.fromstring(response.text)
link = doc.cssselect('.dataTable') [0]
row = link.cssselect('tr')
length = int((len(row)))
print(length - 1)
