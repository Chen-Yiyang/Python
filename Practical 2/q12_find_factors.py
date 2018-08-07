# Finding the factors of an integer
# by Yiyang 29/01/18
# gisc: avoid single letter variables and underscore prefix _ in identifier names
N = int(input())
i = 2 # i is the factor & the iterator
_first = True # for the printing format

while (N >= i):
    if (N % i == 0):
        N /= i # use integer divisor // in Python 3
        if _first == True:
            print(i, end='')
            _first = False
        else:
            print(',', i, end='')
    else:
        i += 1

print('.')
