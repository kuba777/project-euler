#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer and time
# 6857, 0.1s


def main():
    a = 600851475143
    d = 2
    l = []
    while a != 1:
        if a % d == 0:
            l.append(d)
            a = a // d
            d = d + 1
            # print(a, d-1)
        d = d + 1
    print(max(l))
main()
