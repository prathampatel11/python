month_number = int(input("enter the month number ="))

if month_number == 1 or month_number == 3 or month_number == 5 or month_number ==7 or month_number == 8 or month_number == 10 or month_number == 12:
    print("this month has 31 days.")

elif month_number == 2:
    print("this month has 28/29 days.")

elif month_number ==4 or month_number == 6 or month_number ==9 or month_number == 11:
    print("this month has 30 days.")

else:
    print("month number in valid")