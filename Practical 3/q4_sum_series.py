# Summing series
# by Yiyang 03/02/18

m = []
m.append(0)     # let m[0] = 0 for standardisation of the series

print("i\tm(i)")

for i in range(20):
    m.append(m[i] + (i+1)/(i+2))
    print("{0}\t{1:.4f}".format(i+1, m[i+1]))