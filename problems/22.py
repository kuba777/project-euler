
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import os

os.getcwd()

def names():
    f = open(os.getcwd()[:-8] + 'misc files/22_names.txt','r')
    #print(f)
    
    l = []
    for i in f:
        for j in i.split(','):
            l.append(j[1:-1])
    l.sort()
    #print(l)
    
    suma = 0
    score_sum = 0
    for i in range(0,len(l)):
        #print(i,l[i])
        for j in l[i]:
            suma = suma + ord(j) - 64
        #print(i+1,l[i],suma, suma * (i+1))
        
        score_sum = score_sum + suma * (i+1)
        suma = 0
    print(score_sum)
#main()
def main():
    from timeit import Timer
    print (Timer('names()', 'from __main__ import names').timeit(1))

if __name__ == '__main__': main()
