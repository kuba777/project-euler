#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer and time
# 906609, 0.3s


def main():
    n = 999 * 999
    while n > 950 * 950:
        m = 999
        if pal(str(n)):
            while m > 99:
                if n % m == 0 and n // m < 999:
                    print (n, m, n//m)
                m = m - 1
            m = 1
        n = n - 1


def pal(s):
    l = len(s)
    if l % 2 == 0:
        # print (l)
        for i in range(int(l/2)):
            # print (s[i],s[-i-1])
            if s[i] == s[-i-1]:
                if i == int(l/2) - 1:
                    # print(s, "is palindrome")
                    return True
            else:
                # print("Not Palindrome")
                break

main()
