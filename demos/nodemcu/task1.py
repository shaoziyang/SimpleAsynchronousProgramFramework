import asyncio

from global_var import gv

async def task_led(n):

    LED_brightness = 0
    
    while True:
        gv.LED.duty(abs(1023- LED_brightness*32))
        LED_brightness = (LED_brightness + 1) % 64
        await asyncio.sleep(n)

