#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = {}

for i in range(1, 10001):
    j = i - 1
    b = []
    while j > 0:
        if i % j == 0:
            b.append(j)
        j = j - 1
    #print(i,b)
    a[i] = b    
for i in a:
    for j in a:
        if i == sum(a[j]) and j == sum(a[i]) and i !=j:
            print (i, j)
    #print(i,sum(a[i]))
    
'''
220 284
284 220
1184 1210
1210 1184
2620 2924
2924 2620
5020 5564
5564 5020
6232 6368
6368 6232
'''
