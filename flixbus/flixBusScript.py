from flixbus.conectionManager import ConnectionManager

manager = ConnectionManager()

connections = manager.find_forward('Kraków', 'Amsterdam', 60)

for connection in connections:
    print(connection)
