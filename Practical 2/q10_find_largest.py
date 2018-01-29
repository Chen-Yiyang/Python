# Finding the largest n such that n3 < 12000
# by Yiyang 29/01/18

N = 1

while (N ** 3 <= 12000):
    N += 1

print(N-1)