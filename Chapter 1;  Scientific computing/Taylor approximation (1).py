"""
Created on Wed Nov  6 12:05:37 2019

@author: Ahmad Aiman Mohd Nazir
"""


import numpy as np
import matplotlib.pyplot as plt
import math as mt

def f(x):
    return np.sqrt(x+1)
def f1(x):
    return ((x+1)**(-1/2))/2
def f2(x):
    return (-((x+1)**(-3/2)))/4
def f3(x):
    return (3/8)*((x+1)**(-5/2))

x =[]
y =[]
z =[]
n = 4
h = 1/n
for i in np.arange(0.01,1.01,h):
    x.append(i)
    y.append(f(i))
    z.append(f(i) + h*f1(i) + (h**2/mt.factorial(2))*f2(i))
    print("{:8.5f}{:10.5f}{:10.5f}".format(i,f(i),f(i) + h*f1(i) + (h**2/mt.factorial(2))*f2(i)))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y,'-r')
plt.plot(x,z,'ok')
    
              
#error
Rn = ((h**3)/mt.factorial(3))*f3(1.0)
print('Error = ', Rn)