year = int(input("Enter year here: "))
if (year % 4)==0 or (year % 400)==0:
    if (year % 100)==0 and (year % 400)!=0:
        print("Non-leap year")
    else:
        print("leap year")
else:
    print("Non-leap year")
