#!/usr/bin/env python

x = int(raw_input("Enter an integer (>1): "))
#Get an integer > 1 from user
while x < 2:
    x = int(input("Enter an integer (>1): "))

#print i and i*i for 1<=i<x
i = 1;
while i < x:
    print i, ' ', i * i
    i = i + 1
