import asyncio
from asyncio import Future
import time
from utils import  delay


def make_request() -> Future:
    print('я функция make_request')                                                         #2
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future) -> None:
    print('я функция set_future_value')                                                     #4
    await asyncio.sleep(1)
    future.set_result(42)
    print('resuld is set')                                                                  #6

async def main() -> None:
    start_time = time.time()
    future = make_request()                                                                 #1
    print(f'будущий объект готоа? Ответ: {future.done()}')                                  #3
    delay_1 = asyncio.create_task(delay(10))                                                #5
    value = await future
    print(f'будущий объект готоа? Ответ: {future.done()}, result={value}')                  #7
    await delay_1                                                                           #8
    end_time = time.time()
    print(f'running time ={end_time - start_time}')                                         #9

asyncio.run(main())

# я функция make_request
# будущий объект готоа? Ответ: False
# я функция set_future_value
# засыпаю на 10 с. Function:0
# resuld is set
# будущий объект готоа? Ответ: True, result=42
# сон в течении 10 с. закочился. Function:0
# running time =10.01068639755249
