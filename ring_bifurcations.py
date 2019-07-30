import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### NETWORK VARIABLES ###
n=200 # nodes

### REACTIVE FUNCTION VARIABLES ### ###
a = 0.5
b = 1
c = -1
d = 1

I = np.identity(n)

### GENERATE RING GRAPH ###
graph = nx.watts_strogatz_graph(n, 2, 0)
#graph = nx.grid_graph(dim=[int(np.sqrt(n)) ,int(np.sqrt(n))], periodic=False)

### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
w,v = np.linalg.eig(nx.laplacian_matrix(graph).toarray())

### GENERATE DIAGONALIZED LAPLACIAN ###
Lambda = np.diag(w)

### CALCULATE STABILITY FOR DIFFERENT DIFFUSIVITIES ###
Phase_Plane = []
for d_u in np.linspace(0,0.05,50):
    temp = []

    for d_v in np.linspace(0,0.5,50):
        ### REACTIVE LAPLACIAN ###
        A = a * I - d_u * Lambda
        B = b * I
        C = c * I
        D = d * I - d_v * Lambda
        
        Gamma = np.block([
                [A, B], 
                [C, D]
                ])
    
        ### EIGENVALUES OF REACTIVE LAPLACIAN ###
        y,z = np.linalg.eig(Gamma)
        Gamma_eig = np.real(y)

        ### FIND PERCENTAGE OF POSITIVE EIGENVALUES ###
        check = []
        for g in Gamma_eig:
            if g > 0. :
                check.append(1)
            else:
                check.append(0)
        
        value_norm = sum(check)/len(check) 
        temp.append(value_norm)
            
    Phase_Plane.append(temp)
    
### GENERATE TRANSPOSE MATRIX ###
matrix = np.transpose(np.matrix(Phase_Plane))

### CONTOUR PLOT ###
x = np.linspace(0,0.05,50)
y = np.linspace(0,0.5,50)
xx, yy = np.meshgrid(x, y, sparse=True)
z = matrix

h = plt.contourf(x,y,np.log(z), cmap = 'bone_r')
plt.colorbar()
plt.title(r'Stable-unstable regions of the homogenous steady state', size = 16)
plt.gca().title.set_position([.5, 1.05])
plt.xlabel(r'$d_u$', size = 16)
plt.ylabel(r'$d_v$', size = 16)
plt.tight_layout()
#plt.savefig('./PhasePlane_TP.png')
plt.show()

