import time
import requests
import threading


def read_example() -> None:
    response = requests.get('https://ya.ru')
    print(response.status_code)

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

sync_start = time.time()

thread_1.start()
thread_2.start()

print('Все потоки работают')

thread_1.join()
thread_2.join()

sync_end = time.time()

print(f'Синхронное выполнение кода заняло {sync_end - sync_start:.4f} c.')
# Синхронное выполнение кода заняло 0.9220 c.

# Что в 3 раза быстреее чем синхронный запрос!!!!

# GIL блокируется на время выполнения запроса ввода выввода!