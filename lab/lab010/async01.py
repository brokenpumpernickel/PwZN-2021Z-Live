import asyncio

async def hello_async():
    await asyncio.sleep(5)
    print('Hello Async World!')

async def main():
    print('I\'m running')
    await hello_async()
    print('I\'m running')
    await hello_async()
    print('I\'m running')
    await hello_async()
    print('I\'m running')
    await hello_async()
    print('I\'m running')

asyncio.run(main())