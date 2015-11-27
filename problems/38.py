#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Answer and time
# 932718654 0.4s


def is_pandigital_9(n):
    string = str(n)
    if len(string) != 9:
        return False
    for i in range(1, 10):  # if len(set(string)) == 9:
        if str(i) not in string:
            return False
    return True

# print(is_pandigital_9(918273645))

largest = 0

for number in range(1, 100000):
    n = 1
    result = ""
    while len(result) < 9:
        temp = number * n
        result = result + str(temp)
        n = n + 1
    if is_pandigital_9(int(result)):
        # print(number, n-1, result)
        if largest < int(result):
            largest = int(result)

print(largest)
