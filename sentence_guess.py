#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

speed = 0.01
message = "Hello World!"

while True:
    sense.show_message(message, speed)
    user_guess = raw_input("Guess the sentence: ")
    if user_guess != message:
        speed = speed + 0.01
    else:
        print "win"
        print speed
        break

sense.clear()
