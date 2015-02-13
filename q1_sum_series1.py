i = int(input("Enter an integer: "))
def sum_series(i):
    if i == 1:
        return 1
    if i>1:
        return ((1/i)+sum_series(i-1))
    if i<1:
        return "Integer must be above 1"
print(sum_series(i))
