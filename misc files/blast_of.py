

def main():
    #def blast_of(i):
        #if i == 0:
            #print("Blast off")
        #else:
            #print(i)
            #i = i -1
            #blast_of(i)
    #blast_of(5)
    
    #def pal(s):
        #first = s[0]
        #last = s[-1]
        #middle = s[1:-1]
        #if len(s) % 2 == 0:
            #if first == last and len(s) != 2:
                #print(s)
                #pal(middle)
            #elif len(s) == 2 and first == last:
                #print(s)
                #print("Palindrome")
                
                ##return True 
            #else:
                #print(middle)
                #print("Not palindrome")
                ##d = 2
        #else:
            #print("number not ")
        
        
    ##print(pal("12344321"))
    #b = pal("12344321")
    #print(b)
    
    def pal(s):
        l = len(s)
        if l % 2 == 0:
            #print (l)
            for i in range(int(l/2)):
                #print (s[i],s[-i-1])
                if s[i] == s[-i-1]:
                    if i == int(l/2) -1:  
                        #print(s, "is palindrome")
                        return True
                else:
                    #print("Not Palindrome")
                    break
        
    #a = pal("152345543251")
    #print(a)
    
    n = 999 * 999
    while n > 950 * 950:
        
        m = 999
        if  pal(str(n)):
            while m > 99:
                if n % m == 0 and n // m < 999:
                    print (n, m, n//m)
                m = m -1
            #if n % m == 0:
            #print("dddd")
            #m = m - 1
            m = 1
        n = n - 1
    
    
main()

