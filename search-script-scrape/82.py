import requests 
from lxml import html
response = requests.get('http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm070461.htm')
doc = html.fromstring(response.text)

row1 = doc.cssselect('tr')[8]
cell1 = row1.cssselect('td')[1]

row2 = doc.cssselect('tr')[9]
cell2 = row2.cssselect('td')[1]

row3 = doc.cssselect('tr')[10]
cell3 = row3.cssselect('td')[1]

mylist = (cell1.text, cell2.text, cell3.text)

intlist = int(mylist)

print(sum(intlist))
