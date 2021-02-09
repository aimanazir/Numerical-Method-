# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:32:08 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries 
import numpy as np
from scipy.linalg import cholesky as ch
import scipy.linalg as sp

#define the matrix 
a = np.array([[8,20,16],[20,80,50],[16,50,60]])
b = np.array([[100],[250],[100]])

#Cholesky method 
U = ch(a)
L = np.transpose(U)
print(U)

#print result 
print('\n')
print(L)
print('\n')
print(sp.solve(a,b))



