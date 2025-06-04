import numpy as np
import networkx as nx 
import matplotlib.pyplot as mpli

# Matriz de adjacência modificada manualmente
adj_matrix = np.array([
   # 0  1  2  3  4  5  6  7  8  9
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],  # 0
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 1
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # 2
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # 3
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],  # 4
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],  # 5
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # 6
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],  # 7
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # 8
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]   # 9
])

# Criando o objeto Grafo a partir da matriz de adjacência
G = nx.from_numpy_array(adj_matrix)

# Desenhando o Grafo
mpli.figure(figsize=(8, 8))
pos = nx.spring_layout(G)  # Layout para o posicionamento dos nós
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight="bold", node_size=700)

# Exibir o grafo
mpli.show()