"""
модуля selectors для построения цикла событий сокетов
У базового класа BaseSelectors от которого унаследован DefaultSelector. Есть две основные концепции:
1. селекция - функция select блокирует сокет пока не произайдет какоенибудь событие, после возвращает список сокетов готовых для обработки. Можно навесить таймер
2. регистрация - если нужно получить уведомления конкретного типа например чтение запись для данного сокета, а потом то его регистрацию можно отменить
DefaultSelector сам определяет какой селектор((kqueue, epoll, IOCP) нужно употреблять для нашей ОС.

Имея такие строительные блоки, мы можем написать неблокирующий эхо-сервер, не нагружающий процессор. После создания серверного сокета мы регистрируем его в селекторе по умолчанию,
который будет прослушивать запросы на подключение от клиентов. Как только кто-то подключится к серверному сокету, мы зарегистрируем клиентский сокет,
чтобы селектор наблюдал за отправленными в него данными. Получив данные, мы отправим их назад клиенту. Кроме того, добавим тайм-аут, чтобы продемонстрировать
возможность выполнять другой код, пока мы ждем наступления событий.
"""

import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple



selector = selectors.DefaultSelector() # get selector our OC

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # параметры(работай с IP и портом, протокол TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # для того чтоб использовать повторно адрес

server_socket.bind(('127.0.0.1', 8000))
server_socket.setblocking(False)                                       # делаем сокет не блакирующим, тоесть проверяем есть ли там данные но если к нему еще некто не подключился будет ошибка
server_socket.listen()                                                 # Прослушивать запросы на подключение, и «открыть почтовое отделение»

selector.register(server_socket, selectors.EVENT_READ)                  # регистрируем событие

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)  # Создать селектор с тайм-аутом 1 с
    if len(events) == 0:                                                # Если ничего не произошло, сообщить об этом. Такое возможно в случае тайм-аута
        print('Событий нет, подожду еще!')
    for event, _ in events:
        event_socket = event.fileobj                                     # Получить сокет,для которого произошло событие,

        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"Получен запрос на подключение от {address}")
            selector.register(connection, selectors.EVENT_READ)         # Зарегистрировать клиент, подключившийся к сокету
        else:
            data = event_socket.recv(1024)
            print(f"Получены данные: {data}")
            event_socket.send(data)

