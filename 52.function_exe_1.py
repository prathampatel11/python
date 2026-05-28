# -----------------------------
# write a program to create function that convert & return given fahrenheit into celsius 
 
def getcelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

fehrenheit =float (input("Enter Fahrenheit value:"))
celsius = getcelsius(fehrenheit)
print ("Temperature in Celsius is:", celsius)