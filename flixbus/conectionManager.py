import re

import requests
from bs4 import BeautifulSoup

from flixbus.connection import Connection
from flixbus.connectionBuilder import ConnectionBuilder


class ConnectionManager:
    cities = {
        'Amsterdam': 1334,
        'Kraków': 1915,
        'Arnhem': 1314,
    }

    def find_connection(self, departure_station: str, arrival_station: str, ride_data: str):

        url = f'https://shop.flixbus.pl/search?departureCity={self.cities.get(departure_station)}&\
        arrivalCity={self.cities.get(arrival_station)}&route={departure_station}-{arrival_station}&\
        rideDate={ride_data}&adult=1&'

        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        div_r = soup.find('div', id='results-group-container-direct')

        if div_r:
            for div in div_r.findAll('div'):
                try:
                    classes = div['class']
                    for clas in classes:
                        search = re.search(r'aux-id-interconnection', clas)
                        search2 = re.search(r'aux-id-direct', clas)

                        # todo add data from html, not from args

                        if search2 or search:
                            connection = Connection(ConnectionBuilder(str(div), ride_data).build())
                            aa = connection
                            print(aa)

                except Exception as e:
                    continue
