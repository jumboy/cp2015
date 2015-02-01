side_1 = int(input("Enter length of side 1: "))
side_2 = int(input("Enter length of side 2: "))
side_3 = int(input("Enter length of side 3: "))

a = side_1 + side_2
b = side_2 + side_3
c = side_1 + side_3

if a>side_3 and b>side_1 and c>side_2:
    perimeter = int(side_1 + side_2 + side_3)
    print("perimeter of triangle: " + str(perimeter))
else:
    print("invalid")
