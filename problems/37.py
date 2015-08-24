#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# 748317 17.7s


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


def primes(n):
    """
    returns list of first n primes
    """
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


def turncate_prime(n):
    """
    checks if prime number is 'truncatable'
    """
    number = str(n)
    if "0" in number:
        return False
    for i in range(1, len(number)):
        if not is_prime(int(number[0: len(number)-i])) or not is_prime(int(number[i:])):
            # print(int(number[0: len(number)-i]))
            # print(int(number[i:]))
            return False
    return True


list_of_primes = primes(100000)[4:]
# print(list_of_primes)
suma = 0
for i in list_of_primes:
    if turncate_prime(i):
        print(i)
        suma += i
print("sum", suma)
