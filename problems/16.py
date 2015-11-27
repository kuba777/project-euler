#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# Answer and time
# 1366, 0.0s


def main():
    a = 2 ** 1000
    # print(a)
    b = str(a)
    # print(len(b))
    # print(len(a))
    c = 0
    for i in range(len(b)):
        # print(int(b[i]))
        c = c + int(b[i])
    print(c)


main()
