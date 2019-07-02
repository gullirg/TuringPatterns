# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Create an G{n,m} random graph with n nodes and m edges.

This graph is sometimes called the Erdős-Rényi graph
but is different from G{n,p} or binomial_graph which is also
sometimes called the Erdős-Rényi graph.

Then check stability using reactive Laplacian eigenvalues.
"""
__author__ = """Guglielmo Reggio & Shaheim Ogbono-Harmitt"""
__credits__ = """Aric Hagberg"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

### NETWORK VARIABLES ###
n=10 # 10 nodes
m=200 # 20 edges

### RD SYSTEM VARIABLES ###
#d_u = 0.01
#d_v = 0.5
a = 1
b = -2
c = 2
d = -2
I = np.identity(n)
###
x_u= []
y_v = []
Phase_Plane = []
for d_u in np.arange(0, 0.05, 0.001):
    x_u.append(d_u)
    temp = []
    for d_v in np.arange(0, 0.5, 0.01):
        y_v.append(d_v)

        ### GENERATE RANDOM GRAPH ###
        G=nx.gnm_random_graph(n,m)
        
        ### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
        w,v = np.linalg.eig(nx.laplacian_matrix(G).toarray())
        
        ### DIAGONALIZED LAPLACIAN ###
        Lambda = np.diag(w)
        
        ### REACTIVE LAPLACIAN ###
        A = a * I - d_u * Lambda
        B = b * I
        C = c * I
        D = d * I - d_v * Lambda
        
        Gamma = np.block([
                [A, B], 
                [C, D]
                ])
        
        y,z = np.linalg.eig(Gamma)
        Gamma_eig = np.real(y)

        check = []
        for g in Gamma_eig:
            if g > 0. :
                check.append(1)
        
        if not check:
            temp.append(0)
            
        else:
            temp.append(1)
            
            
    Phase_Plane.append(temp)
    

matrix = np.transpose(np.matrix(Phase_Plane))


# =============================================================================
# print(matrix)
# print(len(x_u))
# print(len(y_v))
# print(matrix.shape)
# =============================================================================

# =============================================================================
# fig, ax = plt.subplots()
# 
# min_val, max_val = 0, len(temp)
# 
# 
# cax = ax.matshow(matrix, cmap=plt.cm.Blues, origin = 'lower')
# 
# plt.title('The stable-unstable regions of the homogeneous steady state')
# plt.xlabel('d_u')
# plt.ylabel('d_v')
# 
# fig.colorbar(cax)
# 
# plt.show()
# =============================================================================


x = np.arange(0, 50, 1)
y = np.arange(0, 50, 1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = matrix
h = plt.contourf(x,y,z)
plt.show()















