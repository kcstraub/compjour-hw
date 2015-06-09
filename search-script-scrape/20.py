from lxml import html
import requests
response = requests.get('https://www.osha.gov/pls/imis/establishment.search?p_logger=1&establishment=Walmart&State=CA&officetype=all&Office=all&p_case=all&p_violations_exist=all&startmonth=01&startday=01&startyear=2014&endmonth=06&endday=07&endyear=2015')
doc = html.fromstring(response.text)
link = doc.cssselect('.blueTen')[7]
print(link.text)
