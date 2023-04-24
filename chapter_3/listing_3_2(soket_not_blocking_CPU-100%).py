import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # параметры(работай с IP и портом, протокол TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # для того чтоб использовать повторно адрес
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()      # Прослушивать запросы на подключение, и «открыть почтовое отделение»
server_socket.setblocking(False)


connections = []
try:
    while True:
        try:
            connection, client_address = server_socket.accept()  # Дождаться подключения и выделить клиенту почтовый ящик
            print(f'Получен запрос на подключение от {client_address}!')
            connection.setblocking(False)
            connections.append(connection)
        except BlockingIOError:
            pass
            for connection in connections:
                try:
                    buffer = b''
                    while not buffer.endswith(b'\r\n'):
                        data = connection.recv(2)
                        if not data:
                            break
                        else:
                            print(f'Получены данные {data}')
                            buffer += data
                    print(f'Отправленно соообщение {buffer}')
                    connection.send(buffer)
                except BlockingIOError:
                    pass
finally:
    server_socket.close()
