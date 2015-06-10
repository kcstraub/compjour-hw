import bs4
import requests
data_url = "http://www.gao.gov/browse/topic"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("li")[16]
print(link.text)