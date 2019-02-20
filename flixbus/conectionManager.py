import re

import requests
from bs4 import BeautifulSoup
import datetime

from flixbus.connection import Connection
from flixbus.connectionBuilder import ConnectionBuilder


class ConnectionManager:
    cities = {
        'Amsterdam': 1334,
        'Kraków': 1915,
        'Arnhem': 1314,
    }

    def find_cheapest_in_30_days(self, departure_station: str, arrival_station: str):
        tmp_date = datetime.datetime.now()
        dates = [self.convert_date(tmp_date)]
        for i in range(0, 30):
            tmp_date = tmp_date + datetime.timedelta(days=1)
            dates.append(self.convert_date(tmp_date))

        connections = []
        for date in dates:
            connections.extend(self.find_connection(departure_station, arrival_station, date))

        good_connections = []
        for connection in connections:
            if connection.get_price() >= 190.0:
                print(f'Removed: {connection.get_price()}')
            else:
                good_connections.append(connection)
                print(connection.get_price())

        return good_connections

    def find_connection(self, departure_station: str, arrival_station: str, ride_date: str):

        connections = []

        url = f'https://shop.flixbus.pl/search?departureCity={self.cities.get(departure_station)}&\
        arrivalCity={self.cities.get(arrival_station)}&route={departure_station}-{arrival_station}&\
        rideDate={ride_date}&adult=1&'

        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        div_result = soup.find('div', id='results-group-container-direct')

        if div_result:
            for div in div_result.children:
                try:
                    classes = div['class']
                    flag = False
                    for clas in classes:
                        search = re.search(r'aux-id-interconnection', clas)
                        search2 = re.search(r'aux-id-direct', clas)
                        if search2 or search:
                            flag = True
                            break

                    if flag is True:
                        connection = Connection(ConnectionBuilder(str(div), ride_date).build())
                        connections.append(connection)
                    else:
                        break
                except Exception as e:
                    print(e)

        return connections

    @staticmethod
    def convert_date(date):
        return datetime.datetime.strptime(str(date)[:10], '%Y-%m-%d').strftime('%d.%m.%y')
