#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
# listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations
# of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Answer and time
# 2783915460, 11.7s


def lex_permutation():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_temp = lista[:]
    listy = []

    # number of permutations
    n_of_perm = {1: 1, 2: 2}
    for i in range(2, 12):
        n_of_perm[i] = n_of_perm[i - 1] * i

    print ('number of permutations')
    print("{0:4s}  {1:1s}".format('elements', 'n of perm'))
    for i in range(1, len(n_of_perm)+1):
        print("{0:2d} {2:1s} {1:8d}  ".format(i, n_of_perm[i], '-'))

    first = {}
    for i in range(3, 13):
        first[i] = 0

    dividers_dict = {}
    for i in range(1, 11):
        print("{0:2d} {1}".format(i+1, dividers(i, n_of_perm[i])))
        dividers_dict[i+1] = dividers(i, n_of_perm[i])

    dividers_list = []
    keys = list(dividers_dict.keys())
    keys.reverse()

    for i in keys:
        # dividers_list.append(str(dividers_dict[i]))
        for j in range(len(dividers_dict[i])-1, -1, -1):
            dividers_list.append(dividers_dict[i][j])
            # print(dividers_list)

    print('dividers_list', dividers_list)
    # print('keys', keys)
    listy.append(lista_temp)
    dict_temp = {}
    for i in range(2, 13):
        dict_temp[i] = 0

    while len(listy) != 1000000:  # n_of_perm[len(lista)]:
        for i in keys:
            for j in range(len(dividers_dict[i])-1, -1, -1):
                if len(listy) % dividers_dict[i][j] == 0:
                    if dividers_dict[i][j] == 1:
                        lista_temp = listy[-1][:]
                        permutation(lista_temp, -2)
                        listy.append(lista_temp)
                        # print(lista_temp, "*")
                    else:
                        dict_temp[i] += 1
                        lista_temp = listy[first[i]][:]
                        beginning(lista_temp, -i + dict_temp[i], -i + 1)
                        if dict_temp[i] == i-1:
                            dict_temp[i] = 0
                            first[i] += dividers_dict[i+1][0]
                        # print(lista_temp,first[i])
                        listy.append(lista_temp)
    print("")
    print("1 000 000 permutation - ",  listy[-1])


def dividers(i, n):
    a = []
    for j in range(1, i+1):
        a.append(j*n)
    return a


def beginning(lista, n, p):  # move n to p position of list
    a = lista.pop(n)
    lista.insert(p, a)
    return lista


def permutation(lista, position):  # moves number at position to position + 1
    temp = lista[position]
    lista[position] = lista[position+1]
    lista[position+1] = temp


def main():
    from timeit import Timer
    print (Timer('lex_permutation()', 'from __main__ import lex_permutation').timeit(1))
main()
