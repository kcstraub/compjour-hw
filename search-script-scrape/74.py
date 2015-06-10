import bs4
import requests
data_url = "http://www.legis.ga.gov/Legislation/en-US/display/20152016/HB/106"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("div.item")[3]
print(link.text)