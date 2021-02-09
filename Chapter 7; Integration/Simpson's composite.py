# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:53:34 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the library and define function 
import numpy as np
def f(x):
    return np.exp((x*x))

#n = 5
n = 5
x = [0.0,0.4,0.8,1.2,1.6,2.0]
S = 0
for i in np.arange (0,int(n/2)):
    h = (x[2*i+2]-x[2*i-2+2])/2
    S = S + (h/3)*(f(x[2*i-2+2])+f(x[2*i-1+2])+f(x[2*i+2]))
    
print(S) #value of intergral 

# n =10
n = 10
x = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]

J = 0
for i in np.arange (0,int(n/2)):
    h = (x[2*i+2]-x[2*i-2+2])/2
    J = J + (h/3)*(f(x[2*i-2+2])+f(x[2*i-1+2])+f(x[2*i+2]))
    
print(J) #value of intergral 
