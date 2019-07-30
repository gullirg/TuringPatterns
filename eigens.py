import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from os import system

from argparse import ArgumentParser

def get_args() :
    '''parse arguments from command line'''
    parser = ArgumentParser(description = "Generates reactive Laplacian's eigenvalues histogram")
    parser.add_argument('--graph_type', nargs = '?', type = str, default = 'ring',
                        help = "graph type ['ring' or 'random'] - default = 'ring'")
    parser.add_argument('--nodes', nargs = '?', type = int, default = 1000,
                        help = 'number of nodes - default = 1000')
    parser.add_argument('--a', nargs = '?', type = float, default = 1,
                        help = "entry 'a' of jacobian matrix - default = 1")
    parser.add_argument('--b', nargs = '?', type = float, default = -1.7,
                        help = "entry 'b' of jacobian matrix - default = -1.7")
    parser.add_argument('--c', nargs = '?', type = float, default = 1.9,
                        help = "entry 'c' of jacobian matrix - default = 1.9")
    parser.add_argument('--d', nargs = '?', type = float, default = -2,
                        help = "entry 'd' of jacobian matrix - default = -2")
    parser.add_argument('--du', nargs = '?', type = float, default = 0.05,
                        help = "du value - default = 0.05")
    parser.add_argument('--dv', nargs = '?', type = float, default = 0.5,
                        help = "dv value - default = 0.5")
    return vars(parser.parse_args())

def generate_gif(graph_type = 'ring', nodes = 1000, a = 1, b = -1.7, c = 1.9, d = 2, du = 0.05, dv = 0.5):
        '''generates a gif with the different eiganvalues histograms.

        --parameters--
        graph_type : <str>
            graph type ['ring' or 'random'] - default = 'ring'
        nodes : <int>
            number of nodes in the graph
        a,b,c,d : <int>
            entries of the Jacobian matrix
        '''

        ### GENERATE RING GRAPH ###
        if graph_type == 'ring':
                graph = nx.watts_strogatz_graph(nodes, 2, 0)

        elif graph_type == 'random':
                graph = nx.erdos_renyi_graph(nodes, 0.01)

        ### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
        Lambda = nx.laplacian_matrix(graph).toarray()

        I = np.identity(nodes)

        ### REACTIVE LAPLACIAN ###
        A = a * I - du * Lambda
        B = b * I
        C = c * I
        D = d * I - dv * Lambda

        Gamma = np.block([
                [A, B],
                [C, D]
                ])

        ### EIGENVALUES OF REACTIVE LAPLACIAN ###
        y,z = np.linalg.eig(Gamma)
        Gamma_eig = np.real(y)

        generate_figure(Gamma_eig, du, dv, a, b, c, d, graph_type)


def generate_figure(Gamma_eig, du, dv, a, b, c, d, graph_type):
        '''main program figure display'''

        if a+d<0 :
                if a*d-b*c>0 :
                        message = 'JACOBIAN OBEYS CONDITIONS'
                elif a*d-b*c<0:
                        message = 'JACOBIAN DOES NOT OBEY CONDITIONS'
        else:
                message = 'JACOBIAN DOES NOT OBEY CONDITIONS'
        
        ### HISTOGRAM OF EIGENVALUES ###
        plt.hist(Gamma_eig, bins= 100,histtype='step')
        #plt.ylim(0, 200)
        plt.xlim(-8, 1)
        plt.yscale('log', nonposy='clip')
        plt.title(r'Eigenvalue distribution of reactive Laplacian $\Gamma$ - $d_u =$' + str(round(du,3)) + ' & $d_v =$' + str(round(dv,3))
                        + '\n a=' + str(round(a,3)) + ' & b=' +str(round(b,3)) + ' & c=' + str(round(c,3)) + ' & d=' +str(round(d,3)) 
                        + '\n ' + message + '\n Graph type: ' + graph_type)
        plt.ylabel('Number of Eigenvalues')
        plt.xlabel('Eigenvalue')
        plt.savefig("./image.png")
        plt.clf()

# execute main program
if __name__ == '__main__' :
    args = get_args()
    generate_gif(**args)
