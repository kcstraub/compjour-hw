import bs4
import requests
response = requests.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("div.wanted-person-container-wrapper")
len(link)