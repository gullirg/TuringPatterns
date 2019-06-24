#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:46:25 2019

@author: gulli
"""

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
__credits__ = """Aric Hagberg""" # FOR ERDOS-RENYI NETWORK GENERATION WITH NETWORKX

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

### NETWORK VARIABLES ###
n=100 # 10 nodes
m=200 # 20 edges

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2

I = np.identity(n)

### GENERATE RANDOM GRAPH ###
G=nx.gnm_random_graph(n,m)

### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
w,v = np.linalg.eig(nx.laplacian_matrix(G).toarray())

### GENERATE DIAGONALIZED LAPLACIAN ###
Lambda = np.diag(w)

### CALCULATE STABILITY FOR DIFFERENT DIFFUSIVITIES ###
x_u= []
y_v = []
Phase_Plane = []
for d_u in np.arange(0, 0.05, 0.001):
    x_u.append(d_u)
    temp = []
    for d_v in np.arange(0, 0.5, 0.01):
        y_v.append(d_v)


        
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
        
# ================================================BOOLEAN MATRIX GENERATOR=====
#         if not check:
#             temp.append(0)
#             
#         else:
#             temp.append(1)
# =============================================================================
            
    Phase_Plane.append(temp)
    
### GENERATE TRANSPOSE MATRIX ###
matrix = np.transpose(np.matrix(Phase_Plane))

### CONTOUR PLOT ###
x = np.arange(0, 50, 1)
y = np.arange(0, 50, 1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = matrix
h = plt.contourf(x,y,z, cmap = plt.cm.bone)
plt.colorbar()
plt.show()
