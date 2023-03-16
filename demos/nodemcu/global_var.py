# define global variables, add any variables you need here
# Use class as variable container instead of defining individual variables

from machine import Pin, PWM

class global_var:

    cnt = 1
    name = "Li"
    ver = "1.0"
    
    LED = PWM(Pin(2), freq=200)

gv = global_var()
