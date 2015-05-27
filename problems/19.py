#!/usr/bin/env python
# -*- coding: utf-8 -*-

def leap(rok):
        #print "czy rok jest przestepny"
        #rok = input("podaj rok: ")
        if rok % 100 != 0 and rok % 4 ==0 or rok % 400 == 0:
            #print "przestepny"
            return True
        else:
            #print "zwykly"
            return False
            
def days(month,rok):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if leap(rok):
            return 29
        else:
            return 28

week = ['Pon', 'Wt', 'Sr', 'Cz', 'Pt', 'So', 'Nie']
week1 = ['Wt', 'Sr', 'Cz', 'Pt', 'So', 'Nie']
niedziela = 0

day = 0
for i in range(1901,2001):
    for j in range(1,13):
        day += days(j,i)
        #print (day)
        while day+1 > len(week1):
            week1= week1 + week
        #print(day,len(week1))
        if week1[day] == 'Nie':
            #print ('Nie')
            niedziela += 1
print ('number of days in 20th century is',day)
print(niedziela, len(week1))
