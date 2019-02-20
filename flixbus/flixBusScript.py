from flixbus.conectionManager import ConnectionManager

manager = ConnectionManager()

connections = manager.find_forward('Kraków', 'Amsterdam', 60, 150.0)

for connection in connections:
    print(connection)
