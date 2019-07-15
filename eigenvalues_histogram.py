import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from argparse import ArgumentParser

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
t = 0
for d_u in np.linspace(0,0.05,10):

    for d_v in np.linspace(0,0.5,10):
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
        plt.hist(Gamma_eig, bins=np.linspace(Gamma_eig.min(), Gamma_eig.max()+1, len(Gamma_eig)*10),histtype='step')
        #plt.ylim(0, 200)
        plt.xlim(-3.5, 1)
        plt.yscale('log', nonposy='clip')
        plt.title(r'Eigenvalue distribution of reactive Laplacian $\Gamma$ - $d_u =$' + str(round(d_u,3)) + ' & $d_v =$' + str(round(d_v,3)))
        plt.ylabel('Number of Eigenvalues')
        plt.xlabel('Eigenvalue')
        plt.savefig('./Gamma_eig_'+str(t)+'.png')
        t += 1
        plt.clf()


from os import system
system('convert -delay 10 -loop 0 *.png eigenvalues_histogram.gif')
system('rm *.png')

### ARGUMENT PARSER ###
def get_args() :
    '''parse arguments from command line'''
    parser = ArgumentParser()

    parser.add_argument('--n', help = 'number of nodes', type = int, default = 200)

    return vars(parser.parse_args())

# execute main program
if __name__ == '__main__' :
    args = get_args()
    main(**args)