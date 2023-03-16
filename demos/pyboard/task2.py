import uasyncio as asyncio

from global_var import gv

async def task_print(n):

    gv.cnt = 1
    
    while True:
        print(gv.cnt, gv.LED())
        gv.cnt += 1
        await asyncio.sleep(n)


async def task_blink(n):

    while True:
        gv.LED.toggle()
        await asyncio.sleep(n)
