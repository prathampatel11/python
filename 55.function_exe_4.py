# write a program that return current Time (google search)

# write a program that will find and print maximum number from 2 numbers.
 
# write a program that will find and print maximum number from list, user will pass list as argument in function. 

# write a program that will calculate and display sum of even value into list. user will pass list as argument in function. 
import time

def get_current_time(am_pm=False):
    if am_pm:
        return time.strftime("%I:%M:%S %p")  
    return time.strftime("%H:%M:%S")        
         
print(get_current_time(am_pm=True)) 
