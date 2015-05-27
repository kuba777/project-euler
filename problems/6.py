
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def main():
    suma1 = 0
    suma2 = 0
    for i in list(range(1,101)):
        #print(i ** 2)
        suma1 = suma1 + i ** 2
        suma2 = suma2 + i
    print(suma1,suma2 ** 2)
    print("Różnica",suma2 ** 2 - suma1 )
    
    
    
main()