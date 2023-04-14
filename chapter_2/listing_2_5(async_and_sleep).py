import asyncio


async def hello_world():
    await asyncio.sleep(1)
    return 'hello world'

async def main():
    message = await hello_world()
    # у нас появилась одна секунда, в течение которой мог бы конкурентно работать другой код
    print(message)


asyncio.run(main())
