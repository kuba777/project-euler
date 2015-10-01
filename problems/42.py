#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle
# numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and
# adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?


import string
import os


def triangle_list(n):
    """returns n triangle numbers"""
    tirangle_numbers = []
    for i in range(1, n + 1):
        # print(int(0.5 * i * (i + 1)))
        tirangle_numbers.append(int(0.5 * i * (i + 1)))
    return tirangle_numbers

tirangle_numbers = triangle_list(50)
# print(tirangle_numbers)


f = open(os.getcwd()[:-8] + 'misc files/p042_words.txt', 'r')

words = []
for i in f:
    for j in i.split(','):
        words.append(j[1:-1])
words.sort()

count = 0

for word in words:
    ord_sum = 0
    for letter in word:
        ord_sum += ord(letter) - 64
    if ord_sum in tirangle_numbers:
        # print(word, ord_sum)
        count += 1

print(count)

# upper = list(string.ascii_uppercase)
# print('alphabet len', len(upper))

# print(ord('A'))
# word = "SKY"
# for letter in word:
#     print(letter, ord(letter)-64)
