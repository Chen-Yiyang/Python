# Prime Number
# by Yiyang 03/02/18

import math

def isPrime(x):
    if x == 1 or x == 0:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

intCount = 2
primeCount = 0
lineCount = 0

while (primeCount < 1000):
    if isPrime(intCount):
        primeCount += 1
        lineCount += 1
        
        if (lineCount == 10):
            print(intCount)
            lineCount = 0
        else:
            print(intCount, end='\t')
    
    intCount += 1

