import folium
import pandas

def elevation_color(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation > 3000:
        return 'red'
    else:
        return 'orange'

data = pandas.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data['ELEV'])
name = list(data['NAME'])

popup_html = """
<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br />
<p>Height: %s m </p>
"""

map = folium.Map(location = [30, -120], zoom_start = 5)

volcano_fg = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, el, n in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=popup_html % (n, n, str(el)), width = 200, height = 100)

    volcano_fg.add_child(folium.CircleMarker(location=[lt, ln], popup = folium.Popup(iframe), radius = 5, color = 'grey', weight = 1, fill=True, fill_color = elevation_color(el), fill_opacity = 0.7))

map.add_child(volcano_fg)

population_fg = folium.FeatureGroup(name = 'World Population')

population_color = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}

with open('world.json', 'r', encoding = 'utf-8-sig') as file:
    world_pop_data = file.read()

population_fg.add_child(folium.GeoJson(data = world_pop_data, style_function = population_color ))

map.add_child(population_fg)
map.add_child(folium.LayerControl())

map.save('Map1.html')