def arethematic_oprater():
            print("hello welcome let's learn to first oprater." \
                        "\nfirst oprater is arithmetic oprater.")
            
            A=int(input("\nenter the value of an A="))
            B=int(input("enter the value of a B="))
                       
            print("\naddition=",A+B)
            print("substraction=",A-B)
            print("multiplication=",A*B)
            print("division=",A/B)

            print("\nmodulas=",A%B)
            print("exponent=",A**B)
            print("floor_division =",A//B)

            print("\nend of the first oprater.")  

def relational_oprater():
        print("\nwelcome let's learn to second oprater." \
              "\nsecond oprater is comparison(relational) oprater.")                    

        A=int(input("\nenter the value of an A="))
        B=int(input("enter the value of a B="))            
        
        print("relational oprater's return value only for 2(two). " \
        "\nfirst_value=true " 
        "\nsecond_value=false")
                    
        print("\n==",A==B)
        print("!=",A!=B)
        print(">",A>B)
        print("<",A<B)
        print(">=",A>=B)
        print("<=",A<=B)

        print("\nend of the second oprater.") 

def assignment_oprater():
        print("\nwelcome let's learn to third oprater." \
                        "\nthird oprater is asssignment oprater.")

        A=int(input("\nenter the value of an A="))
        B=int(input("enter the value of a B=")) 

        A+=B
        print(f"\nafter a+=b value of A= {A} b = {B}")

        A-=B
        print(f"after a-=b value of A= {A} B = {B}")

        A*=B
        print(f"after a*=b value of A= {A} B = {B}")

        A/=B
        print(f"after a/=b value of A= {A} B = {B}")

        A**=B
        print(f"after a**=b value of A= {A} B = {B}")

        A//=B
        print(f"after a//=b value of A= {A} B = {B}")

        A%=B
        print(f"after a%=b value of A= {A} B = {B}")
                     
        print("\nend of the third oprater.")

def logical_oprater():
        print("\nwelcome let's learn to fourth oprater." \
                            "\nfourth oprater is logical oprater.") 
                    
        A=int(input("\nenter the value of an A="))
        B=int(input("enter the value of a B=")) 
        C=int(input("enter the value of a C="))
                        
        result = A < B and B < C
        print(f"\n{result}  {A}<{B} and {B}<{C}")
                       
        result = A == B and B == C
        print(f"{result}  {A}=={B} and {B}=={C}")
                        
        result = C > B and B < A
        print(f"{result}  {C}>{B} and {B}<{A}")
                        
        result = A < B or B > C
        print(f"{result}  {A}<{B} or {B}>{C}")

        result = A == B or B == C
        print(f"{result}  {A}=={B} or {B}=={C}")

        result = not (A == B)
        print(f"{result} = not {A} == {B}")

        print("\nend of the fourth oprater.")

def membership_oprater():
        print("\nwelcome let's learn to fifth oprater." \
                "\nfifth oprater is membership oprater.") 

        favourite_fruit = str(input("enter fruit"))
        fruits = "banana mango pineapple apple "
        print(fruits)
        result = favourite_fruit in fruits
        print(result)

        result = favourite_fruit not in fruits
        print(result)   

        print("\nend of the fifth oprater.")

