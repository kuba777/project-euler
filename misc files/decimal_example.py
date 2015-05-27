#!/usr/bin/python

from decimal import *
from sys import stdout

getcontext().prec = 300
num = Decimal(1)
denom = Decimal(998001)
dec = str(num/denom)[2:3002]



for i,c in enumerate(dec):
  if i % 30 == 29:
    stdout.write(c + "\n")
  elif i % 3 == 2:
    stdout.write(c + " ")
  else:
    stdout.write(c)
