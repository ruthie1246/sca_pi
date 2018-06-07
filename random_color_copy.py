#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

for i, c in enumerate('Hey peeps'):  
    r = random.randint(0, 255)    
    s = random.randint(0, 255)
    t = random.randint(0, 255)
    
    sense.show_letter(c, (r, s, t))
    print "Random number r=", r, "s=", s, "t=", t    
    time.sleep(1)

sense.clear()
