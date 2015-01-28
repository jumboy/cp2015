__author__ = 'jinya_000'

name = input("Enter name here: ")
hours = float(input("Enter number of hours worked weekly: "))
pay = float(input("Enter hourly pay rate in dollars: "))
cpf = float(input("Enter CPF contribution rate without percentage symbol: "))
gross_pay = float(7*pay*hours)
cpf_contribution = (cpf/100)*gross_pay
net_pay = gross_pay - cpf_contribution
print("\n")

print("Payroll statement for " + str(name))
print("Number of hours worked in a week: " + str(hours))
print("Enter hourly pay rate: " + str(pay))
print("Gross pay = " + str(gross_pay))
print("CPF contribution = " + str(cpf_contribution))
print("Net pay = " + str(net_pay))


