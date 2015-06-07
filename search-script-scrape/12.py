from lxml import html
import requests
response = requests.get('http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/national_transportation_statistics/html/table_01_44.html')
doc = html.fromstring(response.text)
link = doc.cssselect('.cellright') [6]
print(link.text)