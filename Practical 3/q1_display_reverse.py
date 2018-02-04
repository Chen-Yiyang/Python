# Displaying an integer reversed
# by Yiyang 03/02/18

def reverse_int(n):
    
    nRev = 0
    
    while n > 0:
        nRev = nRev * 10 + n % 10
        n = int(n/10)       # otherwise n will be saved as float
    
    return nRev

n = int(input())
print(reverse_int(n))