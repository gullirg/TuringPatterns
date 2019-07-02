#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:42:08 2019

@author: Shaheim Ogbomo-Harmitt & Guglielmo Reggio

This module generates and plots the Bifurcation Curve of given complex network 
Laplacian matrix.

Class constructor parameters:

    n - number of nodes of complex network
    
    Given that the asymptotic stability of the equilbrium point of the 
    reaction-diffusion model is
    
                        a + d < 0 and ad - bc > 0 
                        
    a,b,c and d repersent these parameters.
    
    L - Laplacian matrix of complex network
    
Bifurcation curve function:
        
    Prototype - Bi_Curve(du,dv)
    
    du - array of U diffusion coeffcient values 
    dv - array of v=V diffusion coeffcient values
    
    Return - Plot of Bifurcation Curve and an array of the percentage
             of postive eigenvalues of each system.
             

Reaction - Diffusion System with applied Forward Euler Method function:
    
    Prototype - RDForward_Euler(u0,v0,du_val,dv_val,delta_t,num_steps)
    
    u0 - Intial values of biological concerntration U
    u0 - Intial values of biological concerntration V
    du_val - diffusion coeffcient of U
    dv_val - diffusion coeffcient of V
    delta_t - time step of Euler Method
    num_steps - number of iterations of Euler Method
    
    
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
 

# CLASS CONSTRUCTOR

class RD_Net:
    
    def __init__(self,n,a,b,c,d,L):
        self.n = n 
        self.a = a 
        self.b = b
        self.c = c
        self.d = d
        self.L = L

    # THE INPUTS DU & DV ARE ARRYS OF THE EACH DIFFUSION COEFFCIENT 
        
    def Bi_Curve(self,du,dv):
        
       # DIAGONALISING THE LAPLACIAN MATRIX  
        
        Eigen_Plot_vals = np.empty([len(du),len(du)])
        eig_val,eig_vec = np.linalg.eig(self.L)
        I = np.identity(self.n)
        Lap_Diag = np.diag(eig_val)
        
        # FINDING EIGENVALUES OF THE REACTIVE LAPLACIAN AND DETERMINING PLOTTING PARAMETERS
            
        for g in range (len(dv)):
            for k in range (len(dv)):
            
                A = self.a * I - du[g] * Lap_Diag
                B = self.b * I
                C = self.c * I
                D = self.d * I - dv[k] * Lap_Diag
        
                Gamma = np.block([[A, B], [C, D]])
        
                Reac_Lap_eigenvalue,Reac_Lap_eigenvector = np.linalg.eig(Gamma)
                
                Reac_Lap_eigenvalue = np.real(Reac_Lap_eigenvalue)
                
                # CALCULATING PERCENTAGE OF POSTIVE EIGENVALUES 
                
                counter = 0 
                for i in Reac_Lap_eigenvalue:
                    if i > 0:
                        counter += 1
        
                Eigen_Plot_vals[g][k] = counter/len(Reac_Lap_eigenvalue)
                    
        # PLOTTING BIFURCATION CURVE
    
        mpl.rcParams['text.usetex'] = False
        plt.contourf(du,dv, Eigen_Plot_vals.transpose(), cmap = plt.cm.binary)
        plt.xlabel(r"$d_{\mathrm{u}}$", fontsize = 'xx-large', fontstyle = 'italic')
        plt.ylabel(r"$d_{\mathrm{v}}$", fontsize = 'xx-large', fontstyle = 'italic')
        ax = plt.gca() 
        ax.xaxis.set_label_coords(1, -0.1)
        ax.yaxis.set_label_coords(-0.1, 1)
        plt.colorbar()
        plt.show()
        
        return Eigen_Plot_vals
    
    def RDForward_Euler(self,u0,v0,du_val,dv_val,delta_t,num_steps):
        
        # INTIALISING PARAMETERS
        
        U = np.zeros((self.n,num_steps))
        V = np.zeros((self.n,num_steps))
        U[:, 0] = u0
        V[:, 0] = v0

        # APPLYING FORWARD EULER METHOD
        
        for i in range(1, num_steps):
            
            U[:, i] = delta_t * (-du_val * np.matmul(self.L, U[:, i-1]) + self.a * U[:, i-1] + self.b * V[:, i-1]) + U[:, i-1]
            V[:, i] = delta_t * (-dv_val * np.matmul(self.L,V[:, i-1]) + self.a * U[:, i-1] + self.b * V[:, i-1]) + V[:, i-1]
            
        # PLOTTING GRAPH
        
        plt.figure()
        plt.plot(U.T, V.T, markersize=0.7, linewidth = 0.4)
        plt.xlabel("u", fontsize = 'xx-large', fontstyle = 'italic')
        plt.ylabel("v", fontsize = 'xx-large', fontstyle = 'italic')
        ax = plt.gca() 
        ax.xaxis.set_label_coords(1, -0.1)
        ax.yaxis.set_label_coords(-0.1, 1)
        plt.show()
        plt.tight_layout()

        return U,V
        
