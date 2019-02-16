import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = "https://www.flixbus.pl/"
r = requests.get(url)

html = r.text


print(r.text)

print("DUPA #################")

soup = BeautifulSoup(html, 'html.parser')


for link in soup.find_all('a'):
    print(link.get('href'))

