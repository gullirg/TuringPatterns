#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:03:19 2019

@author: Ogbomo-Harmitt
"""

import matplotlib.pyplot as plt 
from networkx import nx
from RD_MODULE_VER_3 import *
import numpy as np

a = 1
b = -2
c = 2
d = -2
n = 100
m = 200
G_ER = nx.gnm_random_graph(n,m)


Lap_ER  = nx.laplacian_matrix(G_ER).toarray()

dv = np.linspace(0,0.5,num = 100)
du = np.linspace(0,0.05,num = 100)

bi_obj = RD_Net(n,a,b,c,d,Lap_ER)

val = bi_obj.Bi_Curve(du,dv)


du_val = 0.2
dv_val = 0.8
num_steps = 2000
delta_t = 0.001
u = np.random.rand(n)
v = np.random.rand(n)
gg = np.matmul(Lap_ER,u)


val2 = bi_obj. RDForward_Euler(u,v,du_val,dv_val,delta_t,num_steps)