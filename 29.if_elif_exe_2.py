
num_1 = int(input("enter the num_1 ="))
num_2 = int(input("enter the num_2 ="))

choice = int(input("enter your choice ="))

if choice==1:
    addition = num_1 + num_2
    print("your choice is addition =",addition)

elif choice==2:
    substraction = num_1 - num_2
    print("your choice is substraction =",substraction)

elif choice==3:
    multiplication = num_1 * num_2
    print("your choice is multiplication =",multiplication)

elif choice==4:
    division = num_1  / num_2
    print("your choice is division =",division)

else:
    print("your choice is invalid")
