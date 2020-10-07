import folium
import pandas

data

map = folium.Map(location=[6.160066, 125.116242], zoom_start=12)

mapFeatureGroup = folium.FeatureGroup(name="Explored Horizons")
mapFeatureGroup.add_child(folium.Marker(location=[6.160066, 125.116242], popup="Home", icon=folium.Icon(color="green")))
map.add_child(mapFeatureGroup)

map.save("firstMap.html")
