# main file

import uasyncio as asyncio
import sapf_cfg

# import task files
for i in range(len(sapf_cfg.taskfile)):
    exec("import "+sapf_cfg.taskfile[i])

# create task
for i in range(len(sapf_cfg.taskname)):
    exec("asyncio.create_task("+sapf_cfg.taskname[i]+")")

# start 
asyncio.Loop.run_forever()
