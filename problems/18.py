
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# only manual selection implemented

from graphics import *
from random import *
import os

def main():
    f = open(os.getcwd()[:-8] + 'misc files/18.txt','r')
    #print(f)
    win = GraphWin("Maximum path sum", 450, 450)
    win.setCoords(-20,20,20,-2)
    
    e = []
    c = []
    lista = []
    lines = 0
    for line in f:
        lista.append(line)
        lines += 1
        for i in list(range(0,len(line)-1,3)):
            try:
                d = line[i] + line[i+1]
                c.append(d)
                
            except ValueError:
                pass
                
        
        a = Text(Point(0,lines+1),c)
        a.setStyle('normal')
        b = Text(Point(2,lines+1),c[0])
        
        if lines == 10:
            a.setStyle('bold')
            a.setTextColor('red')
            
        #a.draw(win)
        
        #print("c", c),
        e.append(c)
        c = []
        
    #print('e', e)
    #print (len(e))
    #for i in range(len(e)):
    #    print(len(e[i]))
        
     
    #for i in range(10):
    #    p = win.getMouse()
    #    print (p.getX(), p.getY())
    g = []
    for i in range(1,len(e)+1):# number of rows
        g.append(list(range(-i+1,i,2)))
        #for j in range(len(e[i+1])): #length of each row
            #if i == len(list(range(-j+1,j,2))):
                #g.append(list(range(-j+1,j,2)))
                #print(i,j)
        #win.getMouse()
                #print(list(range(-j+1,j,2)),e[i-1],e[i][j])
                #for k in (range(-j+1,j,2)):
                #    b = Text(Point(k,i+1),e[i][j])
                #    b.draw(win)
            
    #print(g)
    #print(len(g),len(e))
    lines = 0
    suma = 0
    for i, j in zip(e,g):
        #print(i,j)
        for k in range(0,len(i)):
            
            d = Text(Point(j[k],lines),i[k])
            #if k ==0:
               # suma += int(i[k])
               # print (suma)
            ##print(i[k], j[k])
            ##print(len(e[i]),e[i][j])
            ##d = Text(Point(0,i+2),e[i][j])
            d.draw(win)
        
        lines += 1
    
    d = Text(Point(0,0), e[0])
    d.setStyle('bold')
    d.setTextColor('red')
    d.draw(win)
    #win.getMouse()
    
    
    suma = 75
    index = 0
    lines = 1
    for i, j in zip(e[1:],g[1:]):
        mouse = win.getMouse()
        x = mouse.getX()
        #x = choice([-1,1])
        
        if x>0:
            index = index + 1
        else:
            index = index
        for k in range(0,len(i)):
            if index == k:
                
                d = Text(Point(j[k],lines), i[k])
                d.setStyle('bold')
                d.setTextColor('red')
                d.draw(win)
                suma = suma + int(i[k])
                #print(len(i),index,k,i[k])
                print(len(i),i[k])
        print('Suma', suma)
        lines += 1
        #red = Text(Point(len(e[i])/2.1 + 0.4 * i, i+2), e[i][0])
        
        #red.setStyle('bold')
        #red.setTextColor('red')
        #red.draw(win)
        #win.getMouse()
    
        
    
    
    
    win.getMouse()
    
main()

