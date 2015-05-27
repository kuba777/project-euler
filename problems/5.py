
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def main():
    a = list(range(1,11))
    print (a)
    b = 1
    c = True
    while c:
        
        d = 0
        for i in a:
            if b % i == 0:
                d = d + 1
                if d == 10:
                    print(b)
                    c = False
        b = b + 1
main()
