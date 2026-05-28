# 4) write a program to count digits in given string 

name = input("Enter your word")

digit = 0
for item in name:
    if item >='0' and item<='9':
        print(item)
        digit = digit + 1
print('*'*50)
print(digit)