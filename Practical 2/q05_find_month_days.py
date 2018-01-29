# Finding the number of days in a month
# by Yiyang 29/01/18

def _leap(x): # used to test if its leap year and if yes, adjust the days by +1
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return 1
    else:
        return 0

monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

monthValue = int(input("Month: "))
yearValue = int(input("Year: "))

print("{0} {1} has {2} days.".format(monthName[monthValue-1], yearValue, monthLength[monthValue-1] + _leap(yearValue)))