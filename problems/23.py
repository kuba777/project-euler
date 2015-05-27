#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


#4179871


def abb():
    a = {}
    #28123
    suma = 0
    abundant = []
    
    for i in range(2, 28123):
        j = i -1
        b = []
        while j > 0:
            if i % j == 0:
                b.append(j)
            j = j - 1
        s = ''
        for k in b:
            suma = suma + k
        if suma == i:
            s = 'PERFECT'
        elif suma > i:
            s = 'ABUNDANT'
            abundant.append(i)
        else:
            s = 'DEFFICIENT'
        
        #print(i,b, suma, s)
        suma = 0
        #a[i] = b    
    #print(abundant)
    
    
    suma = set()
    for i in abundant:
        for j in abundant:
            suma.add(i+j)
    #print (suma)
    suma2 = 0
    #for i in abundant:
     #   for j in abundant:
       #     print(i+j)
    for i in range(0,28124):
        if i not in suma:
            suma2 += i
    print (suma2)
    
    
def main():
    from timeit import Timer
    print (Timer('abb()', 'from __main__ import abb').timeit(1))    
main()
