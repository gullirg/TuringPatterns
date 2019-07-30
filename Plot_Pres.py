"""
Created on Wed Jul 24 16:15:31 2019

@author: Ogbomo-Harmitt
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#CREATE SUBPLOTS 7x7

fig, ax = plt.subplots(49)

n =200
c = 1

for i in range (-3,1,3):
    for k in range (-3,1,3):
        
        a = 1 
        b = 1
        trace  = i
        det = k 
        d = trace - a
        c = (det -a*d)/b
        
        I = np.identity(n)
        
        ### GENERATE RING GRAPH ###
        graph = nx.watts_strogatz_graph(n, 2, 0)
        
        ### CALCULATE EIGENVALUES OF LAPLACIAN (DIAGONALIZATION) ###
        w,v = np.linalg.eig(nx.laplacian_matrix(graph).toarray())
        
        ### GENERATE DIAGONALIZED LAPLACIAN ###
        Lambda = np.diag(w)
        
        ### CALCULATE STABILITY FOR DIFFERENT DIFFUSIVITIES ###
        Phase_Plane = []
        for d_u in np.linspace(0,0.05,50):
            temp = []
        
            for d_v in np.linspace(0,0.5,50):
                ### REACTIVE LAPLACIAN ###
                A = a * I - d_u * Lambda
                B = b * I
                C = c * I
                D = d * I - d_v * Lambda
                
                Gamma = np.block([
                        [A, B], 
                        [C, D]
                        ])
            
                ### EIGENVALUES OF REACTIVE LAPLACIAN ###
                y,z = np.linalg.eig(Gamma)
                Gamma_eig = np.real(y)
        
                ### FIND PERCENTAGE OF POSITIVE EIGENVALUES ###
                check = []
                for g in Gamma_eig:
                    if g > 0. :
                        check.append(1)
                    else:
                        check.append(0)
                
                value_norm = sum(check)/len(check) 
                temp.append(value_norm)
                    
            Phase_Plane.append(temp)
            
        ### GENERATE TRANSPOSE MATRIX ###
        matrix = np.transpose(np.matrix(Phase_Plane))
        
        ### CONTOUR PLOT ###
        x = np.linspace(0,0.05,50)
        y = np.linspace(0,0.5,50)
        xx, yy = np.meshgrid(x, y, sparse=True)
        z = matrix

        ax[c].plt.contourf(x,y,np.log(z), cmap = 'bone_r')
        c = c + 1
