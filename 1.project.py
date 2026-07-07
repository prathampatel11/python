import module_P as m
print("hello welcome to my project.")

print("\nPress 1 for learn oprater")
print("Press 2 for Bill management")
print("Press 3 for Report management")
print("Press 0 for Exit")

choice=int(input("enter the choice= "))


if choice<0 or choice>5:
        print("invalid choice")

else:
    if choice==1:
        print("let's strat to learn oprater.")
        while True:
            print("\nPress 1 for Arithmetic Operators")
            print("Press 2 for Comparison (Relational) Operators")
            print("Press 3 for Assignment Operators")
            print("Press 4 for Logical Operators")
            print("Press 5 for Membership Operators")
            print("Press 0 for Exit")

            oprater=int(input("\nenter your choice="))
        
            if oprater<0 or oprater>7:
                print("\ninvalid choice")
            else:
                
                if oprater==1:
                    m.arethematic_oprater()   

                elif oprater==2:
                    m.relational_oprater()

                elif oprater==3:
                    m.assignment_oprater()

                elif oprater==4:
                    m.logical_oprater()

                elif oprater==5:
                    m.membership_oprater()

                else:
                     print("exit to main menu.")
                     break