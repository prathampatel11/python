
name = input("Enter your name =")

vowels = 0
for letter in name:
        if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter =='E' or letter == 'I' or letter == 'O' or letter == 'U':    
            vowels = vowels + 1
 
print("total vowels =",vowels)