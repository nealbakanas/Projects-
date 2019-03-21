import pandas as pd
import folium

data = pd.read_excel('ParkData.xlsx')

names = list(data['Name'])
visitors = list(data['Visitors'])
latlon = list(data['Coordinate'])

lat = [float(item.split()[0][:-1]) for item in latlon]
lon = [float('-'+str(item.split()[1][:-1])) for item in latlon]



def color_points(visits):
    if visits < 1000000:
        return 'red'
    elif visits<2000000:
        return 'orange'
    elif visits<300000:
        return 'yellow'
    else:
        return 'green'


test = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name='Parks')

for lt,ln,name,vs in zip(lat,lon,names,visitors):
    # print (lt,ln,name,vs,color_points(vs))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=name+' '+str(vs) + " visitors",
                                      fill_color=color_points(vs), fill=True, color='grey', fill_opacity=0.7))

# fgp = folium.FeatureGroup(name="Population")
#
# fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))





test.add_child(fgv)

test.save("Map2.html")
