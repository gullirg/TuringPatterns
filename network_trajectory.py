

###
# %matplotlib qt
# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib as mpl


### NETWORK VARIABLES ###
n=100 # nodes
m=200 # edges

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2
d_u = 0.1
d_v = 0.05

I = np.identity(n)

### DEFINING BASIC DATA ###
t0 = 0
u0 = np.zeros([n])
v0 = np.zeros([n])
tf = 500
#deltat = (tf - t0) / (n-1)
deltat = 0.1

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### GENERATE RANDOM GRAPH ###
# =============================================================================
# G=nx.gnm_random_graph(n,m)
# =============================================================================
G=nx.grid_graph(dim=[int(np.sqrt(n)) ,int(np.sqrt(n))], periodic=False) 

### Laplacian matrix ###
L = nx.laplacian_matrix(G)

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n,tf))
v = np.zeros((n,tf))

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.rand(n)
v[:, 0] = np.random.rand(n)

for i in range(1, tf):
    u[:, i] = deltat * (-d_u * L * u[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * L * v[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + v[:, i-1]

### CONCENTRATIONS DIFFERENCE ###
z = np.zeros((n,tf))

for m in range(tf):
    z[:, m] = u[:, m] - v[:, m]

### ASSIGN CONCENTRATIONS AS NODE ATTRIBUTES ###
# =============================================================================
# values = {}
# 
# for j in range(len(u[:, tf - 1])):
#     #values[j] = u[:, 9][j] - v[:, 9][j]
#     values[j] = z[:, 9][j]
#    
# nx.set_node_attributes(G, 'values', values)
# =============================================================================

pos = dict( (n, n) for n in G.nodes() )


for k in range(tf):
    nx.draw(G, node_color = z[:, k], pos = pos, cmap= 'Blues', with_labels = False)
    print(k)
    plt.savefig('./Net_'+str(k) +'.png')
    #plt.show()


# =============================================================================
# nx.draw(G, pos)
# node_labels = nx.get_node_attributes(G,'values')
# nx.draw_networkx_labels(G, pos, labels = node_labels)
# plt.show()
# =============================================================================
