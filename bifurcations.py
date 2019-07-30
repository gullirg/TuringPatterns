import networkx as nx
import numpy as np
import matplotlib.pyplot as plt




### NETWORK VARIABLES ###
n=500 # nodes

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2

I = np.identity(n)

### GENERATE RANDOM GRAPH ###
G=nx.nx.erdos_renyi_graph(n, 0.1)

### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
w,v = np.linalg.eig(nx.laplacian_matrix(G).toarray())

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
plt.title(r'\textit{Stable-unstable regions of the homogenous steady state}', size = 'xx-large')
plt.gca().title.set_position([.5, 1.05])
plt.xlabel(r'\textit{d\textsubscript{u}', size = 'xx-large')
plt.ylabel(r'\textit{d\textsubscript{v}', size = 'xx-large')
plt.tight_layout()
plt.savefig('./PhasePlane_ER.png')
plt.show()












