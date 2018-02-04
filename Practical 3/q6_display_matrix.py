# Displaying matrix of 0s and 1s
# by Yiyang 03/02/18

import random       # for random numbers

matrixSize = int(input())

for i in range(matrixSize):
    for j in range(matrixSize):
        print(random.randint(0,1), end = ' ')
    print()     # i.e. '\n'
