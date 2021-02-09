# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:19:14 2019

@author: User
"""
#import the libraries 
import numpy as np
import matplotlib.pyplot as plt
#define the function
def f(N,tau):
    return (-N/tau)

#Euler method for rate of decay of nuclei
t = 0
tau = 1
N = 10.0 #kg
n = 100
h = 0.05
print(' t        N')
for i in range(0,n+1):
    N1 = N + h*f(N,tau)
    print('{:.4f}{:8.4f}'.format(t,N1))
    t = t + h
    N = N1
    plt.plot(t,N,'xb')

#calculate the exact values 
x = np.arange(0,5,0.001)
y = []
for i in x:
    y.append(10.0*np.exp(-i/tau))

#plot the result 
plt.plot(x,y,'-r')
plt.title('Rate of decay')
plt.xlabel('time, hours')
plt.ylabel('Number of nuclei,N (in kg)')