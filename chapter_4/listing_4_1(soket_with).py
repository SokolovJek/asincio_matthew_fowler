"""Контекстный менеждер позволяет не парится о закрытиии файла, а также если произойдет исключение то файл будет закрыт автоматически. По сути своей это красивая
оббертка/замена бока кода с выражериями try,except,finaly.
Но для асинхронной работы они не годятся по этому был придуман асинхронный контекстный менеджер реализующий меттоды __aenter__ и __aexit__"""

import socket
import asyncio


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # параметры(работай с IP и портом, протокол TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # для того чтоб использовать повторно адрес
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()      # Прослушивать запросы на подключение, и «открыть почтовое отделение»


connections = []
try:
    while True:
        connection, client_address = server_socket.accept()  # Дождаться подключения и выделить клиенту почтовый ящик
        print(f'Получен запрос на подключение от {client_address}!')
        connections.append(connection)
        for connection in connections:
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
finally:
    server_socket.close()
