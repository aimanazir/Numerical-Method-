# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:33:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries 
import numpy as np
from scipy.linalg import lu_solve,lu_factor

#define the matrix a and b
a = np.array([[4,2,-1],[1,4,1],[2,-1,4]])
b = np.array([[5], [12], [12]])

#LU factorization method
LU = lu_factor(a)
x = lu_solve(LU,b)

#print results
print(LU)
print('\n')
print(x)
