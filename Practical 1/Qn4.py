# Summing the digits in an integer
# by Yiyang 14/01/18

_no = int(input("The integer is "))
_no1 = _no # copy the number for calculation
_sum = 0


while (_no1 > 0):
    _sum += _no1 % 10
    _no1 //= 10

print("The summation of all the digits of {0} is {1}".format(_no, _sum))