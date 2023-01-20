import math

prime_array = []
FAYJOB = 1000

def isPrime(number):
    d = 2
    while( d <= math.sqrt(number) ):
        if (number%d == 0):
            return False
        d += 1
        
    if ( d > math.sqrt(number) ):
        return True

print('List before: ')
print(prime_array)

for i in range(2,FAYJOB,1):
    if ( isPrime(i) ):
        prime_array.append(i)

print('List after:')
print(prime_array)