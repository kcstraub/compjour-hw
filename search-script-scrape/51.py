from lxml import html
import requests
response = requests.get('http://www.supremecourt.gov/')
doc = html.fromstring(response.text)
link = doc.cssselect('div.recentdecisions a')[0]
print(link.text)
