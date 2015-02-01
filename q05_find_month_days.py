import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(calendar.month_name[month], year, "has a total of", calendar.monthrange(year,month)[1], "days")
