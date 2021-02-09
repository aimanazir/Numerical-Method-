# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:59:56 2019

@author: Ahmad Aiman B. Mohd Nazir
"""
#import the libraries 
import numpy as np
import matplotlib.pyplot as plt

#define the functions 
def f(x):
    return 0.5-x*np.exp(-x**2)

def fp(x):
    return (2.0*x**2-1.0)*np.exp(-x**2)

def fpp(x):
    return (2.0*x*(3.0-2.0*x**2))*np.exp(-x**2)

#looping for Newton Optimazation 
x = 1.0
print('\n')
print('{:5}{:12}{:12}{:12}{:12}'.format('i','x_i','x_i+1','f(x_i+1)','Delta_x'))
for i in range(0,10):
    xi = x - fp(x)/fpp(x)
    delx = abs(xi-x)
    print('{:d}{:12.6f}{:12.6f}{:12.6f}{:12.6f}'.format(i,x,xi,f(xi),delx))
    plt.plot(xi,f(xi),'-xb')
    x = xi
    if(delx < 10**(-5)):
        print('\nThe minumum value of f(x) = {:.6f} at {:.6f}'.format(f(xi),xi))
        break
    
#calculate the exact values
xtrue = np.arange(0,2.5,0.001)
ytrue = []
for i in xtrue:
    ytrue.append(f(i))

#plot the result 
plt.plot(xtrue,ytrue,'-r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Newton Method for Optimisation')
plt.savefig('Newton Method for Optimazation.pdf')