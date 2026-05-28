#  write a program to count positive & negative number in numeric list 

number = [5, -3, 12, -7, 9, -1, 15, -10, 2, -8,
           6, -4, 11, -15, 7, -2, 14, -9, 3, -6,
           1, -12, 8, -5, 13, -11, 4, -14, 10, -13]

print(number)

positive_number =0
negative_number =0

for item in number:
    if item>0:
        positive_number+=1
        
    elif item<0:
        negative_number+=1


print("positive number",positive_number)
print("negative number",negative_number)
