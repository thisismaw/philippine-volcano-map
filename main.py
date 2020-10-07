import folium
map = folium.Map(location=[6.160066, 125.116242], zoom_start=12)

map.add_child(folium.Marker(location=[6.160066, 125.116242], popup="Home", icon=folium.Icon(color="green")))


map.save("firstMap.html")
