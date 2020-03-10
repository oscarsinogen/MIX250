#Imports necessary packages
#Beautiful Soup library for webscraping
from bs4 import BeautifulSoup
#Requests to fetch HTML files
import requests
#Using lxml instead of default parser for speed
import lxml

url = "https://www.bt.no/"
response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)




if response.status_code == requests.codes.ok:
  print('Frontpage identified')

print(html_soup)
