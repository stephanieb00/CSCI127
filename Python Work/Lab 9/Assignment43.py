#Stephanie Bravo
#April 3, 2019
#This program will creates a map with markers for all the traffic collisions from the input file.

import folium
import pandas as pd

#Ask for the CSV file

cuny= pd.read_csv(input("Enter CSV file name:"))
outputfile = input("Enter output file:")

#Create a map, centered around hunter
mapCUNY = folium.Map(location=[40.75, -74.125])
for index,row in cuny.iterrows():
    lat= row["LATITUDE"]
    lon= row["LONGITUDE"]
    newMarker = folium.Marker([lat,lon])
    newMarker.add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile = outputfile)


# columns names are "LATITUDE" and "LONGITUDE"

#"TIME") to label each marker and changed
#the underlying map with the option: tiles="Cartodb Positron" when creating the map.)
