import bs4
import requests
data_url = "https://www.congress.gov/search?q=%7B%22source%22%3A%22congrecord%22%2C%22crHouseMemberRemarks%22%3A%22Issa%2C+Darrell+E.+%5BR-CA%5D%22%7D"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("span")[7]
print(link.text)