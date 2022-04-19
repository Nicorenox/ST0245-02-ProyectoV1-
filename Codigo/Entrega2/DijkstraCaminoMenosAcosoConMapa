import webbrowser
import pandas as pd
import numpy as np  
import networkx as nx

import folium as folium
import os

map_acoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';', encoding = 'latin1')

grafica = nx.from_pandas_edgelist(map_acoso, source='origin', target='destination', edge_attr='harassmentRisk')

## De momento el camino es puesto manualmente por coordenada, mas adelante como objetivo de que el usuario seleccione un camino facilmete

dijkstra_caminomenosacoso = nx.dijkstra_path(grafica , source='(-75.6118262, 6.227342)', target= '(-75.6909483, 6.338773)', weight= 'harassmentRisk')
print (dijkstra_caminomenosacoso)

for i in range(len(dijkstra_caminomenosacoso)):  dijkstra_caminomenosacoso[i] = eval(dijkstra_caminomenosacoso[i])[::-1]

Mapp = folium.Map (dijkstra_caminomenosacoso[0], zoom_start = 15) 
route = folium.PolyLine(dijkstra_caminomenosacoso,color = 'Green',weight = 8,opacity = 0.8).add_to (Mapp)
Mapp.save (os.path.join('CaminoEnMapa.html'))
webbrowser.open_new_tab('CaminoEnMapa.html')
