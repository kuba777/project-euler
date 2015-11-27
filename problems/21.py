#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Let d(n) be defined as the sum of proper divisors of n (numbers less than
# n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# Answer and time
# 31626 56s

a = {}

for i in range(1, 10001):
    j = i - 1
    b = []
    while j > 0:
        if i % j == 0:
            b.append(j)
        j = j - 1
    # print(i,b)
    a[i] = b
suma = 0
for i in a:
    for j in a:
        if i == sum(a[j]) and j == sum(a[i]) and i != j:
            # print (i, j)
            suma = suma + i
    # print(i, sum(a[i]))
print(suma)
'''
220 284
284 220
1184 1210
1210 1184
2620 2924
2924 2620
5020 5564
5564 5020
6232 6368
6368 6232
'''
