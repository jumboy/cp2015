print("Miles", "Kilometers", "Kilometers", "Miles")
for x in range(1,11):
    new_line = x*5
    print("{0:<6}{1:<11}{2:<11}{3:<.5}".format(x,x*1.609,new_line+15,(new_line+15)/1.609 ))
