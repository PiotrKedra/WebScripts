from flixbus.conectionManager import ConnectionManager

manager = ConnectionManager()

connections = manager.find_cheapest_in_30_days('Kraków', 'Amsterdam')

for connection in connections:
    print(connection)
