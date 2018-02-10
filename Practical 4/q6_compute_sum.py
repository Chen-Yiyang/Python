# Summing the digits in an integer using Recursion
# by Yiyang 10/02/18

# recursion
def sum_digits(numStr):
    
    if len(numStr) == 1:
        return int(numStr[0])
    else:
        return int(numStr[0]) + sum_digits(numStr[1:])


# main
numStr = input("Enter the integer: ")

print("The sum of the digits in {0} is {1}.".format(numStr, sum_digits(numStr)))