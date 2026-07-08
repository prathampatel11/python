from datetime import datetime as dt 

#create datetime type object 
dt = dt.now()

husband=input("enter husband's birth_date=")
wife=input("enter wife's birth_date=")

date_1= dt.strptime(husband,"%d-%m-%Y")
date_2= dt.strptime(wife,"%d-%m-%Y")

if date_1>date_2:
    print("husband is older and wife is younger.")

elif date_1>date_2:
    print("husband and wife both are same.")

else:
    print("husband is younger and wife is older.")
