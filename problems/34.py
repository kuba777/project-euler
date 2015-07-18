#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Answer and time
# 40730 - 1.5s

factorials = {0: 1, 1: 1, 2: 2, 3: 6}
sum_of_all = 0


def factorial(n):
    if n in factorials:
        return factorials[n]
    else:
        temp = factorial(n-1) * n
        factorials[n] = temp
        return temp

for i in range(3, 200000):
    digit = str(i)
    suma = 0
    for j in range(len(digit)):
        suma += factorial(int(digit[j]))
    if suma == i:
        # print(digit, suma)
        sum_of_all += suma

print(sum_of_all)
