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
    lista = [0,1,2]
    lista_temp = lista[:]
    
    listy = []
    
    # number of permutations
    n_of_perm = {1:1,2:2}
    
    for i in range(2,12):
        n_of_perm[i] =  n_of_perm[i-1]*i
        
    #for i in range(1, len(n_of_perm)+1):
    #    print("{0:2d}  {1:8d}".format(i, n_of_perm[i]))
    
    
    
    dividers_dict = {}
    
    for i in range(1,11):
        print("{0:2d} {1}".format(i+1, dividers(i,n_of_perm[i])))
        dividers_dict[i+1] = dividers(i, n_of_perm[i])
    
    #print(dividers_dict)
    
    dividers_list = []
    
    keys = list(dividers_dict.keys())
    keys.reverse()
    #print(keys)
    
    for i in keys:
        #dividers_list.append(str(dividers_dict[i]))
        for j in range(len(dividers_dict[i])-1,-1,-1):
           
            dividers_list.append(dividers_dict[i][j])
            #print(dividers_list)
    print(dividers_list)
    print(keys)
    
    listy.append(lista_temp)
    
    
    while len(listy) != n_of_perm[len(lista)]:
        for i in keys:
        #dividers_list.append(str(dividers_dict[i]))
            for j in range(len(dividers_dict[i])-1,-1,-1):
                if len(listy) % dividers_dict[i][j] == 0:
    
                    #print(listy[-1],  dividers_dict[i].index(dividers_dict[i][j]) - len(dividers_dict[i]), -i+1)
                    
                    if dividers_dict[i][j] == 1:
                        #print("dupa")
                        lista_temp = listy[-1][:]
                        permutation(lista_temp,-2)
                        listy.append(lista_temp)
                    else:
                        #print("dupa 2")
                        lista_temp = listy[0][:]
                        print(lista_temp) #, dividers_dict[i].index(dividers_dict[i][j]) - len(dividers_dict[i]), -i)
                        beginning(lista_temp, dividers_dict[i].index(dividers_dict[i][j]) - len(dividers_dict[i]), -i+1 )
                        listy.append(lista_temp)
        
    
    print(listy)
    #print(listy, len(listy), dividers_dict[i][j])
    #for i in range(len(listy)):
        #print(i+1, " - ",listy[i])
        #print("{0:2d} - {1}  {2}".format(i+1, listy[i], (i+1) % 6))
        
        #if i % 5  == 0:
        #    print("------------", i)
    
    
    
    
def dividers(i,n):
    a = []
    for j in range(1, i+1):
        a.append(j*n)
    return a

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
    
def permutation(lista, position):
    temp = lista[position] 
    lista[position] = lista[position+1]
    lista[position+1] = temp    
    
def main():
    from timeit import Timer
    print (Timer('lex_permutation()', 'from __main__ import lex_permutation').timeit(1))    
main()
