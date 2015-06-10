import bs4
import requests
data_url = "http://www.dol.gov/whd/minwage/america.htm#Consolidated"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("table")[10]
print(link.text)