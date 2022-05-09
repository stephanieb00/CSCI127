#Stephanie Bravo
#February 6,2019
#This code will prompt the user for DNA string and then prints lenfth of the GC content

Message = input("Enter a DNA string:")

#Compute the Length of the input:
l = len(Message)
print("The length is",l)

#Compute amount of C and G in the input:
numC = Message.count('C')
numG = Message.count('G')

#Compute the GC-content:
gc = (numC + numG)/l

gcPercent = gc
print("GC-content is", gcPercent)
