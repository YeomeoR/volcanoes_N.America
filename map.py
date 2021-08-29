import folium
import pandas as pd

data = pd.read_csv("Volcanoes.csv")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = """<h4>Volcano information:</h4>"""

def height_range(elev):
    if elev < 1500:
        return 'green'
    elif 1500 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[40.58,-100], zoom_start=5, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcano Map")

for lt,ln,el,nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(radius=6,location=[lt,ln],popup=html + "\n" + "Name: \n" + nm + "." + "\n" + "Elevation(M): \n" + str(el), fill_color=height_range(el), color='gray', fill_opacity=0.7))
   
fgp = folium.FeatureGroup(name="Population")
 
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'darkred' }))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")
