"""
Shows the live evolution of the RD system on the network.
 
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

### NETWORK VARIABLES ###
n=200 # nodes

### REACTIVE FUNCTION VARIABLES ###
a = 0.5
b = 1
c = -1
d = -1
d_u = 0.01
d_v = 0.3

### DEFINING BASIC DATA ###
t0 = 0
tf = 40000
deltat = 0.005

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### GENERATE RING GRAPH ###
G=nx.watts_strogatz_graph(n, 2, 0)

### Laplacian matrix ###
L = nx.laplacian_matrix(G)


I = np.identity(n)

### REACTIVE LAPLACIAN ###
A = a * I - d_u * L
B = b * I
C = c * I
D = d * I - d_v * L

Gamma = np.block([[A, B], [C, D] ])
y,z = np.linalg.eig(Gamma)
Gamma_eig = np.real(y)

plt.hist(Gamma_eig,bins=np.linspace(Gamma_eig.min(), Gamma_eig.max()+1, len(Gamma_eig)),histtype='step')
plt.yscale('log')
plt.xlim(-3.5, 1)
plt.title(r'Eigenvalue distribution of reactive Laplacian $\Gamma$ - $d_u =$' + str(round(d_u,3)) + ' & $d_v =$' + str(round(d_v,3)))
plt.ylabel('Number of Eigenvalues')
plt.xlabel('Eigenvalue')
plt.savefig('./Gamma_eig.png')
plt.close()

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n,tf))
v = np.zeros((n,tf))

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.uniform(0,0.1,size = n)
v[:, 0] = np.random.uniform(0,0.1,size = n)

for i in range(1, tf):
    u[:, i] = deltat * (-d_u * L.dot(u[:, i-1]) + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * L.dot(v[:, i-1]) + c * u[:, i-1] +d * v[:, i-1]) + v[:, i-1]

### GRAPH DRAWING ###
pos = nx.circular_layout(G)

j = 0
for k in range(tf):
    if k % 250 == 0:

        plt.title('t = {}'.format(deltat*k))
        nx.draw_networkx(G,node_color = v[:, k],
                pos = pos, alpha=0.5, cmap='coolwarm',
                with_labels = False)
        sm = plt.cm.ScalarMappable(cmap='coolwarm',
                norm=plt.Normalize(vmin=np.amin(u[:, k]-v[:, k]),
                vmax=np.amax(u[:, k]-v[:, k]))
                )
        sm.set_array([])
        cbar = plt.colorbar(sm)
        plt.savefig(str(j).zfill(3)+'.png')
        j += 1
        plt.close()

from os import system
system('convert -delay 10 -loop 0 *.png network_trajectory.gif')
system('rm *.png')