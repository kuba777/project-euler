#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

# 7652413 too slow :)


def is_prime(n):
    if n == 1:
        return False
    if n in [2, 3, 5, 7, 11]:
        return True
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True


def is_pandigital(n):
    string = str(n)
    for i in range(1, len(string) + 1):
        if str(i) not in string:
            return False
    else:
        return True

for i in range(11, 1000000):
    if is_prime(i) and is_pandigital(i):
        print(i)
