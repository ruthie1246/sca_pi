#!/usr/bin/env python

import random
i = 0
n = random.randint (1,10)
while True:
    guessed_number = int(raw_input("Guess a number from 1 to 10: "))
    if guessed_number > n:
        print "Guess is too high"
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # assign pin number for Passive Buzzer; pin 32 = GPIO 12
        buzz_pin = 32

        # set Passive Buzzer pin's mode as output
        GPIO.setup(buzz_pin, GPIO.OUT)

        # create Buzz function and set initial sound frequency to 1000 Hz
        Buzz = GPIO.PWM(buzz_pin, 1000)

        # change frequency and start Passive Buzzer using Buzz function with 50% duty for 1         second
        Buzz.ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()

        # reset GPIO resrouces used by script
        GPIO.cleanup()
    elif guessed_number < n:
        print "Guess is too low"
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # assign pin number for Passive Buzzer; pin 32 = GPIO 12
        buzz_pin = 32

        # set Passive Buzzer pin's mode as output
        GPIO.setup(buzz_pin, GPIO.OUT)

        # create Buzz function and set initial sound frequency to 1000 Hz
        Buzz = GPIO.PWM(buzz_pin, 1000)

        # change frequency and start Passive Buzzer using Buzz function with 50% duty for 1         second
        Buzz.ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()

        # reset GPIO resrouces used by script
        GPIO.cleanup()
    else:
        print "You guessed it"
        import RPi.GPIO as GPIO
        import time

        # breadboard setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False) 
    
        # assign pin number for Auto Flash LED; pin 11 = GPIO 17
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
        break
