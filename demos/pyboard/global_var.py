# define global variables, add any variables you need here
# Use class as variable container instead of defining individual variables

import pyb

class global_var:

    cnt = 1
    name = "Li"
    ver = "1.0"
    
    LED = pyb.LED(1)

gv = global_var()
