from lxml import html
import requests
response = requests.get("https://www.us-cert.gov/ncas/alerts")
doc = html.fromstring(response.text)
link = doc.cssselect('.document_id') 
print(len(link))
