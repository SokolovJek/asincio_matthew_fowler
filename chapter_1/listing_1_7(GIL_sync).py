import time
import requests


def read_example(url) -> None:
    response = requests.get(url)
    print(response.status_code)

sync_start = time.time()

read_example('https://ya.ru')
read_example('https://ya.ru')

sync_end = time.time()

print(f'Синхронное выполнение кода заняло {sync_end - sync_start:.4f} c.')
# Синхронное выполнение кода заняло 3.0535 c.