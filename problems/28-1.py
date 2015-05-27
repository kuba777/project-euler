#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#1,1,2,2,3,3,4,4
#{1: [0, 0], 2: [0, 1], 3: [-1, 1], 4: [-1, 0], 5: [-1, -1]}

from graphics import *

row = 0 
column = 0 

# right down left up 

def right(l):
    row, column = l[-1]
    l.append([row, column + 1])
    return l
    
def left(l):
    row, column = l[-1]
    l.append([row, column - 1])
    return l

def up(l):
    row, column = l[-1]
    l.append([row + 1, column ])
    return l

def down(l):
    row, column = l[-1]
    l.append([row - 1, column ])
    return l

lista = [[row,column]]

x = 1
end = 1002001
suma = 1
cycle = 0


while True: # when to stop
    for i in range(x):
        if len(lista) == end:
            break
        right(lista)
        if abs(lista[-1][0]) == abs(lista[-1][1]):
            #print(lista[-1][0], lista[-1][1], 'dia', len(lista))
            suma = suma + len(lista)
        
        
    for i in range(x):
        if len(lista) == end:
            break
        down(lista)
        if abs(lista[-1][0]) == abs(lista[-1][1]):
            #print(lista[-1][0], lista[-1][1], 'dia', len(lista))
            suma = suma + len(lista)
        
    for i in range(x+1):
        if len(lista) == end:
            break            
        left(lista)
        if abs(lista[-1][0]) == abs(lista[-1][1]):
            #print(lista[-1][0], lista[-1][1], 'dia', len(lista))
            suma = suma + len(lista)
        
    for i in range(x+1):
        if len(lista) == end:
            break
        up(lista)
        if abs(lista[-1][0]) == abs(lista[-1][1]):
            #print(lista[-1][0], lista[-1][1], 'dia', len(lista))
            suma = suma + len(lista)
        
    if len(lista) == end:
            break
    x = x + 2 
    
    
    
    
    
print(len(lista))
print(suma)
#win = GraphWin("Diagonal sum", 450, 450)
#win.setCoords(-10,-10,10,10)

#if abs(lista[-1][0]) == abs(lista[-1][1]):
            #print(lista[-1][0], lista[-1][1], 'dia', len(lista))
            #suma = suma + len(lista)
        #if len(lista) > end:
            #break


#if abs(lista[-1][0]) == abs(lista[-1][1]):
            #suma = suma + len(lista)
        #if len(lista) == 25:
            #break 

#for i in range(0, 25): 
    #d = Text(Point(lista[i][1], lista[i][0]), i+1)
    #if abs(lista[i][0]) == abs(lista[i][1]):
        #d.setStyle('bold')
        #d.setTextColor('red')
        #d.draw(win)
        #suma += i +1
    #else:
        #d.draw(win)

#print(suma)
#win.getMouse()              
    
