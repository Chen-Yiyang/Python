# Converting an uppercase letter to lowercase
# by Yiyang 14/01/18

_charU = input("The uppercase letter is ")

_valueU = ord(_charU)    # ord() return the ascii value of the char
_valueL = _valueU + 97 - 65    # convert it to lowercase as the ascii of 'A' & 'a' are 65 and 97 respectively
_charL = chr(_valueL)    # chr() return the corresponding char of the given ascii value

print("The lowercase letter is", _charL)