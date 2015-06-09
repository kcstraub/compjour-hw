from lxml import html
import requests
response = requests.get('http://wildlife.faa.gov/database.aspx')
doc = html.fromstring(response.text)
link = doc.cssselect('span#ctl00_ContentPlaceHolder1_Lbl_Results') [0]
print(link.text)