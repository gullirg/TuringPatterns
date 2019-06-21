#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:11:12 2019

@author: Shaheim Ogbomo-Harmitt

This is a test script to test the Bifurcation_curve_ver2 module
"""

import matplotlib.pyplot as plt 
from networkx import nx
from Bifurcation_curve_ver2 import *
import numpy as np 

a = 1
b = -2
c = 2
d = -2
n=100 # 10 nodes
m=200 # 20 edges


G_ER = nx.gnm_random_graph(n,m)

Lap_ER  = nx.laplacian_matrix(G_ER).toarray()

dv = np.linspace(0,0.5,num = 100)
du = np.linspace(0,0.05,num = 100)

bi_obj = Bi_Curve(100,a,b,c,d,du,dv,Lap_ER)
val = bi_obj.Bi_Curve_1()