import pandas as pd
import numpy as np  
import networkx as nx

map_acoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';', encoding = 'latin1')

grafica = nx.from_pandas_edgelist(map_acoso, source='origin', target='destination', edge_attr='harassmentRisk')

dijkstra_caminomenosacoso = nx.dijkstra_path(grafica, source='(-75.6019061, 6.2843217)', target='(-75.5929496, 6.2813088)', weight='harassmentRisk')
print (dijkstra_caminomenosacoso)
