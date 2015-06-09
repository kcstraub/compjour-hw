import requests 
from lxml import html
response = requests.get('http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::')
doc = html.fromstring(response.text)
first = doc.cssselect('td a') [14:24]

mylist = []
for f in first:
    mylist.append((f).text)

newlist = (([s.strip('*') for s in mylist]))

intlist = (int(x) for x in newlist)

print(sum(intlist))


