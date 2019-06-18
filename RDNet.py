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

from networkx import *
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix


n=10 # 10 nodes
m=20 # 20 edges

G=gnm_random_graph(n,m)

# some properties
print("node degree clustering")
for v in nodes(G):
    print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

k_sum = 0
for i in nodes(G):
    k_sum += degree(G,i)
print("k_sum = ", k_sum)

L_sum = 0
for j in range(len(laplacian_matrix(G).toarray()[:,0])):
    L_sum += laplacian_matrix(G).toarray()[j][j]
print("L_sum = ", L_sum)
    
    

# print the adjacency list to terminal
try:
    write_adjlist(G,sys.stdout)
except TypeError: # Python 3.x
    write_adjlist(G,sys.stdout.buffer)
    
nx.draw_networkx(G)

print("ADJACENCY MATRIX OF G:")
print(adjacency_matrix(G).toarray())

print("LAPLACIAN MATRIX OF G:")
print(laplacian_matrix(G).toarray())

#plt.imshow(laplacian_matrix(G).toarray())
#plt.show()