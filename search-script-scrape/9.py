import bs4
import requests
response = requests.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml')
soup = bs4.BeautifulSoup(response.text)
votes=0


for link in soup.select('votes vote'):
    if link.yeas is not None and link.nays is not None:
        if int(link.nays.text)-int(link.yeas.text) < 5:
            votes=votes+1

print(votes)