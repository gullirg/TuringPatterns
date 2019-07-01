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
n=100 # 10 nodes
m=200 # 20 edges

### REACTIVE FUNCTION VARIABLES ###
a = 1
b = -2
c = 2
d = -2
d_u = 0.2
d_v = 0.8

I = np.identity(n)

### GENERATE RANDOM GRAPH ###
# =============================================================================
# G=nx.gnm_random_graph(n,m)
# =============================================================================
G=nx.grid_graph(dim=[10 ,10], periodic=False)

### Laplacian matrix ###
L = nx.laplacian_matrix(G)

### DEFINING BASIC DATA ###
t0 = 0
u0 = np.zeros([n])
v0 = np.zeros([n])
tf = 10
#deltat = (tf - t0) / (n-1)
deltat =0.001

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

### CONCENTRATIONS DIFFERENCE ###
z = np.zeros((n,tf))

for m in range(9):
    z[:, m] = u[:, m] - v[:, m]

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

pos = dict( (n, n) for n in G.nodes() )


for k in range(9):
    nx.draw(G, node_color = z[:, k], pos = pos, cmap= 'Blues', with_labels = False)
    
    #plt.savefig('/Users/gulli/Google Drive/KURF/Net_'+str(k) +'.png')
    plt.show()






















