# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:09:21 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries 
import numpy as np
import matplotlib.pyplot as mpl

#function to solve
def f(x):
   return 2-np.exp(x)

# secant method
x0  = 1.0
x1 = 0.0
tol = 1.0e-5
f0 = f(x0)
f1 = f(x1)

for i in range (0,100):
  xx = x1 - f1*((x1-x0)/(f1-f0)) #secant formula
  delx = abs(xx-x1)
#  print(x0,x1,xx,f0,f1)
  if delx > tol:
     print("{:f} {:f} {:f} {:f} {:f} ".format(x0,x1,xx,f(xx),delx))
     x0 = x1
     x1 = xx

#print the result and marks the solution     
print(xx,f(xx))    
mpl.plot(xx,f(xx),'bx')

#plot our result 
x = np.arange(-3,1,0.1)
mpl.title ('Secant Method')
mpl.xlabel('x-axis')
mpl.ylabel ('y-axis')
mpl.plot(x,f(x),'g-')
mpl.savefig('Secant Method.pdf')

mpl.show()
   
