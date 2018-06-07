#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0, 255)
s = random.randint(0, 255)
t = random.randint(0, 255)

sense.show_letter("H", (r, s, t))
time.sleep(1)
sense.show_letter("i", (t, r, s))
time.sleep(1)
sense.show_letter("!", (s, t, r))
time.sleep(1)

sense.clear()
