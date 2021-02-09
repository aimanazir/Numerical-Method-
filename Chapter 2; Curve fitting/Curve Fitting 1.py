"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import relvent libraries
import matplotlib.pyplot as plt
import math as mt

#read the CF1.txt file
f = open('CF1.txt','r')
#make arrays and split the data into corresoponding parts
x = []
fx = []
plotx = [0.1,0.2]
ploty = []
errorx = []
for i in f:
    spl = i.split()
    x.append(float(spl[0]))
    fx.append(float(spl[1]))
    
#define our polynomial     
def p(y):
    return (x[1]-y)/(x[1]-x[0])*fx[0] + ((y-x[0])/(x[1]-x[0]))*fx[1]

print('The value of f(0.14) is ',p(0.14))

for i in plotx:
    ploty.append(p(i))
    
for i in plotx:
    errorx.append((4*i/mt.sqrt(mt.pi))*(mt.exp(-i**2)))

#calculate the error
error = 1/8*((x[1]-x[0])**2)*(max(errorx))
print('Error is ',error) 

#plot our result
plt.plot(x,fx,'-r')
plt.plot(0.14,p(0.14),'ok')
plt.show()