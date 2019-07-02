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
d_u = 0.3
d_v = 0.5

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
p0 = [np.zeros(2*n)]
tf = 10
deltat = (tf - t0) / (n-1)

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### INITIALIZING ARRAY FOR p-VALUES ###
u = [None] * n
v = [None] * n
p = [None] * 2 * n

### DEFINING M ### 
### REACTIVE LAPLACIAN ###
A = a * I - d_u * L
B = b * I
C = c * I
D = d * I - d_v * L

M_a = np.block([
            [A, B], 
            [C, D]
            ])

### FOR LOOP FOR EULER'S METHOD ###
p[0] = np.random.rand(n*2, 1)
for i in range(1,2 * n):
    p[i] = deltat * (M_a * p[i-1]) + p[i-1]

for i in range(n): print(t[ i ] ,p[ i ])

# =============================================================================
# for k in range(len(p)):
#     u.append(p[k][0:1])
#     v.append(p[k][0:2])
# print(u,v)
# =============================================================================

# =============================================================================
# u = []
# v = []
# for j in p[-1]:
#     u.append(p[0+2*j])
#     v.append(p[1+2*j])
# =============================================================================

# =============================================================================
# plt.plot(t,p[-1], 'o')
# plt.xlabel('Value of x')
# plt.ylabel('Value of y')
# plt.title('Approximate Solution with Forward Euler’s Method') 
# plt.show()
# =============================================================================

### GENERATE TRANSPOSE MATRIX ###
matrix = np.transpose(np.matrix(p[-1]))

