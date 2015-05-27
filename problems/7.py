
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 10001 104743


def main():
    n = 2
    i = 2
    primes = 0
    while primes < 10001:
        while i - 1 < n :
            if n % i == 0:
                #print('i',i, 'n', n, 1)
                if i == n :
                    primes = primes + 1
                    print(primes, n)
                i = n + 10
                
            else:
                pass
                #print('i',i, 'n', n)
            
            i = i + 1
        i = 2
        n = n + 1
        #primes = primes + 1
        #print()
    
    #f = True
    #l = []
    #n = 2
    #m = 0
    #for i in list(range(2,20)):
        #while n < i + 1:
            #if i % n == 0:
                #l.append(n)
                #if len(l) == 1 and i == n:
                    #m = m + 1
                    #print(m, i)
            ##print(n,i)
            #n = n + 1
        #l = []
        #n = 2
        
    
    
    
main()
