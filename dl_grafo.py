from bs4 import BeautifulSoup as soup
import requests

site = "https://srgrafo.com/comic/"
site_no = 1
site_data = requests.get(site+str(site_no), {'user-agent':'bot1'})

site_soup = soup(site_data.text)

print (site_soup)