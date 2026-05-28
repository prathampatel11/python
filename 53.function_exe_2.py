
''' write a program to create function that calculate and return simple interest 
 of given amount rate and year'''


def getreturnsimpleinterest(amount, rate, year):
    simpleintrest =(amount*rate*year)/100
    return simpleintrest

amount =int(input("enter your amount: "))
rate =int(input("enter your rate: "))
year =int(input("enter your year: "))

simpleinterest= getreturnsimpleinterest(amount, rate, year)
print("Simple Interest is:", simpleinterest)