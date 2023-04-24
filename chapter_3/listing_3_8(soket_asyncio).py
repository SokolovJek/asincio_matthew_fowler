"""
у библиотеки asyncio уже реализованы основные методы работы с API сокетов:sock_accept, sock_recv, sock_sendall.
Только передается сокет в качестве аргумента и возвращают они сопрограмму
"""

import socket
import asyncio
from asyncio import AbstractEventLoop


async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024):           # В бесконечном цикле ожидаем данных от клиента
        await loop.sock_sendall(connection, data)                   # Получив данные, отправляем их обратно клиенту

async def listen_for_connection(server_socket: socket,
                                 loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        asyncio.create_task(echo(connection, loop))                 # После получения запроса на подключение создаем задачу echo, ожидающую данные от клиента

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())    # Запускаем сопрограмму прослушивания порта на предмет подключений

asyncio.run(main())
