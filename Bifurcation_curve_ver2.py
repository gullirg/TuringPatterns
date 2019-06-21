"""
Created on Tue Jun 18 17:02:38 2019

@author: Shaheim Ogbomo-Harmitt & Guglielmo Reggio

This module generates and plots the Bifurcation Curve of given complex network 
Laplacian matrix.

Class constructor parameters:

    n - number of nodes of complex network
    
    Given that the asymptotic stability of the equilbrium point of the 
    reaction-diffusion model is
    
                        a + d < 0 and ad - bc > 0 
                        
    a,b,c and d repersent these parameters.
    
    du - diffusion coeffcient of u
    dv - diffusion coeffcient of v
    L - Laplacian matrix of complex network
    
Reac_EigenVals function:
        
    This function returns a 2D-array of the mean Eigenvalue of each 
    reaction-diffussion system with its respective coeffcients.
    
    
    
"""
import numpy as np 
import matplotlib.pyplot as plt

class Bi_Curve:
    
    def __init__(self,n,a,b,c,d,du,dv,L):
        self.n = n 
        self.a = a 
        self.b = b
        self.c = c
        self.d = d
        self.du = du
        self.dv = dv
        self.L = L
                    
    def Bi_Curve_1(self):
            
        Eigen_Bin_vals = np.empty([len(self.du),len(self.du)])
        eig_val,eig_vec = np.linalg.eig(self.L)
        I = np.identity(self.n)
        Lap_Diag = np.diag(eig_val)
            
        for g in range (len(self.dv)):
            for k in range (len(self.dv)):
            
                A = self.a * I - self.du[g] * Lap_Diag
                B = self.b * I
                C = self.c * I
                D = self.d * I - self.dv[k] * Lap_Diag
        
                Gamma = np.block([[A, B], [C, D]])
        
                Reac_Lap_eigenvalue,Reac_Lap_eigenvector = np.linalg.eig(Gamma)
                
                Reac_Lap_eigenvalue = np.real(Reac_Lap_eigenvalue)
                
                check = False 
                    
                for i in Reac_Lap_eigenvalue:
                    if i > 0. :
                        check = True 
        
                if check == True:
                    Eigen_Bin_vals[g][k] = 1
            
                else:
                    Eigen_Bin_vals[g][k] = 0
        
        fig = plt.figure()
        fig.suptitle('Bifurcation Curve', fontsize = 16)
        plt.xlabel('du', fontsize = 12)
        plt.ylabel('dv', fontsize = 10)
        plt.pcolormesh(self.dv, self.du, Eigen_Bin_vals.transpose())
        plt.colorbar()
        plt.show()        
        return Eigen_Bin_vals
                
            
        

        

        