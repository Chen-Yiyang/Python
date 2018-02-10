# Occurrences of a specified character in a string using Recursion
# by Yiyang 10/02/18

# recursion
def count_letter(strValue, charValue):
    
    if len(strValue) == 1:
        return 1 if strValue[0] == charValue[0] else 0
    else:
        return count_letter(strValue[1:], charValue) + (1 if strValue[0] == charValue[0] else 0)


# main
strValue = input("Enter the string: ")
charValue = input("Enter the character to be found: ")

print("The number of occurrences of {0} in the given string is {1}.".format(charValue, count_letter(strValue, charValue)))