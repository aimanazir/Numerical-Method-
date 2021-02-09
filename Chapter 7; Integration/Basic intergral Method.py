# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:34:51 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the ;ibrary 
import numpy as np

#define the function to integral 
def f(x):
    return np.exp(x*x)
a = 0
b = 2
#mid-point
m = (b-a)*f((a+b)/2)
print(m)

#trapezoid rule
t = (b-a)/2*(f(a)+f(b))
print(t)

#simpson's rule
s = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
print(s) 
