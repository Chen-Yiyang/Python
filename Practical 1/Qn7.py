# Payroll
# by Yiyang 14/01/18

# input
userName = input("Enter name: ")
weeklyHours = int(input("Enter number of hours worked weekly: "))
hourlyPay = float(input("Enter hourly pay rate: "))
CPFRate = int(input("Enter CPF contribution rate(%): "))

# calculation
grossPay = weeklyHours * hourlyPay
CPFDistribution = CPFRate / 100 * grossPay
netPay = grossPay- CPFDistribution

# output
print("Payroll statement for", userName)
print("Number of hours worked in week:", weeklyHours)
print("Hourly pay rate: ${0:.2f}".format(hourlyPay))
print("Gross pay = ${0:.2f}".format(grossPay))
print("CPF contribution at {0}% = ${1:.2f}".format(CPFRate, CPFDistribution))
print("Net pay = ${0:.2f}".format(netPay))
