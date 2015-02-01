score = int(input("Enter score here: "))
if 0<score<=35:
     print("U")
if 35<score<=45:
     print("S")
if 45<score<=50:
     print("E")
if 50<score<=55:
     print("D")
if 55<score<=60:
     print("C")
if 60<score<=70:
     print("B")
if 70<score<=100:
     print("A")
if score<0 or score>100:
    print("Invalid! Your number must be between 0 to 100")
