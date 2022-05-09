import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

#Tells the computer to plot the year as x and for y to plot only manhattan.
#If you dont specify anything all the colomns will be shown. 
##pop.plot(x = "Year", y = "Manhattan")
##plt.show()

print("The largest number living in the Bronx is", pop["Bronx"].max())

print("The average number living in Queens is", pop["Queens"].mean())

print("The standard deviation of living in Brooklyn is", pop["Brooklyn"].std())

print("The minimum number living in Stanten Island is", pop["Staten Island"].min())

print("The numbersof the data of Queens is", pop["Queens"].count())

print(pop["Queens"]/2) ##divide every number by 2

print (pop["Bronx"]/pop["Total"])

pop["Fraction"] = pop["Queens"]/pop["Total"]

pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()
fig.savefig('fractionBX.png')


