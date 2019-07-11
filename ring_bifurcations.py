import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### NETWORK VARIABLES ###
n=200 # nodes

### REACTIVE FUNCTION VARIABLES ### ###
a = 1
b = -1.7
c = 1.9
d = -2

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
#t = 0
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
        
        ### HISTOGRAM OF EIGENVALUES ###
        # plt.hist(Gamma_eig,bins=np.linspace(Gamma_eig.min(), Gamma_eig.max()+1, len(Gamma_eig)),histtype='step')
        # plt.ylim(0, 200)
        # plt.xlim(-3.5, 1)
        # plt.title('Eigenvalue distribution of reactive Laplacian $\Gamma$ - $d_u =$' + str(round(d_u,3)) + ' & $d_v =$' + str(round(d_v,3)))
        # plt.ylabel('Number of Eigenvalues')
        # plt.xlabel('Eigenvalue')
        # plt.savefig('./Gamma_eig_'+str(t)+'.png')
        # t += 1
        # plt.clf()

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
#plt.savefig('./PhasePlane.png')
plt.show()

