"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries
import math as mt
import numpy as np
import matplotlib.pyplot as plt
x = [1/4,1/2,1]
fx = [-2,-1,0]
#define our polynomial 
def P(y):
    if(y<0.5):
        n = 0
    else:
        n = 1
    return fx[n]+((fx[n+1]-fx[n])/(x[n+1]-x[n]))*(y-x[n])

print('Value of q(0.4) and q(0.8) are {:.4f} and {:.4f}'.format(P(0.4),P(0.8)))
#plot the approximate graph 
plt.plot([0.4,0.8],[P(0.4),P(0.8)],'xk')
plt.plot(x,fx,'-r')
plt.plot(x,fx,'ob')
    
xtrue = []
fxtrue = []
for i in np.arange(0.2,1.0,0.001):
    xtrue.append(i)
    fxtrue.append(mt.log2(i))
#plot the exact graph    
plt.plot(xtrue,fxtrue,'-g')
plt.show()

#calculate the error
fxdiff = []
for i in x:
    fxdiff.append((1/(mt.log(2)))*(1/(i**2)))
    
errorbound = []
for i in range(0,2):
    errorbound.append(((1/8)*((x[i+1]-x[i])**2))*max(fxdiff[i],fxdiff[i+1]))
    
for i in range(0,2):
    print('The error bound between {:0.2f} and {:0.2f} = {:0.4f}'.format(x[i],x[i+1],errorbound[i]))
    
    