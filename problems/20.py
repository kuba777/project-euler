#!/usr/bin/env python
# -*- coding: utf-8 -*-

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# 648


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

# print(factorial(100))

a = factorial(100)

suma = 0
for i in range(len(str(a))):
    b = str(a)[i]
    suma = suma + int(b)

print(suma)
