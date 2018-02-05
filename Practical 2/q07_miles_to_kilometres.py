# Conversion from miles to kilometres
# by Yiyang 29/01/18

print("Miles\tKilometers\tKilometers\tMiles")

for i in range(10):
    print("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(i+1, (i+1) * 1.609, (i * 5 + 20), (i * 5 + 20)/1.609))

# are there any other ways to print such columns other than \t ?
# you can use column width in the format specifier eg {0:10} will reserve 10 columns for the first value
