"""
Контекстный менеждер позволяет не парится о закрытиии файла, а также если произойдет исключение то файл будет закрыт автоматически. По сути своей это красивая
оббертка/замена бока кода с выражериями try,except,finaly.
Но для асинхронной работы они не годятся по этому был придуман асинхронный контекстный менеджер реализующий меттоды __aenter__ и __aexit__. для его использования
нужно применять await.
"""

import socket
import asyncio
from typing import Optional, Type
from types import TracebackType


class ConnectSocket():
    def __init__(self, server_socket):
        self.connection = None
        self.server_socket = server_socket

    async def __aenter__(self):
        print('Вход в контексный менеджер, ожидание подключения')
        loop = asyncio.get_event_loop()
        conection, addres = await loop.sock_accept(self.server_socket)
        self.connection = conection
        print('Подключение подтвержденно')
        return self.connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        print('Выход из контексного менеджера.')
        self.connection.close()
        print('Подключение закрыто')


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.setblocking(False)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen()
    async with ConnectSocket(server_socket) as connection:  # Здесь вызывается __aenter__ и начинается ожидание подключения
        data = await loop.sock_recv(connection, 1024)
        print(data)                                         # __aexit__ и подключение закрывается

asyncio.run(main=main())
