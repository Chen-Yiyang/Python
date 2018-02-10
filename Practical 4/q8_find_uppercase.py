# Finding the number of uppercase letters in a string using recursion
# by Yiyang 10/02/18

# function checking if uppercase
def is_uppercase(strValue):
    if ord('A') <= ord(strValue[0]) <= ord('Z'):
        return True
    else:
        return False

# recursion
def find_num_uppercase(strValue):
    
    if len(strValue) == 1:
        return 1 if is_uppercase(strValue[0]) else 0
    else:
        return  find_num_uppercase(strValue[1:]) + (1 if is_uppercase(strValue[0]) else 0)


# main
strValue = input("Enter the string: ")
print("The number of uppercase letters in the given string is {0}.".format(find_num_uppercase(strValue)))