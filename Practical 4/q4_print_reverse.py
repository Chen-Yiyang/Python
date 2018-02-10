# Reverse the digits in an integer recursively using Recursion
# by Yiyang 09/02/18

def reverse_int(numStr):
    if len(numStr) == 1:
        return numStr
    else:
        return reverse_int(numStr[1:]) + numStr[0]


# main

numStr = input("Enter the number: ")          # store the number as a string
print(reverse_int(numStr))
