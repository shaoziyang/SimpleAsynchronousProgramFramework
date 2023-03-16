import uasyncio as asyncio
import random

from global_var import gv

async def task_print():

    gv.cnt = 1
    
    while True:
        print(gv.cnt, random.getrandbits(10))
        gv.cnt += 1
        await asyncio.sleep(2)

