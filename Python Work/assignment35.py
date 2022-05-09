#Stephanie Bravo
#March 15, 2018
#This program will take inputed information and print out the first name and last names of people.
##

#list of names:
names = input("Please enter your list of names:")
#names = "Cohn, Mildred; Dolciani, Mary P.; Rees, Mina; Teitelbaum, Ruth; Yalow, Rosalyn"
#split the list by person (;)
nombres = names.split("; ")

l = len(nombres)

for i in range(l):
    nombres2 = nombres[i].split(", ")
    print(nombres2[1],nombres2[0])
