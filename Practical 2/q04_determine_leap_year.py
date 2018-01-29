# Determining leap year
# by Yiyang 29/01/18

_year = int(input("Enter year: "))

if (_year % 4 == 0 and _year % 100 != 0) or (_year % 400 == 0):
    print("Leap")
else:
    print("Non-Leap")