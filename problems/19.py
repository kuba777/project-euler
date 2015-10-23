#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# 171


def leap(year):
        if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
            # print "przestepny"
            return True
        else:
            # print "zwykly"
            return False


def days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap(year):
            return 29
        else:
            return 28

week = ['Pon', 'Wt', 'Sr', 'Cz', 'Pt', 'So', 'Nie']
week1 = ['Wt', 'Sr', 'Cz', 'Pt', 'So', 'Nie']
niedziela = 0

day = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        day += days(j, i)
        # print (day)
        while day+1 > len(week1):
            week1 = week1 + week
        # print(day,len(week1))
        if week1[day] == 'Nie':
            # p rint ('Nie')
            niedziela += 1
print ('number of days in 20th century is', day)
print('number of Sundays', niedziela)
