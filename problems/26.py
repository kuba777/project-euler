#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#d = 983  length 982

from decimal import *
from sys import stdout
import re

getcontext().prec = 10000
print(Context())

maks = [0,0]

for i in range(1, 1001):
    dec = str(1/Decimal(i))[0:10000]
    
    
    
    
    
    
    for j in range(1, len(dec)+1):
        #print("1/{0:<3} {1:2} {2} {3:" ">60} ".format(i, "=", dec, dec[2:]))
        if len(dec[2:]) > 10:
            for k in [2,3,4,5]: #from where it stars searching
                for x in range(0, 1000): #length of recurring cycle
                    search = '\d{' + str(x)+ '}\d'
                    p = re.compile(search)
                    lista = p.findall(dec[k:])
                    if len(set(lista[:-1])) == 1:
                        #print( i,set(lista[:-1]), len(list(set(lista[:-1]))[0]))
                        if len(list(set(lista[:-1]))[0]) > maks[0]:
                            maks[0] = len(list(set(lista[:-1]))[0])
                            maks[1] = i
                            #print(len(list(set(lista[:-1]))[0]), i)
                        
                        break
                if len(set(lista[:-1])) == 1: # if one is found
                    break
        
        break
        
    
            
    
print (maks)
        #if rec:
        #print("{0:3d} {1:26s} {2:b} {3:d}  ".format(i, dec, rec, len(dec)))
    #stdout.write( str(1/Decimal(i))[2:] + "\n")
    #print(i,dec,  1/Decimal(i), pos, len(dec)  )
