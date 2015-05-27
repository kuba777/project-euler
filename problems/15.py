# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# not finished

from graphics import *
#from random import *
import random

def main():
    
    def chunks(l, n):
        a = []
        for i in range(0, len(l), n):
            a.append(tuple(l[i:i+n]))
        return a
            
    def grid(a,b,win): 
        for i in range(1,a+1):
            for j in range(1,b+1):
                r2 = Rectangle(Point(i-1,j-1), Point(i,j))
                r2.draw(win)
     
    
    class arrow(object):
        """  """
        
        def __init__ (self,xb,yb, xs,ys, win):
            """ Class initialiser """
            self.xb = xb
            self.yb = yb
            self.xs = xs
            self.ys = ys
            self.win = win
            self.line = Line(Point(xb,yb), Point(xs,ys))
            self.line.setWidth(3)
            self.line.setArrow("last")
            self.line.setFill("blue")
            self.line.draw(win)
        def undraw(self):
            self.line.undraw()
            
        def right(self):
            
            self.xs = self.xs + 1
            
            self.line.undraw()
            self.line1 = Line(Point(self.xb,self.yb), Point(self.xs,self.ys))
            self.line1.setWidth(3)
            self.line1.setFill("blue")
            self.line1.draw(win)
            self.line = Line(Point(self.xb,self.yb), Point(self.xs,self.ys))
            self.line.setWidth(3)
            self.line.setArrow("last")
            self.line.setFill("blue")
            self.line.draw(win)
            self.xb = self.xs
            self.yb = self.ys
            
           
        def down(self):
            
            self.ys = self.ys + 1
            self.line.undraw()
            self.line2 = Line(Point(self.xb,self.yb), Point(self.xs,self.ys))
            self.line2.setWidth(3)
            self.line2.setFill("blue")
            self.line2.draw(win)
            self.line = Line(Point(self.xb,self.yb), Point(self.xs,self.ys))
            self.line.setWidth(3)
            self.line.setArrow("last")
            self.line.setFill("blue")
            self.line.draw(win)
            self.xb = self.xs
            self.yb = self.ys
        def __str__(self):
            return "(%s, %s)" % (self.xs, self.ys)
        def x(self):
            return self.xs
        def y(self):
            return self.ys
        """ Function doc"""
    
        
    lista = []  
    
    
    win = GraphWin("Lattice paths", 450, 450)
    win.setCoords(-1,23,23,-1)
    
    gridX = 4
    
    grid(gridX,gridX,win)
    a = arrow(0,0,0,0,win)
    
    war = 0
    liczba = 2
    for i in range(500):
        while not (a.x() == a.y() and a.x() == gridX):
            b = random.choice(["d","r"])
            if b == "d" and a.y() != gridX:
                a.down()
            elif b == "r" and a.x() != gridX:
                a.right()
            elif a.y() == gridX:
                a.right()
            elif a.x() == gridX:
                a.down()
            #print(a,b)
            win.getMouse()
            lista.append((a.x(),a.y()))
           
        a.undraw()
        a = arrow(0,0,0,0,win)
      
   
    print(len(set(chunks(lista,gridX*2))))
    win.getMouse()
    
    win.close()    # Close window when done

main()

