number = int(input("Enter an integer: "))
factors = []
factor = 2
while number%factor == 0:
    factors.append(factor)
    number = number/factor
while number%factor != 0:
    factor += 1
    while number%factor == 0:
        factors.append(factor)
        number = number/factor
        if number == 1:
            print("The factors are: " + str(factors))
