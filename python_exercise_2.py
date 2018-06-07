#!/usr/bin/python

x = raw_input('Enter the first integer:')
y = raw_input('Enter the second integer:')

x = int(x)
y = int(y)

if x > y:
    Maximum = x
    Minimum = y

else:
    Maximum = y
    Minimum = x

print "The maximum is", Maximum
print "The minimum is", Minimum

answer = Maximum - Minimum
print "Maximum - Minimum =", answer 
