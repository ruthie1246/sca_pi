#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
yellow = (0, 200, 200)
blue = (100, 100, 100)

speed = 0.05

message = "Hello World!"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
