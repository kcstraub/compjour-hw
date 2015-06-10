from lxml import html
import requests
response = requests.get('http://forecast.weather.gov/MapClick.php?CityName=Gatlinburg&state=TN&site=MRX&textField1=35.7234&textField2=-83.4937&e=0#.VXZEl6ZrWl0')
doc = html.fromstring(response.text)
link = doc.cssselect('div#current_conditions_detail td')[1]
print(link.text)