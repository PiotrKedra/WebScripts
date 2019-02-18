import re

import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = "https://shop.flixbus.pl/search?departureCity=1314&arrivalCity=1915&route=Arnhem-Kraków&rideDate=24.02.2019&adult=1&"
r = requests.get(url)

html = r.text


#print(r.text)

print("DUPA #################")

soup = BeautifulSoup(html, 'html.parser')





# 'departure'
# aux-id-interconnection

for link in soup.find_all('div'):

    try:
        classes = link['class']

        for clas in classes:
            search = re.search(r'aux-id-interconnection', clas)

            if search:
                #print(clas)
                #print(link)
                #print("DASDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                #print(get_tag_text(str(link)))
                print("asdddddddddddddddddddddddddddddddddddddddddddd")
    except:
        continue



# search?q=dupa&




