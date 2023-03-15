# Simple Asynchronous Program Framework for micropython

A very Simple Asynchronous Program Framework for micropython.

The purpose of this project is to create a simple and easy-to-use framework for micropython asynchronous programs. Simply create the user's own task files, then add the task file name and task function to the configuration file, and the system will automatically create and run the task.

## Framework files

The framework itself has three files:

- **main.py**, main.py file for system.
- **sapf_cfg.py**, framework configuration file, you need define task file name and task function name in it.
- **global_var.py**, add any global variables you need here. To make it easier to use, class is used here as the variable container

## Configuration

It is very simple, in file sapf_cfg.py, you need define two list:

```
# task file list
taskfile = []

# task function name list
taskname = []
```

**taskfile** include task file name, and **taskname** define task function name. For example:

```
# task file list
taskfile = ["task1", "task2"]

# task function name list
taskname = ["task1.task_blink", "task2.task_inc"]
```

For more detailed usage, please refer to the routines in the [demos folder](demos).