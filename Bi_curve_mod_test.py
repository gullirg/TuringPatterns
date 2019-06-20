#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:43:35 2019

@author: Shaheim Ogbomo-Harmitt

This is a test script to test the Bifurcation_curve module 
"""

import matplotlib.pyplot as plt 
from networkx import nx
from Bifurcation_curve import *
import numpy as np 

a = 1
b = -2
c = 2
d = -2

G_ER = nx.erdos_renyi_graph(200,0.7)

Lap_ER  = nx.laplacian_matrix(G_ER).toarray()

dv = np.linspace(0,0.5,num = 100)
du = np.linspace(0,0.05,num = 100)

bi_obj = Bi_Curve(200,a,b,c,d,du,dv,Lap_ER)
val = bi_obj.Reac_EigenVals()

