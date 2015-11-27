#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer and time
# 232792560, 127s


def pLista(n, l):
        d = 0
        for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            if n % i != 0:
                return False
            else:
                d = d + 1
        # print(d)
        return True


def main():
    s = False
    n = 100000
    while not s:
        if pLista(n, 10):
            print(n)
            s = True
        n = n + 1

main()
