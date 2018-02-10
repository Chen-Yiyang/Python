# Computing greatest common divisor using Recursion
# by Yiyang 09/02/18

def gcd(m, n):              # m and n, two parameters, the numbers whose gcd to be found, always m < n
    
    if n % m == 0:
        return m
    else:
        return gcd(n%m, m)


# main

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    gcdValue = gcd(num2, num1)
else:
    gcdValue = gcd(num1, num2)
print("The greatest common divisor for {0} and {1} is {2}.".format(num1, num2, gcdValue))
print("The greatest common divisor for {0} and {1} is {2}.".format(24, 16, gcd(24, 16)))
print("The greatest common divisor for {0} and {1} is {2}.".format(255, 25, gcd(255, 25)))