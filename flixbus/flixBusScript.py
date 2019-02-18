import re

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

from flixbus.connectionBuilder import ConnectionBuilder

url = "https://shop.flixbus.pl/search?departureCity=1334&arrivalCity=1915&route=Amsterdam-Kraków&rideDate=24.02.2019&adult=1&"

r = requests.get(url)
print("DUDPA{A")
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

                # todo aux-id-direct does not work

                if search:
                    connection = ConnectionBuilder(str(div))
                    connection.set_departure_time()
                    connection.set_arrival_time()
                    connection.set_departure_station()
                    connection.set_arrival_station()
                    connection.set_duration()
                    connection.set_price()
                    connection.set_bus_transfer()
                    aa = connection.build()

                    print(aa)

        except:
            continue

# search?q=dupa&
# results-group-container-direct
