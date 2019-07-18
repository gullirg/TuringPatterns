import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from os import system

from argparse import ArgumentParser

def get_args() :
    '''parse arguments from command line'''
    parser = ArgumentParser(description = "Generates reactive Laplacian's eigenvalues histogram")
    parser.add_argument('nodes', nargs = '?', type = int, default = 200, 
                        help = 'number of nodes')
    parser.add_argument('a', nargs = '?', type = int, default = 1, 
                        help = "entry 'a' of jacobian matrix - default = 1")
    parser.add_argument('b', nargs = '?', type = int, default = -1.7, 
                        help = "entry 'b' of jacobian matrix - default = -1.7")
    parser.add_argument('c', nargs = '?', type = int, default = 1.9, 
                        help = "entry 'c' of jacobian matrix - default = 1.9")
    parser.add_argument('d', nargs = '?', type = int, default = -2, 
                        help = "entry 'd' of jacobian matrix - default = -2")
    parser.add_argument('num', nargs = '?', type = int, default = 10, 
                        help = "number of evenly spaced samples for du & dv - default = 10")
    parser.add_argument('du_max', nargs = '?', type = int, default = 0.05, 
                        help = "maximum du value - default = 0.05")
    parser.add_argument('dv_max', nargs = '?', type = int, default = 0.5, 
                        help = "maximum dv value - default = 0.5")
    return vars(parser.parse_args())

def generate_gif(nodes = 200, a = 1, b = -1.7, c = 1.9, d = 2, num = 10):
        '''generates a gif with the different eiganvalues histograms'''
        ### GENERATE RING GRAPH ###
        graph = nx.watts_strogatz_graph(nodes, 2, 0)
        #graph = nx.grid_graph(dim=[int(np.sqrt(nodes)) ,int(np.sqrt(nodes))], periodic=False)

        ### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
        w,v = np.linalg.eig(nx.laplacian_matrix(graph).toarray())

        ### GENERATE DIAGONALIZED LAPLACIAN ###
        Lambda = np.diag(w)

        I = np.identity(nodes)

        t = 0
        for d_u in np.linspace(0,0.05,num = 10):

                for d_v in np.linspace(0,0.5,num = 10):
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
                        plt.hist(Gamma_eig, bins=np.linspace(Gamma_eig.min(), Gamma_eig.max()+1, 
                                                                len(Gamma_eig)*10),histtype='step')
                        #plt.ylim(0, 200)
                        plt.xlim(-3.5, 1)
                        plt.yscale('log', nonposy='clip')
                        plt.title(r'Eigenvalue distribution of reactive Laplacian $\Gamma$ - $d_u =$' + str(round(d_u,3)) + ' & $d_v =$' + str(round(d_v,3)))
                        plt.ylabel('Number of Eigenvalues')
                        plt.xlabel('Eigenvalue')
                        plt.savefig("Gamma_eig_du=" + du +"_dv=" + dv + "_a=" + a + "_b=" + b + "_c=" + c + "_d=" + d + ".png")
                        t += 1
                        plt.clf()

        system('convert -delay 10 -loop 0 *.png eigenvalues_histogram.gif')
        system('rm *.png')

# execute main program
if __name__ == '__main__' :
    args = get_args()
    generate_gif(**args)