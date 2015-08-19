#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# 872187 1.9s


def decimal_to_binary(n):
    bits = ''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    result = 0
    while result != 1:
        bit = str(n % 2)
        bits = bit + bits
        # print(n % 2)
        n = n // 2
        result = n
    return "1" + bits


def is_palindrome(string):
    for i in range(len(string)//2 + 1):
        if string[i - 1] != string[-i]:
            return False
        # print(string[i-1], string[-i])
    return True


suma = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        # print(i, bin(i)[2:])
        suma = suma + i
print(suma)


# for i in range(0, 11):
#    print(i, decimal_to_binary(i), bin(i),  "{0:b}".format(i) )
