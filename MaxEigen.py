"""
Created on Tue Jul 30 16:06:06 2019

@author: Shaheim Ogbomo-Harmitt
"""
import networkx as nx
import numpy as np

def FindMaxEigen(Lambda,nodes,a,b,c,d,du,dv):

    I = np.identity(nodes)
    A = a * I - du * Lambda
    B = b * I
    C = c * I
    D = d * I - dv * Lambda
    
    Gamma = np.block([
            [A, B],
            [C, D]
            ])
    
    ### EIGENVALUES OF REACTIVE LAPLACIAN ###
    Gamma_eig  = np.linalg.eigvals(Gamma)
    Gamma_eig = np.real(Gamma_eig)
    max_eig = np.amax(Gamma_eig)
    
    return max_eig

# OPTIONAL PARAMETERS
a = 0.5
b = -1
c = 1
d = -1
n = 100

G_Ring = nx.watts_strogatz_graph(n, 2, 0)
G_ER = nx.erdos_renyi_graph(n,0.5)
Lap_ER = nx.laplacian_matrix(G_ER).toarray()
Lap_Ring = nx.laplacian_matrix(G_Ring).toarray()

ER_mx_val = FindMaxEigen(Lap_ER,n,a,b,c,d,0.5,0.05)
Ring_mx_val = FindMaxEigen(Lap_Ring,n,a,b,c,d,0.5,0.05)

from RD_MODULE_VER_3 import *

dv = np.linspace(0,0.5,num = 100)
du = np.linspace(0,0.05,num = 100)

ER_obj = RD_Net(n,a,b,c,d,Lap_ER)

val = ER_obj.Bi_Curve(du,dv)

print('ER')

R_obj = RD_Net(n,a,b,c,d,Lap_Ring)

print('Ring')

val2 = R_obj.Bi_Curve(du,dv)