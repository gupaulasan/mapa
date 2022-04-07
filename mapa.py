import folium
import webbrowser
#inicializar o mapa
city_map = folium.Map()
#definir os pins no mapa
green_cities = [
    {'loc':(-30.0368,-51.2090),'label':'Porto Alegre'},
    {'loc':(-26.9980,-48.6326),'label':'Balneário Camboriú'},
    {'loc':(-25.4372,-49.2700),'label':'Curitiba'},
    {'loc':(-23.5558,-46.6396),'label':'São Paulo'}]
white_cities = [
    {'loc':(-27.6015,-48.5165), 'label':'Florianópolis'},
    {'loc':(-22.14714,-51.42874),'label':'Presidente Prudente'},
    {'loc':(45.2757,-75.7203),'label':'Ottawa'},]
cisv_cities = [
    {'loc':(-21.7791,-48.1793),'label':'Araraquara'},
    {'loc':(-20.3197,-40.3385),'label':'Vitória'},
    {'loc':(-12.9777,-38.5016),'label':'Salvador'},
    {'loc':(14.6349,-90.5069),'label':'Cidade da Guatemala'},
    {'loc':(60.3923,25.6651),'label':'Porvoo'}]
folium.Marker(location=(-23.3197,-51.1662),popup='Nascimento: Londrina',icon=folium.Icon(color='red',icon='star',icon_color='darkred')).add_to(city_map)
for city in green_cities:
    marker = folium.Marker(location=city['loc'],popup='Amigos: ' + city['label'],icon=folium.Icon(color='lightgreen',icon='users',prefix='fa',icon_color='darkgreen'))
    marker.add_to(city_map)
for city in white_cities:
    marker = folium.Marker(location=city['loc'],popup='Casa: ' + city['label'],icon=folium.Icon(color='white',icon="home",prefix='fa',icon_color='gray'))
    marker.add_to(city_map)
for city in cisv_cities:
    marker = folium.Marker(location=city['loc'],popup='CISV: ' + city['label'],icon=folium.Icon(color='orange',icon='globe',prefix='fa',icon_color='darkred'))
    marker.add_to(city_map)
#salvar o arquivo e abrir
city_map.save('map_file.html')
webbrowser.open('map_file.html')
