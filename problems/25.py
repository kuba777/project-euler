#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21,
# F9 = 34, F10 = 55, F11 = 89, F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Answer and time
# 4782, 0.1s

known = {1: 1, 2: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# print (len(str((fibonacci(4728)))))

# for i in range(1,13):
#    print(i, fibonacci(i))

n = 1
while len(str(fibonacci(n))) < 1000:
    n = n + 1
print (n)
