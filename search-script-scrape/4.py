from lxml import html
import requests
response = requests.get('https://www.usajobs.gov/Search?Keyword=librarian&Location=&search=Search&AutoCompleteSelected=False')
doc = html.fromstring(response.text)
link = doc.cssselect('span.pageset') [2]
print(link.text)