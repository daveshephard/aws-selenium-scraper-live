import requests
from bs4 import BeautifulSoup

AUTONATION_START_LINK = 'https://www.pro-football-reference.com/players/'

#does not execute javascript
response = requests.get(AUTONATION_START_LINK)

print('Status Code', response.status_code)
#status code 200 = successful (400 / 404 is not successful)

#print('Output', response.text[:1000])

#with open('autonation.html', 'w') as f:
 #   f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser' )
print('Page title:', doc.title.text)

#find all the player links, all inks where class = page_index
player_links = doc.find_all("a", string="players")
print('Players links:', player_links)

  #listing = listings[0]
  #print('Model: ',listing_title.text)
  #print('URL: ',url)