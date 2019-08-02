import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Network parameters
a = 0.5
b = -1
c = 1
d = -1
nodes = 1000
du = 1.0
dv = 0.1

G_Ring = nx.watts_strogatz_graph(nodes, 2, 0)
Lambda = nx.laplacian_matrix(G_Ring).toarray()

# Calculating eigenvalues

I = np.identity(nodes)
A = a * I - du * Lambda
B = b * I
C = c * I
D = d * I - dv * Lambda
    
Gamma = np.block([
        [A, B],
        [C, D]
        ])
Gamma_eig  = np.linalg.eigvals(Gamma)
Gamma_eig = np.real(Gamma_eig)

inv_gamma_eig = 1/abs(Gamma_eig)

print('done')

#Plotting
fig, axs = plt.subplots(2)
axs[0].hist(inv_gamma_eig, bins= 100,histtype='step')
axs[0].set_title('Inverse')
axs[1].hist(Gamma_eig, bins= 100,histtype='step')
axs[1].set_title('Normal')