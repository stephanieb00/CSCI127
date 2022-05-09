#Stephanie Bravo
#April 3, 2019
#This program will use folium to make a map centered (40.75, -74.125) and include a marker of Hunter College.

import folium

#Create a map, centered around hunter
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start= 10)
folium.Marker(location=[40.768731, -73.964915], popup= "Hunter College").add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile="nycMap.html")
