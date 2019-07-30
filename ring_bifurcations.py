import networkx as nx
import numpy as np
from numpy.lib import scimath

import matplotlib.pyplot as plt
from time import time


def generate_reactive_laplacian(a,b,c,d,d_u,d_v,Lambda) :
    ### REACTIVE LAPLACIAN ###
    A = a * I - d_u * Lambda
    B = b * I
    C = c * I
    D = d * I - d_v * Lambda
    
    Gamma = np.block([
            [A, B], 
            [C, D]
            ])

    return Gamma


def get_eigenvalues(Gamma) :
    '''returns eigenvalues of reactive laplacian'''

    ### EIGENVALUES OF REACTIVE LAPLACIAN ###
    eigenvalues = np.linalg.eigvals(Gamma)
    return eigenvalues


### NETWORK VARIABLES ###
n_nodes=70 # nodes

# ### REACTIVE FUNCTION VARIABLES ### ###
a = 0.5
b = -1
c = 1
d = -1


I = np.identity(n_nodes)

### GENERATE RING GRAPH ###
graph = nx.watts_strogatz_graph(n_nodes,2,0)
#graph = nx.grid_graph(dim=[int(np.sqrt(n)) ,int(np.sqrt(n))], periodic=False)

### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
w,v = np.linalg.eig(nx.laplacian_matrix(graph).toarray())

### GENERATE DIAGONALIZED LAPLACIAN ###
Lambda = np.diag(w)

N = 50
d_us,d_vs = np.linspace(0,0.1,N),np.linspace(0,1,N)
d_ugrid,d_vgrid = np.meshgrid(d_us,d_vs)

Gammas = [ generate_reactive_laplacian(a,b,c,d,d_u,d_v,Lambda)
        for d_v in d_vs for d_u in d_us
]


### CALCULATE STABILITY FOR DIFFERENT DIFFUSIVITIES ###
t = time()
eigenvalues = np.array([ get_eigenvalues(Gamma) for Gamma in Gammas ]).reshape(N,N,2*n_nodes)
print(time()-t)

plt.figure(figsize=(7,7))
plt.title(r'Stable-unstable regions of the homogenous steady state', size = 16, y=1.04)
plt.contourf(d_ugrid,d_vgrid,np.amax(eigenvalues,axis=-1)>0,cmap='bone_r',vmin=0,vmax=1)

plt.xlabel(r'$d_u$', size = 16)
plt.ylabel(r'$d_v$', size = 16)
plt.show()

# ### GENERATE TRANSPOSE MATRIX ###
# matrix = np.transpose(np.matrix(Phase_Plane))

# ### CONTOUR PLOT ###
# x = np.linspace(0,0.05,50)
# y = np.linspace(0,0.5,50)
# xx, yy = np.meshgrid(x, y, sparse=True)
# z = matrix

# h = plt.contourf(x,y,np.log(z), cmap = 'bone_r')
# plt.colorbar()
# plt.title(r'Stable-unstable regions of the homogenous steady state', size = 16)
# plt.gca().title.set_position([.5, 1.05])
# plt.xlabel(r'$d_u$', size = 16)
# plt.ylabel(r'$d_v$', size = 16)
# plt.tight_layout()
# #plt.savefig('./PhasePlane_TP.png')
# plt.show()