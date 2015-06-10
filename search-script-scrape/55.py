import bs4
import requests
data_url = "http://www.gao.gov/browse/topic"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("span")[30]
print(link.text)