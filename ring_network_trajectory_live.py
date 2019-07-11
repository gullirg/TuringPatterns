#%%

"""
Shows the live evolution of the RD system on the network.

To display on the Python Interactive cell click 'Run Cell' at the top or bottom of the code. 
"""

# %matplotlib qt
# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib as mpl

### NETWORK VARIABLES ###
n=200 # nodes

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -1.7
c = 1.9
d = -2
d_u = 0.006
d_v = 0.125

### DEFINING BASIC DATA ###
t0 = 0
tf = 4000
deltat = 0.01

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### GENERATE RING GRAPH ###
G=nx.watts_strogatz_graph(n, 2, 0)

### Laplacian matrix ###
L = nx.laplacian_matrix(G)

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n,tf))
v = np.zeros((n,tf))

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.uniform(0,0.01,size = n)
v[:, 0] = np.random.uniform(0,0.01,size = n)

for i in range(1, tf):
    u[:, i] = deltat * (-d_u * L * u[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * L * v[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + v[:, i-1]


### CONCENTRATIONS DIFFERENCE ###
z = np.zeros((n,tf))

for m in range(tf):
    z[:, m] = u[:, m] - v[:, m]

### GRAPH DRAWING ###
pos = nx.circular_layout(G)

for k in range(tf):
    if k % 100 == 0:
        cmap = plt.cm.coolwarm
        fig = nx.draw_networkx(G, node_color = z[:, k], pos = pos, cmap= cmap, with_labels = False, vmin=0, vmax=1)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=1))
        sm.set_array([])
        cbar = plt.colorbar(sm)
        #plt.savefig('./Ring_'+str(k) +'.png')
        plt.show(fig)
        plt.pause(0.5)
        plt.close()
        print(k)


#%%
