#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes
# for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# lista (94, -61, 971)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
            break
    return True

lista = (0, 0, 0)

for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        length = 0
        for x in range(0, 100):
            prime = x ** 2 + i * x + j
            if is_prime(prime):
                length += 1
                # print(i, j, x, prime, is_prime(prime))
        if length > lista[0]:
            lista = length, i, j
            print(lista)
            # a = input()
print(lista)
