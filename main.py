import folium
import pandas

data = pandas.read_csv("volcano.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
elev = list(data["ELEV"])

map = folium.Map(location=[6.160066, 125.116242], zoom_start=12)


def elevationParameters(elevate):
    if elevate < 1000:
        return "green"
    elif 1000 <= elevate < 2000:
        return "red"
    else:
        return "red"


mapFeatureGroup = folium.FeatureGroup(name="Volcanoes")

for ltitude, lngitude, elevation in zip(lat, lon, elev):
    mapFeatureGroup.add_child(folium.CircleMarker(location=[ltitude,lngitude], radius=7, popup=str(elevation)+"m",
                                                  fill_color=elevationParameters(elevation), color="grey", fill_opacity=0.7))

mapFeatureGroup.add_child(folium.GeoJson(data = (open('world.json','r', encoding='utf-8-sig').read())))

map.add_child(mapFeatureGroup)
map.save("firstMap.html")
