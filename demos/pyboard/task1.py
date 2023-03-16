import uasyncio as asyncio
import random

from global_var import gv

async def task_blink():

    while True:
        gv.LED.toggle()
        await asyncio.sleep(random.random()+0.2)

