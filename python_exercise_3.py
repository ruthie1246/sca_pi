#!/usr/bin/env python

import random
i = 0
n = random.randint (1,10)
while True:
    guessed_number = int(raw_input("Guess a number from 1 to 10: "))
    if guessed_number > n:
        print "Guess is too high"
    elif guessed_number < n:
        print "Guess is too low"
    else:
        print "You guessed it"
        break
