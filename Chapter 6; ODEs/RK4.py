# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:51:45 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import libarary and define function
import numpy as np
def f(x,y):
    return x+y

#Runge Kutta 4th order
n = 4
h = 1/n
y = 1.0
x = 0.0

for i in range(0,n+1):
    k1 = f(x,y)
    k2 = f(x+h/2,y+(h/2)*k1)
    k3 = f(x+h/2,y+(h/2)*k2)
    k4 = f(x+h,y+h*k3)
    y1 = y+h/6*(k1+2*k2+2*k3+k4)
    exact = 2*np.exp(x)-x-1
    error = abs(y1-exact)
    print('{:.4f}{:8.4f}{:8.4f}{:8.4f}{:8.4f}'.format(x,y,y1,exact,error))
    x=x+h
    y=y1
    
    