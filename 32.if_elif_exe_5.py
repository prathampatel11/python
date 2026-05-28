
# 1=0
# 2=3
# 3=3
# 4=6
# 5=1
# 6=4
# 7=6
# 8=2
# 9=5
# 10=0
# 11=3
# 12=5

date =int(input("enter the date"))
month =int(input("enter the month"))
year =int(input("enter the year"))


week = date + month
print(week)

week = week -date 
print(week)

if week>6:
    day =date * 7
    day = day - week
    print(day)

    

