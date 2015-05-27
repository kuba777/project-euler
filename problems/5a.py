
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 232792560


def main():
    def pLista(n, l):
        d = 0
        #print(n, list(range(1,l+1)))
        #for i in list(range(1,l+1)):
        for i in [11,12,13,14,15,16,17,18,19,20]:
            #print(n,i,n % i)
            if n % i != 0:
                #print(i, n % i)
                #print(d)
                return False
            else:
                d = d + 1
        print(d)
        return True
        
    #print(pLista(2520,10))
    
    s = False
    n = 100000 
    while not s  :
        if n % 100000 == 0:
            print(n)
        if pLista(n,10) == True:
            print(n)
            s = True 
        n = n + 1
    
main()
