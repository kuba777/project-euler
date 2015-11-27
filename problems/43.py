#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each
# of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

# Answer and time
# 16695334890, 93s


def property(pandigital09):  # checks if 0 to 9 padigital number has substring divisibility property
    pan = str(pandigital09)
    div_list = [2, 3, 5, 7, 11, 13, 17]
    for i in div_list:
        index = div_list.index(i)
        # print(i, pan[index + 1:index + 4])
        if int(pan[index + 1: index + 4]) % i != 0:
            return False
    return True

# print (property(1406357289))

# pandigital number generator - problem 24


def permutation(lista, position):  # moves number at position to position + 1
    temp = lista[position]
    lista[position] = lista[position + 1]
    lista[position + 1] = temp


def dividers(i, n):
    a = []
    for j in range(1, i+1):
        a.append(j*n)
    return a


def beginning(lista, n, p):  # move n to p position of list
    a = lista.pop(n)
    lista.insert(p, a)
    return lista

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_temp = lista[:]
listy = []

# number of permutations
n_of_perm = {1: 1, 2: 2}
for i in range(2, 12):
    n_of_perm[i] = n_of_perm[i - 1] * i

first = {}
for i in range(3, 13):
    first[i] = 0

dividers_dict = {}
for i in range(1, 11):
    # print("{0:2d} {1}".format(i+1, dividers(i, n_of_perm[i])))
    dividers_dict[i+1] = dividers(i, n_of_perm[i])

dividers_list = []
keys = list(dividers_dict.keys())
keys.reverse()

for i in keys:
    # dividers_list.append(str(dividers_dict[i]))
    for j in range(len(dividers_dict[i])-1, -1, -1):
        dividers_list.append(dividers_dict[i][j])
        # print(dividers_list)

# print('dividers_list', dividers_list)
# print('keys', keys)
listy.append(lista_temp)
dict_temp = {}
for i in range(2, 13):
    dict_temp[i] = 0

# 3628800 - number of pandigital 0 to 9 numbers
while len(listy) != 3628800:  # n_of_perm[len(lista)]:
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

print(len(listy))
pan_sum = 0
for i in listy:
    suma = ""
    for j in i:
        suma += str(j)
    if int(suma) > 999999999:
        if property(int(suma)):
            # print(int(suma))
            pan_sum += int(suma)
print("Sum", pan_sum)
