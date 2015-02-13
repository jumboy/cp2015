i = int(input("Enter an integer: "))
def sum_series2(i):
    if i == 1:
        return 1/3
    if i>1:
        return (i/((i+i)+1))+sum_series2(i-1)
    if i<1:
        return "Please enter an integer above 1"
print(sum_series2(i))
