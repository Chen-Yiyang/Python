# Summing series using Recursion
# by Yiyang 09/02/18

# the series:
# m(n) = sigma(i / (2i + 1)), i = 1 to n

calcValues = {1:1/3}             # use a dict to store the calculated values in the series to reduce repeated work, default value m(1)

def sum_series1(num):
    
    if num in calcValues:
        return calcValues[num]
    else:
        calcValues[num] = sum_series1(num-1) + num / (2 * num + 1)
        return calcValues[num]

# main
num = int(input("Enter the number n for series m(n): "))
print("m({0}) = {1:.5f}".format(num, sum_series1(num)))