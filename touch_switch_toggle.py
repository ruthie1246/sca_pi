#!/usr/bin/env python
# this script uses the Touch Switch to toggle on/off sensors

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Touch Switch; pin 31 = GPIO 6
touch_pin = 31

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin, GPIO.IN)

# create infinite loop that reads Touch Switch input
while True:
    if GPIO.input(touch_pin) == 0:
        led_pin = 11

        # set Auto Flash LED pin's mode as output
        GPIO.setup(led_pin,GPIO.OUT)

        # turn on Auto Flash LED
        GPIO.output(led_pin,True)
        time.sleep(2)

        # turn off Auto Flash LED
        GPIO.output(led_pin,False)

        # reset GPIO resources used by script
        GPIO.cleanup()
    if GPIO.input(touch_pin) == 1:
        led_pin = 11

        # set Auto Flash LED pin's mode as output
        GPIO.setup(led_pin,GPIO.OUT)

        # turn on Auto Flash LED
        GPIO.output(led_pin,True)
        time.sleep(2)

        # turn off Auto Flash LED
        GPIO.output(led_pin,False)

        # reset GPIO resources used by script
        GPIO.cleanup()
