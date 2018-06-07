#!/usr/bin/env python

import random
i = 0
num_random_numbers = 10
while i < num_random_numbers:
    random_number = random.randint(1,4)
    guessed_number = int(raw_input("Guess an integer (between 1 and 4): "))
    print "Random number is", random_number
    if guessed_number != random_number:
        print "Your guess was not correct. Please try again."
    i = i + 1
