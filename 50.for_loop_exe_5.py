# 5) write a program to count vowels, consonants, digits, words, and symbol in given list 
 
name = input("Enter your word")

vowels =0
consonant=0
words=1
digit=0
symbol=0
for letter in name:
    if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter =='E' or letter == 'I' or letter == 'O' or letter == 'U':    
            vowels += 1
               
    elif letter ==' ':
          words+=1
    
    elif letter>='0' and letter<='9':
          digit+=1
    
    elif letter == 'b' or letter == 'c' or letter == 'd' or letter == 'f' or letter == 'g' or \
   letter == 'h' or letter == 'j' or letter == 'k' or letter == 'l' or letter == 'm' or \
   letter == 'n' or letter == 'p' or letter == 'q' or letter == 'r' or letter == 's' or \
   letter == 't' or letter == 'v' or letter == 'w' or letter == 'x' or letter == 'y' or \
   letter == 'z' or letter == 'B' or letter == 'C' or letter == 'D' or letter == 'F' or \
   letter == 'G' or letter == 'H' or letter == 'J' or letter == 'K' or letter == 'L' or \
   letter == 'M' or letter == 'N' or letter == 'P' or letter == 'Q' or letter == 'R' or \
   letter == 'S' or letter == 'T' or letter == 'V' or letter == 'W' or letter == 'X' or \
   letter == 'Y' or letter == 'Z':
          consonant+=1        
    
    else:
          symbol+=1
          
         
print("vowels=",vowels)
print("consonants=",consonant)
print("words=",words)
print("digit=",digit)
print("symbol=",symbol)
    