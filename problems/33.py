#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by !cancelling !the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.


product = []

for i in range(10,100):
    for j in range(10,100):
        a, b = str(i)[0], str(i)[1]
        c ,d = str(j)[0], str(j)[1]
        frac = "01"
        if a == d and int(a) != 0 and int(c) != 0 and b != c:
            frac = (b + "/" + c, int(b)/int(c))
        elif b == c and int(b) != 0 and int(d) != 0 and a != d:
            frac = (a + "/" + d, int(a)/int(d))
        if int(a+b)/int(c+d) == frac[1] and frac[1] < 1:
            print (a+b+"/"+c+d, i/j, frac[1])
            
            product.append(frac[1])
print(product)
prod = 1
for i in range(4):
    prod = product[i] * prod
print(prod)
