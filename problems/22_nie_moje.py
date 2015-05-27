import os

def p22():
    f = open(os.getcwd()[:-8] +"misc files/22_names.txt")
    names = sorted([n.strip('"') for n in f.read().split(',')])

    total = 0
    a = ord('A')
    for i in range(len(names)):
        total += sum([ord(c)-a+1  for c in names[i]]) * (i+1)
    print (total)

def main():
    from timeit import Timer
    print (Timer('p22()', 'from __main__ import p22').timeit(1))

if __name__ == '__main__': main()
	