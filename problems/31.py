# !/usr/bin/env python
# -*- coding: utf-8 -*-

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
# 73682 3 godziny :)

from random import *
from decimal import *


getcontext().prec = 2
    
    
    
    
suma = 0 
l = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
#      p1    p2   p5    p10  p20  p50 1  2
#      200    100  40   20    10   4   2  1
p1, p2, p5, p10, p20, p50, f1, f2 = 0,0,0,0,0,0,0,0
x = p1 * 0.01 + p2 * 0.02 + p5 *  0.05 + p10 * 0.1 + p20 * 0.2 + p50 * 0.5 + f1 * 1 + f2 * 2

lista = []
d = {}

for f2 in range(0,2):
    for f1 in range(0,3):
        for p50 in range(0,5):
            for p20 in range(0,11):
                for p10 in range(0,21):
                    for p5 in range(0,41):
                        for p2 in range (0,101):
                            for p1 in range(0, 201):
                                x = float(format(p1 * 0.01 + p2 * 0.02 + p5 *  0.05 + p10 * 0.1 + p20 * 0.2 + p50 * 0.5 + f1 * 1 + f2 * 2,'.2f'))
                                #lista.append(x)
                                #if x in d:
                                    #d[x] += 1
                                #else:
                                    #d[x] = 1
                                #if x > 2:
                                    #pass             
                                
                                if x == 2:
                                #print('p1', p1, 'p2', p2, 'p5', p5, 'p10', p10, 'p20', p20, 'p50', p50, x)
                                #print( p1,  p2,  p5,  p10,  p20,  p50, x)
                                    suma = suma + 1
                    
                    
                       
                    #for f1 in range (0,3):
                        #for f2 range(0,2):
                            
print(suma)
    
#print(sorted(set(lista)))
#for i in sorted(d):
#    print(i,d[i])
