#!/usr/bin/env python
# -*- coding: utf-8 -*-

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product
#is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#45228
suma = 0
lista = []

for i in range(0,10000):
    for j in range(0,10000):
        if len( set ((str(i))+(str(j))+(str(i * j))) ) == 9 and len(str(i)+str(j)+str(i*j))==9 and '0' not in str(i)+str(j)+str(i*j):
            x = j*i
            if x not in lista:
                lista.append(x) 
            print(i,'*', j, '=', j*i)
            
print(lista,sum(lista))        
