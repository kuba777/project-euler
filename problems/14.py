#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Answer and time
# 837799(525), 60s


count = 0


def Collatz(n):
    global count
    count = count + 1
    # print(count, n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return Collatz(n // 2)
    else:
        return Collatz(3 * n + 1)

# Collatz(13)
# print("count", count)

maximum = [0, 0]
for i in range(1, 1000001):
    Collatz(i)
    # print (i, count)
    if maximum[0] < count:
        maximum = [count, i]
    count = 0

print("number", maximum[1])
print("chain length", maximum[0])
