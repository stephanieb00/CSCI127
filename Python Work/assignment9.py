#Stephanie Bravo
#February 1, 2019
#This program prints out each letter, shifted right by 13, in the word the user enteres

message = input("Enter a word:")
coded = ""
for ch in message:
     offset = ord(ch) - ord('a') + 13 #tells the computer to add 13
     wrap = offset % 26 #lets the computer know that when at 26 go back to 0
     newChar = chr(ord('a')+ wrap) 
     coded= coded + newChar

print("Your word in code is:", coded)
