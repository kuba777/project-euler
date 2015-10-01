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


def right(d):
    diclk = list(d.keys())[-1]  # dict last key
    row, column = d[diclk]
    d[diclk + 1] = [row, column + 1]
    return d


def left(d):
    diclk = list(d.keys())[-1]  # dict last key
    row, column = d[diclk]
    d[diclk + 1] = [row, column - 1]
    return d


def up(d):
    diclk = list(d.keys())[-1]  # dict last key
    row, column = d[diclk]
    d[diclk + 1] = [row + 1, column ]
    return d


def down(d):
    diclk = list(d.keys())[-1]  # dict last key
    row, column = d[diclk]
    d[diclk + 1] = [row - 1, column]
    return d

dic = {1:[row, column]}

diclk = list(dic.keys())[-1]
x = 1

dsum = 0

while diclk< 100: # when to stop
    for i in range(x):
        right(dic)
    for i in range(x):
        down(dic)
    for i in range(x+1):
        left(dic)
    for i in range(x+1):
        up(dic)
        
    x = x + 2 # alert
    diclk = list(dic.keys())[-1]
    
    

print(dic)

win = GraphWin("Diagonal sum", 450, 450)
win.setCoords(-10,-10,10,10)

 

for i in range(1, 51): #1001 * 1001 
    d = Text(Point(dic[i][1], dic[i][0]), i)
    if abs(dic[i][1]) == abs(dic[i][0]):
        d.setStyle('bold')
        d.setTextColor('red')
        d.draw(win)
        dsum += i
    else:
        d.draw(win)

print(dsum)
win.getMouse()            
    
    
