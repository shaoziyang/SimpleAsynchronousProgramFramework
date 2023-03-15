# define global variables, add any variables you need here
# Use class as variable container instead of defining individual variables

from machine import Pin

class global_var:

    cnt = 1
    name = "Li"
    ver = "1.0"
    
    LED = Pin(2, Pin.OUT, value = 0)

gv = global_var()
