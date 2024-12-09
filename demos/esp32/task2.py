import asyncio

from global_var import gv

async def task_inc():

    gv.cnt = 1
    
    while True:
        print(gv.cnt, gv.LED())
        gv.cnt += 1
        await asyncio.sleep(1)

