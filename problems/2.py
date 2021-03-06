#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.

# Answer and time
# 4613732, 0.1s


def main():
    a = 1
    b = 2
    # print(a,b)
    suma = 0
    while b < 4000000:
        if b % 2 == 0:
            suma = suma + b
        c = b
        b = b + a
        a = c
        # print(c)
    print (suma)
main()
