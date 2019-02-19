import re

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

from flixbus.connectionBuilder import ConnectionBuilder

ride_data = '24.02.2019'

url = f'https://shop.flixbus.pl/search?departureCity=1334&arrivalCity=1915&route=Amsterdam-Kraków&rideDate={ride_data}&adult=1&'

r = requests.get(url)
html = r.text

# print(r.text)

print("DUPA #################")

soup = BeautifulSoup(html, 'html.parser')

# 'departure'
# aux-id-interconnection

div_r = soup.find('div', id='results-group-container-direct')
if div_r:
    for div in div_r.findAll('div'):
        try:
            classes = div['class']

            for clas in classes:

                search = re.search(r'aux-id-interconnection', clas)

                search2 = re.search(r'aux-id-direct', clas)

                # todo aux-id-direct does not work
                # todo add data from html, not from args

                if search:
                    connection = ConnectionBuilder(str(div), ride_data)
                    aa = connection.build()

                    print(aa)

        except:
            continue

# search?q=dupa&
# results-group-container-direct
