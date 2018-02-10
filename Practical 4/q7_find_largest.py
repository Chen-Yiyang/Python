# Finding the largest number in an array using recursion
# by Yiyang 10/02/18

# recursion
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        tmp = find_largest(alist[1:])
        return tmp if tmp > alist[0] else alist[0]

# main
arrSize = int(input("Enter the size of the array: "))
alist = []

for i in range(arrSize):
    alist.append(int(input()))

print("The largest element in the array is {0}.".format(find_largest(alist)))