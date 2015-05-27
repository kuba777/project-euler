#!/usr/bin/env python
# -*- coding: utf-8 -*-

known = {1:1, 2:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


#print (len(str((fibonacci(4728)))))

#for i in range(1,13):
#    print(i, fibonacci(i))

n = 1
while len(str(fibonacci(n))) < 1000:
    n = n + 1
print (n)
