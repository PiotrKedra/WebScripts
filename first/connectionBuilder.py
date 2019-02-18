from typing import Any

from bs4 import BeautifulSoup


class ConnectionBuilder:

    def __init__(self, div: str):
        self.departure_time = None
        self.arrival_time = None
        self.departure_station = None
        self.arrival_station = None
        self.duration = None
        self.bus_transfers = None
        self.bus_transfers_message = None
        self.price = None

        self.div = div

        """ FlixBus classes names """
        self.departure_time_class = 'departure'
        self.arrival_time_class = 'arrival'
        self.departure_station_class = 'departure-station-name'
        self.arrival_station_class = 'arrival-station-name'
        self.duration_class = 'duration'  #  ride__duration ride__duration-messages
        self.bus_transfers_class = 'transf-num'
        self.price_class = 'total'

    def set_departure_time(self):
        self.departure_time = self.get_tag_text(self.departure_time_class)
        return self

    def set_arrival_time(self):
        self.arrival_time = self.get_tag_text(self.arrival_time_class)
        return self

    def set_departure_station(self):
        self.departure_station = self.get_tag_text(self.departure_station_class)
        return self

    def set_arrival_station(self):
        self.arrival_station = self.get_tag_text(self.arrival_station_class)
        return self

    def set_duration(self):
        self.duration = self.get_tag_text(self.duration_class)
        return self

    def set_price(self):
        self.price = self.get_tag_text(self.price_class)
        return self

    def get_tag_text(self, class_name: str):
        soup = BeautifulSoup(self.div, 'html.parser')
        tag = soup.find('div', class_=class_name)
        if tag:
            return tag.string
        else:
            raise Exception
