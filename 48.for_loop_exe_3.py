# 3) write a program to count words in given string (hit count space)

name = input("Enter your name")

word = 1
for letter in name:
    if letter==' ':
        print(letter)
        word = word + 1

print(word)