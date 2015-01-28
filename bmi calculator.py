__author__ = 'jinyang_000'

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

bmi = weight/(height*height)
print("\n")
print("your bmi is:" + str(bmi))

if bmi <= 18.5:
    print("You are currently underweight")
if 18.5<bmi<24.9:
    print("your weight is acceptable")
if 25<bmi<29.9:
    print("You are currently overweight")
if bmi > 30:
    print("you are currently severely overweight")




