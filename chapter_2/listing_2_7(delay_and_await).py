import asyncio
from utils import delay


# from chapter_2.my import a
# from my1 import a

# # import os
# print(a)
# # print(os.path.abspath(path))


# async def add_one(number: int) -> int:
#     return number + 1

# async def hello_world() -> str:

#     await delay(2)
#     return 'Hello world'

# async def main() -> None:
#     message = await hello_world()
#     one_pluse_one = await add_one(1)
#     print(one_pluse_one)
#     print(message)

# asyncio.run(main())

# И что же не так с этим кодом? плохой результат так как фукция main приостанавливается и ждет пока отработает hello_world а после ждет пока отработает функция add_one
# В данном случае код ведет себя как последовательный

# Нам хотелось бы уйти от этой последовательной модели и выполнять add_one конкурентно с hello_world. Для этого введем в рассмотрение концепцию задачи