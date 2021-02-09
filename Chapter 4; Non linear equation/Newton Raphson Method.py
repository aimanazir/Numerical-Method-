# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:53:50 2019

@author: Ahmad Aiman Mohd Nazir 
"""
#import the libraries 
import numpy as np
import matplotlib.pyplot as mpl

#define our functions 
def f(x):
    return 7.0*np.sin(x)*np.exp(-x)-1.0 

def fp(x):
    return 7*np.exp(-x)*(np.cos(x)-np.sin(x))

#Newton - Raphson method 
x = 0.3
for i in range (0,10):
    xi = x - f(x)/fp(x) 
    delx = abs(xi-x)
    x = xi
    if delx > 1.0e-4:
      print('{:d}{:8.4f}{:8.4f}{:8.4f}'.format(i,xi,f(x),delx))

print(x,f(x))      
mpl.plot(x,f(x),'bx')


#plot our result 
x = np.arange(0,1,0.001)
mpl.title ('Newton Raphson Method')
mpl.xlabel('x-axis')
mpl.ylabel ('y-axis')
mpl.plot(x,f(x),'g-')
mpl.savefig('NRM.pdf')


mpl.show()
