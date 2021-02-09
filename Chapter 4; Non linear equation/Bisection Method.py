# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:22:38 2019

@author: Ahmad Aiman Mohd Nazir 
"""

import numpy as np
#import math as mt
import matplotlib.pyplot as mpl

#function f(x) = 3.0 - 2.0^x
def f(x):
    return -12.0-21.0*x+18.0*x**2-2.75*x**3

#this range is used for plotting
x = np.arange(-2.0,0.5,0.2)

#error bound
tol = 0.001

#[a,b] is the range for the function
a = -1.0
b = 0.0

#calculate mid-point
c = a+0.5*(b-a)

#find the difference
delx = abs(b-a)

#start bisection calculation

for i in range(0,10):
  c = a+0.5*(b-a)
  if f(c)*f(a)<0:
    a = a
    b = c
    delx = abs(b-a)
  else:
       a = c
  if delx > tol:
   print("{:8.4f} {:8.4f} {:8.4f}{:8.4f} {:8.4f} {:8.4f} ".format(a,c,b,f(a),f(b),delx))

#plotting format
print(a,f(a))

#to create title
mpl.title('Solution for bisection method:  $f(x)=-12.0-21.0x+18.0x^2-2.75x^3$')

#plot the convergenced function
mpl.plot(a,f(a),'ob')
mpl.plot(b,f(b),'xk')

#label x-axis
mpl.xlabel('x')
#label y-axis
mpl.ylabel('f(x)')

#plot the exact function
mpl.plot(x,f(x),'g-')
mpl.savefig('BSM.pdf')

mpl.show()