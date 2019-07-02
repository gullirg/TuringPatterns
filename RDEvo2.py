#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:30:23 2019

@author: gulli
"""

#!/usr/bin/env ppthon3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:47:27 2019

@author: gulli
"""

import numpy as np
from matplotlib import pyplot as plt
import networkx as nx

### NETWORK VARIABLES ###
n=100 # 10 nodes
m=200 # 20 edges

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2
d_u = 1
d_v = 1

I = np.identity(n)

### GENERATE RANDOM GRAPH ###
G=nx.gnm_random_graph(n,m)

### Laplacian matrix ###
L = nx.laplacian_matrix(G)

### DEFINING BASIC DATA ###
t0 = 0
#no = 101
u0 = np.zeros([n])
v0 = np.zeros([n])
p0 = [u0, v0]
tf = 10
deltat = (tf - t0) / (n-1)

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros([n])
v = [0] * n
p = [u, v]

### DEFINING M ### 
### REACTIVE LAPLACIAN ###
A = a * I - d_u * L
B = b * I
C = c * I
D = d * I - d_v * L

M_a = np.block([
            [A], 
            [C]
            ])

### FOR LOOP FOR EULER'S METHOD ###
u[0] = u0
for i in range(1,n):
    u[i] = deltat * (A * u[i-1] + C * u[i-1]) + u[i-1]

#for i in range(n): print(t[ i ] ,u[ i ])
