# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:28:58 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import libraries 
import numpy as np
#define our function
def f(x,y):
    return y+x

#Euler method calculation
n = 4
h = 1/n
x = 0.0
y = 1.0
for i in range(0,n+1):
    y1 = y + h*f(x,y)
    exact = 2*np.exp(x)-x-1
    error = abs(y-exact)
    print('{:.4f}{:8.4f}{:8.4f}{:8.4f}{:8.4f}'.format(x,y,y1,exact,error))
    x = x + h
    y = y1
    
    
