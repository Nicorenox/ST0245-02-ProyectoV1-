import webbrowser
import pandas as pd
import numpy as np  
import networkx as nx
import matplotlib.pyplot as plt

import folium as folium
import os

#Leer archivo
map_acoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';', encoding = 'latin1')

map_acoso['harassmentRisk'].fillna(map_acoso['harassmentRisk'].mean(), inplace = True)
map_acoso["harassmentRisk * length"] = map_acoso["harassmentRisk"] * map_acoso["length"]
map_acoso

#Menor acoso
graph_map_acoso = nx.from_pandas_edgelist(map_acoso, source='origin', target='destination', edge_attr='harassmentRisk')
dijkstra_caminomenosacoso = nx.dijkstra_path(graph_map_acoso , source='(-75.5705713, 6.2684867)', target= '(-75.5796409, 6.26', weight= 'harassmentRisk')
dijkstra_caminomenosacoso_weight = nx.dijkstra_path_length(graph_map_acoso , source='(-75.5705713, 6.2684867)', target= '(-75.5796409, 6.26059)', weight= 'harassmentRisk')

#Menor distancia
graph_map = nx.from_pandas_edgelist(map_acoso, source='origin', target='destination', edge_attr='length')
dijkstra_caminomenosdist = nx.dijkstra_path(graph_map , source='(-75.5705713, 6.2684867)', target= '(-75.5796409, 6.26059)', weight= 'length')
dijkstra_caminomenosdist_weight = nx.dijkstra_path_length(graph_map , source='(-75.5705713, 6.2684867)', target= '(-75.5796409, 6.26059)', weight= 'length')


prom_dist = 0
prom_acoso = 0
# Promedio distancia
for i in dijkstra_caminomenosdist:
    prom_dist += 1
    prom_dist = dijkstra_caminomenosdist_weight / prom_distancia
# Promedio acoso
for i in dijkstra_caminomenosacoso:
    prom_acoso += 1
    prom_acoso = dijkstra_caminomenosacoso_weight / prom_acoso

print ("\n Ruta con menos acoso:", dijkstra_caminomenosacoso)
print("Acoso de tu camino:",dijkstra_caminomenosacoso_weight)
print(prom_acoso)

print ("\n Ruta mas corta:", dijkstra_caminomenosdist)
print("Distancia de tu camino:",dijkstra_caminomenosdist_weight)
print(prom_distancia)


#Mapas
for i in range(len(dijkstra_caminomenosacoso)): dijkstra_caminomenosacoso[i] = eval(dijkstra_caminomenosacoso[i])[::-1]

Mapp = folium.Map (dijkstra_caminomenosacoso[0], zoom_start = 15) 
route = folium.PolyLine(dijkstra_caminomenosacoso,color = 'Green',weight = 5,opacity = 0.8).add_to (Mapp)
Mapp.save (os.path.join('CaminoEnMapa.html'))
webbrowser.open_new_tab('CaminoEnMapa.html')

for i in range(len(dijkstra_caminomenosdist)): dijkstra_caminomenosdist[i] = eval(dijkstra_caminomenosdist[i])[::-1]

Mapp2 = folium.Map (dijkstra_caminomenosdist[0], zoom_start = 15) 
route = folium.PolyLine(dijkstra_caminomenosdist,color = 'Blue',weight = 5,opacity = 0.8).add_to (Mapp2)
Mapp2.save (os.path.join('CaminoEnMapa2.html'))
webbrowser.open_new_tab('CaminoEnMapa2.html')
