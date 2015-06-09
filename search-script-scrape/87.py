from lxml import html
import requests
response = requests.get('https://nfdc.faa.gov/xwiki/bin/view/NFDC/Construction+Notices')
doc = html.fromstring(response.text)
link = doc.cssselect('.wikiattachmentlink') 
print(len(link))