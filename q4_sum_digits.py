__author__ = 'jinya_000'

x = float(input("Enter a digit between 0 to 1000: "))
sum = (x%10) + (x//10)%10 + ((x//10)//10)%10
print("The sum of the digits is: " + str(sum))