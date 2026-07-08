import module_P as m

print("hello welcome to my project.")
print("let's learn python language")

while True:
    
    print("\nPress 1 for learn introduction,overview and history, ")
    print("Press 2 for learn oprater")
    print("Press 3 for learn ")
    print("Press 4 for Report management")
    print("Press 0 for Exit")

    choice=int(input("enter the choice= "))

    if choice<0 or choice>5:
            print("invalid choice.")

    else:
        if choice==1:
           print("let's know introduction,overview and history of python language.")
           
           while True:
                print("\nPress 1 for about introduction to python.")
                print("Press 2 for about overview to python.")
                print("Press 3 for knew history of python.")
                print("Press 4 for knew advantage of python.")
                print("Press 5 for knew feature of python.")
                print("Press 6 for knew application of python.")
                print("Press 7 for knew use of python.")
                print("Press 0 for exit.")

                choice=int(input("enter your choice="))

                if choice<0 or choice>7:
                        print("invalid choice.")

                else:

                        if choice==1:
                            m.introduction()
                        
                        elif choice==2:
                            m.overview()

                        elif choice==3:
                            m.history()

                        elif choice==4:
                            m.advantage()
                        
                        elif choice==5:
                            m.feature()
                    
                        elif choice==6:
                            m.application()
                        
                        elif choice==7:
                            m.uses()
                        
                        else:
                            print("exit to main menu.")
                            break       

        elif choice==2:
            print("let's strat to learn python's oprater.")
            
            while True:
                print("\nPress 1 for Arithmetic Operators.")
                print("Press 2 for Comparison (Relational) Operators.")
                print("Press 3 for Assignment Operators.")
                print("Press 4 for Logical Operators.")
                print("Press 5 for Membership Operators.")
                print("Press 0 for Exit.")

                oprater=int(input("\nenter your choice="))
            
                if oprater<0 or oprater>7:
                    print("\ninvalid choice.")
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


        else:
            print("exit to program.")
            break
