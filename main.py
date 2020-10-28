import folium
import pandas

data = pandas.read_csv("volcano.csv", encoding="cp1252")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
pro = list(data["PROVINCE"])
elev = list(data["ELEVATION"])
picture = list(data["PICTURE"])
VolName = list(data["NAME"])

mapworld = folium.Map(location=[6.160066, 125.116242], zoom_start=5)

mapVolcano = folium.FeatureGroup(name="Volcanoes")

for latitude, longitude, volcanoName, province, elevation, pic in zip(lat, lon, VolName, pro, elev, picture):
    mapVolcano.add_child(folium.Marker(location=[latitude, longitude]
                                       , popup="<b> Name: </b> Mt." + volcanoName + "<br> <b> Place: </b> " + province +
                                               "<br>" + " <b>Elevation:</b> " + str(elevation) + " m" + "<br>" +
                                               "<img src=" + pic + " height=142 width=290>", marker_color="yellow"))
    # fill_color=elevationParameters(volcanoName),
    # fill_opacity=0.7))

mapPopulation = folium.FeatureGroup(name="Population")
mapPopulation.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                       style_function=lambda x: {
                                           'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                           else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                           else 'red'}))

mapworld.add_child(mapVolcano)
mapworld.add_child(mapPopulation)
mapworld.add_child(folium.LayerControl())
mapworld.save("firstMap.html")
