# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:59:06 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import library and define the function
import numpy as np
def f(x,y):
    return x+y

#Runge Kutta Second order calculation
n = 10
h = 1/n
y = 1.0
x = 0.0
for i in range(0,n+1):
    k1 = f(x,y)
    k2 = f(x+h,y+h*k1)
    y1 = y+h/2*(k1+k2)
    exact = 2*np.exp(x)-x-1
    error = abs(y-exact)
    print('{:.4f}{:8.4f}{:8.4f}{:8.4f}{:8.4f}'.format(x,y,y1,exact,error))
    x=x+h
    y=y1

    
    
