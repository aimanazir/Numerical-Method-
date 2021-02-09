# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:06:14 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries 
import numpy as np
from scipy.linalg import solve as sv
#define our matrix  a and b 
a = np.array([[4,2,-1],[1,4,1],[2,-1,4]])
b = np.array([[5],[12],[12]])
#solve it 
x = sv(a,b)
#print the result 
print(x)
