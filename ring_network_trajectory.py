#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:50:39 2019

@author: gulli
"""
# %matplotlib qt
# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command

### NETWORK VARIABLES ###
n=100 # nodes

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -1.7
c = 1.9
d = -2
d_u = 0.7
d_v = 0.1

I = np.identity(n)

### DEFINING BASIC DATA ###
t0 = 0
u0 = np.zeros([n])
v0 = np.zeros([n])
tf = 100
#deltat = (tf - t0) / (n-1)
deltat = 0.1

### DEFINING t-VALUES ###
t = np.linspace(t0,tf,n)

### GENERATE RANDOM GRAPH ###
# =============================================================================
# G=nx.gnm_random_graph(n,m)
# =============================================================================
G=nx.watts_strogatz_graph(n, 2, 0)

### Laplacian matrix ###
L = nx.laplacian_matrix(G)

### INITIALIZING ARRAY FOR p-VALUES ###
u = np.zeros((n,tf))
v = np.zeros((n,tf))

### FOR LOOP FOR EULER'S METHOD ###
u[:, 0] = np.random.rand(n)
v[:, 0] = np.random.rand(n)

for i in range(1, tf):
    u[:, i] = deltat * (-d_u * L * u[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + u[:, i-1]
    v[:, i] = deltat * (-d_v * L * v[:, i-1] + a * u[:, i-1] +b * v[:, i-1]) + v[:, i-1]



### CONCENTRATIONS DIFFERENCE ###
z = np.zeros((n,tf))

for m in range(tf):
    z[:, m] = u[:, m] - v[:, m]


pos = nx.circular_layout(G)

for k in range(tf):
    nx.draw_networkx(G, node_color = z[:, k], pos = pos, cmap= 'Blues', with_labels = False)
    
    #plt.savefig('./Ring_'+str(k) +'.png')
    plt.show()
    print(k)


### ASSIGN CONCENTRATIONS AS NODE ATTRIBUTES ###
# =============================================================================
# values = {}
# 
# for j in range(len(u[:, tf - 1])):
#     #values[j] = u[:, 9][j] - v[:, 9][j]
#     values[j] = z[:, 9][j]
#    
# nx.set_node_attributes(G, 'values', values)
# =============================================================================

# =============================================================================
# nx.draw(G, pos)
# node_labels = nx.get_node_attributes(G,'values')
# nx.draw_networkx_labels(G, pos, labels = node_labels)
# plt.show()
# =============================================================================