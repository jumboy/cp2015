from fractions import gcd
number_1 = int(input("Enter number here: "))
number_2 = int(input("Enter second number here: "))
ans = gcd(number_1,number_2)
print("The greatest common factor is: " + str(ans))
