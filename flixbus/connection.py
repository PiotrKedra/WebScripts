import re

from flixbus.connectionBuilder import ConnectionBuilder


class Connection:
    def __init__(self, builder: ConnectionBuilder):
        self.departure_time = builder.departure_time
        self.arrival_time = builder.arrival_time
        self.departure_station = builder.departure_station
        self.arrival_station = builder.departure_station
        self.duration = builder.duration
        self.bus_transfers = builder.bus_transfers
        self.bus_transfers_message = builder.bus_transfers_message
        self.price = builder.price
        self.ride_date = builder.ride_date

    def get_price(self) -> float:
        return float(re.sub(r',', '.', self.price))

    def get_bus_transfers(self) -> int:
        return int(self.bus_transfers)

    def __str__(self) -> str:
        return f'Ride data: {self.ride_date} \n' \
               f'Departure time: {self.departure_time} -- from {self.departure_station} \n' \
               f'Arrival time: {self.arrival_time} -- to {self.arrival_station} \n' \
               f'Duration: {self.duration} \n' \
               f'Price: {self.price} \n' \
               f'Transfers: {self.bus_transfers} --> Transfer message: {self.bus_transfers_message}'

