"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read txt file 
f = open('CA4(2).txt','w')
xk1 = np.arange(0,121,10)
yk1 = [0.716,0.893,1.055,1.134,1.167,1.281,1.994,2.500,3.151,4.300,5.308,4.966,10.919]

#plot raw data   
plt.scatter(xk1,yk1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph y against x')

for i in range(0,13):
    print('{}{:8.3f}'.format(xk1[i],yk1[i]),file =  f)
    
f.close()
df = pd.read_fwf('CA4(2).txt',sep = ' ',header = None)
df.columns = ['xk','yk']
print(df)
plt.show()

#calculate for linear regression 
X = xk1
Y = np.log(yk1)
X2 = X**2
Y2 = Y**2
XY = X*Y
sx = sum(X)
sy = sum(Y)
sx2 = sum(X2)
sxy = sum(XY)
m = (13*sxy-sx*sy)/(13*sx2-(sx**2))
b = (sx2*sy-sx*sxy)/(13*sx2-(sx**2))
print('\nThe gradient is {:.4f} and b is {:.4f}'.format(m,b))

def y(x):
    return m*x+b

#plot the linear regression and coressponding to the actual data
x1 = np.arange(0,121,1)
y1 = []
ytrue = []
for i in x1:
    y1.append(y(i))

plt.scatter(X,Y,color = 'blue')
plt.plot(x1,y1,color = 'red')
plt.show()

