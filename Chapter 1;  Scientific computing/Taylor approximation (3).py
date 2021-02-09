# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:05:37 2019

@author: Ahmad Aiman Mohd Nazir
"""

import math as mt
import numpy as np

def f(x):
    return np.exp(x)  #define the original function

def g(x):
    return 1+x+(x**2/mt.factorial(2))+(x**3/mt.factorial(3))+(x**4/mt.factorial(4)) #define expansion term

i = float(input('x = ')) #input the value of x

print('\nThe value for exponential(x) is {:.9f}'.format(f(i))) #value for exp
print('The value for expansion term is {:.9f}'.format(g(i))) #value for expansion term

#relative error
rerror = abs((f(i)-g(i))/f(i))*100 #calculate the relative error
print('\nThe relative error is {:.12f}'.format(rerror)) #print value of relative error