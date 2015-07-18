#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
# are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# Answer and time
# 55 6594s
def rot(n):
    str_n = str(n)
    ret = []
    if len(str_n) == 1:
        return [int(str_n)]
    else:
        for i in range(len(str_n)):
            temp = str_n[-1]
            str_n = temp + str_n[:-1]
            ret.append(int(str_n))
    return ret


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

rot_prime = 0
for i in range(2, 1000001):
    rots = rot(i)
    count = 0
    for j in range(len(rots)):
        if not is_prime(rots[j]):
            break
        else:
            count = count + 1
    if count == len(rots):
        # print(i)
        rot_prime += 1

print((rot_prime))