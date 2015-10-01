#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

# 840 too long

maximum = 0
pp = 0

for p in range(743, 1000):
    solutions = set()
    for a in range(1, p//2):
        for b in range(1, p//2):
            for c in range(1, p//2):
                if a + b + c == p and a ** 2 + b ** 2 == c ** 2:
                    solutions.add((a, b, c))
    print(p, len(solutions))
    if len(solutions) > maximum:
        maximum = len(solutions)
        pp = p
print(pp, maximum)
