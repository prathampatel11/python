
hours = float(input("enter_the_value_of_an_hours="))
 
hours = hours
if hours>=25:
    print("notavalid")
    exit()

if hours>=12 and hours<=24:
     time =hours - 12
     print(time,"P.M.")

else :
    print(hours,"A.M.")

