# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries
import numpy as np
import math as mt
import matplotlib.pyplot as plt
x = [0,1/4,1/2,3/4,1]
f = []
for i in x:
    f.append(np.cos((mt.pi*i)/2))
    
#define the polynomial 
def P(y):
    if(y>1/4):
        if(y>1/2):
            if(y>3/4):
                n = 3
            else:
                n = 2
        else:
            n = 1
    else:
        n = 0
    return f[n]+ ((f[n+1]-f[n])/(x[n+1]-x[n]))*(y-x[n])

#calculate the error
fdiff = []
for i in x:
    fdiff.append(((mt.pi)**2/4)*(np.cos((mt.pi*i)/2)))
errorbound = []
for i in range(0,4):
    errorbound.append(((1/8)*((x[i+1]-x[i])**2))*max(fdiff[i],fdiff[i+1]))
    
print('\nError Bound :')
print('\n')
for i in range(0,4):
    print('Between {:.2f} and {:.2f} = {:.4f}'.format(x[i],x[i+1],errorbound[i]))

#plotting 
plt.plot(x,f,'-r', label = 'q(x)')
plt.plot(x,f,'ob', label = 'nodes')
xtrue = np.arange(0,1.00,0.001)
ytrue = []
for i in xtrue:
    ytrue.append(np.cos((mt.pi*i)/2))
plt.plot(xtrue,ytrue,'-g',label = 'analytical')
plt.legend(loc = 'upper right')
plt.show()