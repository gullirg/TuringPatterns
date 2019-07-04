#!/usr/bin/env ppthon3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:40:19 2019

@author: gulli
"""
# %matplotlib qt
# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx

### NETWORK VARIABLES ###
n_nodes=1000
m_edges=200 

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2
d_u = 0.2
d_v = 0.8

### GENERATE RANDOM GRAPH ###
graphObject = nx.gnm_random_graph(n_nodes,m_edges)

### Laplacian matrix ###
laplacian_matrix = nx.laplacian_matrix(graphObject)

### DEFINING BASIC DATA ###
n_timepoints = 1500
deltat = 0.01

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n_nodes,n_timepoints))
v = np.zeros((n_nodes,n_timepoints))

u[:] = np.nan
v[:] = np.nan

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.uniform(-1,1,size=n_nodes)
v[:, 0] = np.random.uniform(-1,1,size=n_nodes)

j = 0
for i in range(1, n_timepoints):

    u[:, i] = deltat * (-d_u * laplacian_matrix * u[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * laplacian_matrix * v[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + v[:, i-1]

    if i % 50 == 0 :
        plt.figure(figsize=(7,7))

        plt.plot(u.T, v.T, linewidth=2, color='r', alpha=0.2)
        plt.plot(u[:,-1], v[:,-1], 'ko')

        plt.xlim(-1,1)
        plt.ylim(-1,1)

        plt.xlabel(r'u', size = 16)
        plt.ylabel(r'v', size = 16)

        plt.title(r'state-space trajecotries $(u(t),v(t))$ per node', size = 16, y = 1.02)
        plt.savefig(str(j).zfill(3)+'.png')

        plt.close()
        j += 1


