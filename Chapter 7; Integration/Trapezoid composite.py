# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:08:49 2019

@author: Ahmad Aiman Mohd NAzir
"""
#import library and define function 
import numpy as np
def f(x):
    return np.exp((x*x))

#n=5
x = [0.0,0.4,0.8,1.2,1.6,2.0]
h = 0.4
sum = 0
for i in range(0,4):
    sum = sum + f(x[i+1])
    
T = h/2*(f(x[0])+2*sum+f(x[5]))
print(T) #value of intergral 


#n = 10
x1 = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
h = 0.2 
sum = 0
for i in range(0,9):
    sum = sum + f(x1[i+1])
    
P = h/2*(f(x1[0])+2*sum+f(x1[10]))
print(P) #value of intergral 
    
