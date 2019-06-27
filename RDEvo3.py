#!/usr/bin/env ppthon3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:40:19 2019

@author: gulli
"""

import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command

### NETWORK VARIABLES ###
n=100 # 10 nodes
m=200 # 20 edges

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2
d_u = 0.1
d_v = 0.9

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
tf = 10
deltat = (tf - t0) / (n-1)

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n,tf))
v = np.zeros((n,tf))

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.rand(n)
v[:, 0] = np.random.rand(n)

for i in range(1, tf):
    u[:, i] = deltat * (-d_u * L * u[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * L * v[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + v[:, i-1]

#for i in range(n): print(t[ i ] ,u[ i ])

#plt.figure(figsize=(16.0, 14.0))
plt.plot(u, v, linestyle='--', marker='o', markersize=0.7, linewidth=0.2)
plt.title(r'\textit{Variance of concetrations per single node}', size = 'xx-large')
plt.gca().title.set_position([.5, 1.05])
plt.xlabel(r'\textit{u}', size = 'xx-large')
plt.ylabel(r'\textit{v}', size = 'xx-large')

#plt.savefig('/Users/gulli/Google Drive/KURF/NodeEvo.png')

plt.tight_layout()
plt.show()
