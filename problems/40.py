#!/usr/bin/env python
# -*- coding: utf-8 -*-

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910(1)112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# 210 0.2s


constant = 1
n = 2
s = str(constant)

while len(s) < 1000000:
    s += str(n)
    n += 1

print(int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999]))


# for x in range(1, 7):
#     prod *= int(y[10**x])
