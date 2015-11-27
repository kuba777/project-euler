#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# Answer and time
# 25164150, 0.1s


def main():
    suma1 = 0
    suma2 = 0
    for i in list(range(1, 101)):
        # print(i ** 2)
        suma1 = suma1 + i ** 2
        suma2 = suma2 + i
    print(suma1, suma2 ** 2)
    print("Difference", suma2 ** 2 - suma1)

main()
