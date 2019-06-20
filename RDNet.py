# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Create an G{n,m} random graph with n nodes and m edges
and report some properties.

This graph is sometimes called the Erdős-Rényi graph
but is different from G{n,p} or binomial_graph which is also
sometimes called the Erdős-Rényi graph.
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
__credits__ = """"""
#    Copyright (C) 2004-2015 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

import networkx as nx
import sys
import numpy as np
import matplotlib.pyplot as plt

### NETWORK VARIABLES ###
n=10 # 10 nodes
m=20 # 20 edges

### RD SYSTEM VARIABLES ###
d_u = 1
d_v = 1
a = 1
b = -2
c = 2
d = -2
I = np.identity(n)

### GENERATE RANDOM GRAPH ###
G=nx.gnm_random_graph(n,m)

### SHOW PROPERTIES ###
print("node degree clustering")
for v in nx.nodes(G):
    print('%s %d %f' % (v,nx.degree(G,v),nx.clustering(G,v)))

k_sum = 0
for i in nx.nodes(G):
    k_sum += nx.degree(G,i)
print("k_sum = ", k_sum)

L_sum = 0
for j in range(len(nx.laplacian_matrix(G).toarray()[:,0])):
    L_sum += nx.laplacian_matrix(G).toarray()[j][j]
print("L_sum = ", L_sum)
    
### PRINT ADJACENCY LIST ###
try:
    nx.write_adjlist(G,sys.stdout)
except TypeError: # Python 3.x
    nx.write_adjlist(G,sys.stdout.buffer)

### PLOT NETWORK ###    
nx.draw_networkx(G)
plt.show()
plt.close()
### PRINT ADJACENCY AND LAPLACIAN MATRICES ###
print("ADJACENCY MATRIX OF G:")
print(nx.adjacency_matrix(G).toarray())

print("LAPLACIAN MATRIX OF G:")
print(nx.laplacian_matrix(G).toarray())

### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
w,v = np.linalg.eig(nx.laplacian_matrix(G).toarray())
#print("w: ", w)
#print("v: ", v)

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

Phase_Plane = []
if (Gamma_eig>0).all() == False:
    Phase_Plane.append(0)
else:
    Phase_Plane.append(1)

print("Stability: ", Phase_Plane)

plt.imshow(Gamma);
plt.colorbar()
plt.show()
