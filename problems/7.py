#!/usr/bin/env python
# -*- coding: utf-8 -*-

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Answer and time
# 104743, 130.7s


def main():
    n = 2
    i = 2
    primes = 0
    while primes < 10001:
        while i - 1 < n:
            if n % i == 0:
                if i == n:
                    primes = primes + 1
                    print(primes, n)
                i = n + 10

            else:
                pass
            i = i + 1
        i = 2
        n = n + 1

main()
