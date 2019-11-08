import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_edge(0,1)

# graph gen properties
size = 1000 + len(G)
sample_range = range(750,900)
C = 5
alpha = 1
weight = C/(C + alpha)

k_incr = []

for i in range(len(G),size):
  r = np.random.random() 

  if r < weight:
    sel_edge_index = np.random.choice(len(G.edges)) 
    sel_edge = list(G.edges())[sel_edge_index]
    node_sel = sel_edge[1]
    if i in sample_range:
      in_deg = G.in_degree(node_sel)
      print(node_sel, in_deg)
      k_incr.append(in_deg)
  else:
    node_sel = np.random.choice(G.nodes)

  G.add_edge(i, node_sel)
  #nx.draw_networkx(G)
  #plt.show()

print(k_incr)
#nx.draw_networkx(G)
#plt.show()


plt.hist(k_incr, bins=range(0,max(k_incr)), density=False)
plt.show()
