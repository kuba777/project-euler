#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

suma = 0
for i in range(len(str(a))):
    b =  str(a)[i]
    suma = suma + int(b)
print(suma)
    
