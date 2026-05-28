# write a program to calculate sum and average of  values in list

values = [5, 12, 8, 20, 15, 7, 3, 18, 25, 10, 6, 14, 9, 30, 22]

total =0
for item in values:
    total = item + total
    
    average =total / len(values)
    
print(total)    
print(average)    