def introduction():
        intro="""\n▫ Python is a general-purpose interpreted, interactive,
object-oriented,and high-level programming language.
▫ Python is easy to learn and use.
▫ Python source code is also available under the GNU
GeneralPublicLicense(GPL). General PublicLicense(GPL).
▫ Latest version of python is python 3.14 at the time of
updating presentation last time.
"""

        print("introduction =",intro)

def overview():
        o_v="""\n▫ Python can be used to develop large sized application like
bankingsoftware , ERPapplication.
▫ It uses English keywords frequently so it is easy to
understandlanguage.
▫ Python is a great language for the beginner-level
programmers.
"""
        print("overview =",o_v)

def history():
        his="""\n▫ Python was developed by Guidovan Rossum in 1980
1990 at the National Research Institute for
Mathematics and Computer Science in the
Netherlands.
▫ Python is named after the comedy television show
Monty Python's Flying Circus. It is not named after the
Pythonsnake. 
▫ Python is inspired(learnedfrommistake) from many
other languages, including ABC,Modula-3, C, C++,
Algol-68,SmallTalk,and Unixshell and other scripting
languages."""
        print("history =",his)

def advantage():
        a_v="""\n▫ 1.Readable:-Python is a very readable language.
▫ 2.Easy to Learn:-Learning python is easy as this is a expressive and highlevel
programming language.
▫ 3.Cross platform:-Python is available and can run on various operating systems.
▫ 4.Open Source:-Python is a open source programming language.
▫ 5.Large standard library:-Python comes with a large standard library that has
some ready to use functions which we can use while writing code in Python.
▫ 6.Free:-Python is free to download and use.
▫ 7.Supports exception handling:-python can handle run time errors so program
do not stop suddenly.
▫ 8. Automatic memory management: Python supports automatic memory
management which means the memory is cleared and freed automatically.You do
not have to clear the memory."""
        print("advantage of python=",a_v)

def feature():
        f_t="""\n▫ It supports POP as well as OOP technique.
▫ It can be used as a scripting language or can be
compiled to byte-code for building large applications.
▫ Inpythonwecanstoreanytypeofvalueinanyvariable.
▫ It can be easily integrated with other programming
language."""

def application():
        a_c="""▫ 1. Web development – Web framework like Django and Flask are based on Python. They 
help you write server side code which helps you manage database, write backend 
programming logic, mapping urlsetc.
▫ 2. Machine learning – There are many machine learning applications written in Python. 
Machine learning is a way to write a logic so that a machine can learn and solve a 
particular problem on its own. For example, products recommendation in websites like 
Amazon, Flipkart, eBay etc. is a machine learning algorithm that recognisesuser’s Amazon, Flipkart, eBay etc. is a machine learning algorithm that recognisesuser’s 
interest. 
▫ 3. Data Analysis – Data analysis and data visualization in form of charts can also be 
developed using Python.
▫ 4. Scripting – Scripting is writing small programs to automate simple tasks such as 
sending automated response emails etc. Such type of applications can also be written in 
Python programming language.
▫ 5. Game development – You can develop games using Python.
▫ 6. You can develop embedded applications in Python.
▫ 7. Desktop applications – You can develop desktop application in Python using library like 
TKinteror QT."""

        print("where it can be used=",a_c)

def uses():
        use="""▫ Python can be used on a server to create web
applications.
▫ Python can be used together with software to create
workflows.
▫ Python can connect to database systems. It can also read and modify files.
▫ Python can be used to handle big data and perform
complex mathematics(datamining).
▫ Python can be used for rapid prototyping, or for
production-ready software development."""
        print("python can be used=",use)


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

