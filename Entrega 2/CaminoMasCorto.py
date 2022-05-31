import pandas as pd
import numpy as np  
import networkx as nx

map_acoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';', encoding = 'latin1')

grafica = nx.from_pandas_edgelist(map_acoso, source='origin', target='destination', edge_attr='length')

dijkstra_caminocorto = nx.dijkstra_path(grafica, source='(-75.6118262, 6.227342)', target= '(-75.6909483, 6.338773)', weight='length')
print (dijkstra_caminocorto)
