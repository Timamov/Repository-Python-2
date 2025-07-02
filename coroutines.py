import asyncio
import time

async def some():
    print('Hello')
    await asyncio.sleep(1)
    print('Hello again')
asyncio.run(some())