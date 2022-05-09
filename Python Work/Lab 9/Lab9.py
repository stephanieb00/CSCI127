#Import the folium package for making maps and pandas
import folium
import pandas as pd

cuny= pd.read_csv("cunyLocations.csv")

#Create a map, centered around hunter
mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():
    lat= row["Latitude"]
    lon= row["Longitude"]
    name= row["Campus"]
    newMarker = folium.Marker([lat,lon], popup=name)
    newMarker.add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile='cunyLocations.html')
#You can use the CSV file. this can be found on Lab 9.
