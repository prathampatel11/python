
month_number = int(input("enter_the_value_of_month_number="))

if month_number==2:
    print("this_month_has_28/29_days")
    exit()

if month_number==1 or month_number==3  or month_number==5 or  month_number==7 or month_number==8 or month_number==10 or month_number==12:
    print("this_month_has_31_days")  

else:
    print("this_month_has_30_days")