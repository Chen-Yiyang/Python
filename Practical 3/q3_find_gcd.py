# Computing GCD
# by Yiyang 04/02/18

def gcd(x, y):
    
    if x > y:
        x, y = y, x
    
    while (y % x != 0):
        y = y % x
        x, y = y, x
    
    return x

print("The greatest common divisor between 24 and 16 is", gcd(24,16))
print("The greatest common divisor between 255 and 25 is", gcd(255,25))