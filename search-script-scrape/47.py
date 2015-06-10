import requests
from lxml import html
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect('a') if 'pinterest.com' in str(a.attrib.get('href'))]
print(len(pinlinks))