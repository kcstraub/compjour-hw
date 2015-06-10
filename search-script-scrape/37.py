import bs4
import requests
response = requests.get('https://www.cia.gov/about-cia/leadership/')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("div.documentByLine div")[2]
print(link.text)