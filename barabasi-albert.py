import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

'''# create graph with seed graph
k_incr = []
old_G = nx.barabasi_albert_graph(2, 1, seed=707)
for i in range(3,100):
  G = nx.barabasi_albert_graph(i, 1, seed=707)
  for j in old_G:
    if G.degree(j) > old_G.degree(j) and i>50:
      k_incr.append(old_G.degree(j))
  old_G = G
  #nx.draw_networkx(G)
  #plt.show()
print(k_incr)
plt.hist(k_incr)
plt.show()
exit()'''

G = nx.Graph()
G.add_edge(0,1)

# graph gen properties
size = 100 + len(G)
sample_range = range(75,100)

k_incr = []

for i in range(len(G),size):
  k_sum = 2*G.number_of_edges()
  prob = [ k/k_sum for n,k in G.degree() ]  
  print(prob)

  node_sel = np.random.choice(G.nodes(), p=prob)
  if i in sample_range:
    k_incr.append(G.degree(node_sel))
  G.add_edge(i, node_sel)

print(k_incr)
nx.draw_networkx(G)
plt.show()


plt.hist(k_incr)
plt.show()
