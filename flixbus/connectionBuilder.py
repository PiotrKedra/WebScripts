import re

from bs4 import BeautifulSoup


class ConnectionBuilder:

    def __init__(self, div: str, ride_data: str):
        self.departure_time = None
        self.arrival_time = None
        self.departure_station = None
        self.arrival_station = None
        self.duration = None
        self.bus_transfers = None
        self.bus_transfers_message = None
        self.price = None
        self.ride_date = ride_data

        self.div = div

        """ FlixBus classes names """
        self.departure_time_class = 'departure'
        self.arrival_time_class = 'arrival'
        self.departure_station_class = 'departure-station-name'
        self.arrival_station_class = 'arrival-station-name'
        self.duration_class = 'duration'
        self.bus_transfers_class = 'transf-num'
        self.price_class = 'total'

    def set_departure_time(self):
        self.departure_time = self.get_div_text(self.departure_time_class)

    def set_arrival_time(self):
        self.arrival_time = self.get_div_text(self.arrival_time_class)

    def set_departure_station(self):
        self.departure_station = self.get_div_text(self.departure_station_class)

    def set_arrival_station(self):
        self.arrival_station = self.get_div_text(self.arrival_station_class)

    def set_duration(self):
        self.duration = self.get_div_text(self.duration_class)

    def set_price(self):
        self.price = self.get_div_text(self.price_class)[0:7]

    def set_bus_transfer(self):
        soup = BeautifulSoup(self.div, 'html.parser')
        tag = soup.find('div', class_=self.bus_transfers_class)
        self.bus_transfers = tag.find('span', class_='num').text
        self.bus_transfers_message = re.sub(r'( +)|(\n)', ' ', tag.find('span', class_='has-popup').text)

    def build(self):
        self.set_departure_time()
        self.set_arrival_time()
        self.set_departure_station()
        self.set_arrival_station()
        self.set_duration()
        self.set_price()
        self.set_bus_transfer()
        return str(self)

    def __str__(self) -> str:
        return f'Ride data: {self.ride_date} \n' \
               f'Departure time: {self.departure_time} -- from {self.departure_station} \n' \
               f'Arrival time: {self.arrival_time} -- to {self.arrival_station} \n' \
               f'Duration: {self.duration} \n' \
               f'Price: {self.price} \n' \
               f'Transfers: {self.bus_transfers} --> Transfer message: {self.bus_transfers_message}'

    def get_div_text(self, class_name: str):
        soup = BeautifulSoup(self.div, 'html.parser')
        tag = soup.find('div', class_=class_name)
        if tag.text:
            return tag.text.lstrip()
        else:
            return f'Sth went wrong with: {class_name}'
