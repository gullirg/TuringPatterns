"""
Created on Tue Jun 18 17:02:38 2019

@author: Shaheim Ogbomo-Harmitt

@co-author: Guglielmo Reggio

This module generates the Bifurcation Curve of given complex network 
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

    def Reac_EigenVals(self):
        
        EV_plt_vals = np.empty([len(self.dv),len(self.dv)])
        
        for g in range (len(self.dv) - 1):
        
            for k in range (len(self.dv) - 1):
                
                
                I = np.identity(self.n)
    
                Lap_Diag = np.diag(self.L)
            
                A = self.a * I - self.du[g] * Lap_Diag
                B = self.b * I
                C = self.c * I
                D = self.d * I - self.dv[k] * Lap_Diag
    
                Gamma = np.block([[A, B], [C, D]])
    
                Reac_Lap_eigenvalue,Reac_Lap_eigenvector = np.linalg.eig(Gamma)
            
                Reac_Lap_eigenvalue = np.real(Reac_Lap_eigenvalue)
            
                Eigen_Bin_vals = np.empty([len(Reac_Lap_eigenvalue),1])
    
                for i in range (len(Reac_Lap_eigenvalue)):
                    
                    if Reac_Lap_eigenvalue[i] >= 0:
                        Eigen_Bin_vals[i] = 0
                    else:
                        Eigen_Bin_vals[i] =1
                        
            EV_plt_vals[g][k] = np.mean(Eigen_Bin_vals)
                
        
        return EV_plt_vals
    
        
        

        

        