# Computing the greatest common divisor
# by Yiyang 29/01/18

N1 = int(input())
N2 = int(input())

if N1 > N2:
    N1, N2 = N2, N1     # swap N1 and N2

while (N2 % N1 != 0):
    N2 = N2 % N1
    N1, N2 = N2, N1

print(N1)
    