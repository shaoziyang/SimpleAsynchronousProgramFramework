# main file
import asyncio
import sapf_cfg
import machine


# import task files
for i in range(len(sapf_cfg.taskfile)):
    exec("import "+sapf_cfg.taskfile[i])

# create task
for i in range(len(sapf_cfg.taskname)):
    exec("asyncio.create_task("+sapf_cfg.taskname[i]+")")

# start
while (len(sapf_cfg.taskname) > 0):
    try:
        asyncio.Loop.run_forever()
    except KeyboardInterrupt:
        break
    except MemoryError:
        machine.reset()
    except:
        pass
