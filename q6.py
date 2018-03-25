# Write a program that calculates and prints the value according
# to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be
# input to your program in a comma-separated sequence.


#!/usr/bin/python
import math


dValues = input("Enter a sequence of numbers: ")
values = dValues.split(',')

c = 50
h = 30
l = []

for d in values:
    l.append(str(int(math.sqrt((2 * c * float(d))/h))))

print(','.join(l))
