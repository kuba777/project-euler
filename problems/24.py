#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A permutation is an ordered arrangement of objects. For example, 3124 
#is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
#listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations
# of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#2783915460 mathematica

def lex_permutation():
    
    lista = [0,1,2,3,4]
    lista_temp = lista[:]
    listy = []
    listy.append(lista)
    
    last = listy[-1][:]
    last.reverse()
    print(last)
    
    n = 1
    for i in range(4):
        #if len(listy) % 24 == 0:
            #lista_temp = listy[0][:]
            #lista_temp = beginning(lista_temp, len(listy) // 24 + len(lista_temp) % 5  , -4)
            #listy.append(lista_temp)
        if len(listy) % 6 == 0:
            lista_temp = listy[0][:]
            lista_temp = beginning(lista_temp, len(listy) // 6   , -3)  #+len(lista) % 4
            listy.append(lista_temp)
            print('dupa',lista_temp, len(listy) // 6 )
         
        #print(i)
        six(lista_temp,listy)
        
        
            
    
    
    #while l != lista:
        #listy.append([0,1,2,3,4])
        #listy.append([0,1,2,3,4])
        #listy.append([0,1,2,3,4])
        #listy.append([4,3,2,1,0])
    
    
    #listy.append(lista_temp)
    #six(lista_temp,listy)
    #a = listy[0][:]
    #a = beginning(a,2,1)
    #six(a,listy)
    #a = listy[0][:]
    #a = beginning(a,3,1)
    #six(a,listy)
    #a = listy[0][:]
    #a = beginning(a,4,1)
    #six(a,listy)
    #a = listy[0][:]
    #a = beginning(a,1,0)
    #six(a,listy)
    
    
    
    #listy.append(a)
    #print (listy, len(listy))
    for i in range(len(listy)):
        #print(i+1, " - ",listy[i])
        print("{0:2d} - {1}  {2}".format(i+1, listy[i], (i+1) % 6))
        
        #if i % 5  == 0:
        #    print("------------", i)
    
    
    
def beginning(lista, n, p): #move n to p position of list
    a = lista.pop(n)
    lista.insert(p, a)
    return lista
        
def lenn(lista,n):
    
    lista_temp = lista[:]
    pop = lista_temp.pop(n)
    lista_temp.insert(n,pop)
        #listy.append(lista1)
    return lista_temp
        
    
def six(lista, listy):
    
    #listy.append(lista)
    lista_temp = lista[:]
    
    permutation(lista_temp,-2)
    listy.append(lista_temp)
    
    for i in [-2,-1]:

        lista1 = lista[:]
        
        pop = lista1.pop(i)
        lista1.insert(-2, pop)
        listy.append(lista1)
        
        lista2 = lista1[:]
        permutation(lista2,-2)
        listy.append(lista2)
    return listy
    
def permutation(lista, position):
    temp = lista[position] 
    lista[position] = lista[position+1]
    lista[position+1] = temp    
    
def main():
    from timeit import Timer
    print (Timer('lex_permutation()', 'from __main__ import lex_permutation').timeit(1))    
main()
