"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read txt file 
f = open("Conductivity(raw).txt","r")
df = pd.read_fwf('Conductivity(raw).txt',sep= " ",header=None)
df.columns = ['xk','yk']

#plot the raw data 
plt.scatter(df['xk'],df['yk'],label = 'raw data')
plt.xlabel('T')
plt.ylabel('Conductivity')
plt.title('Conductivity versus T')
plt.legend(loc = 'upper right')
plt.show()

#calculate the corresponding values for linear regression
sumx = sum(df['xk'])
sumx2 = sum((df['xk'])**2)
sumy = sum(df['yk'])
sumxy = sum(df['xk']*df['yk'])
print('\nSum of \nX: {:.4f}\nY: {:.4f}\nX^2: {:.4f}\nXY: {:.4f}'.format(sumx,sumy,sumx2,sumxy))

#calculate gradient and y-intercept
m = (len(df['xk'])*(sumxy)-(sumx*sumy))/(len(df['xk'])*(sumx2)-((sumx)**2))
b = ((sumx2*sumy)-(sumx*sumxy))/((len(df['xk'])*sumx2)-((sumx)**2))
print('\nThe gradient is {:.9f} and b is {:.4f}'.format(m,b))

#plot the linear regression and actual plot 
x = np.arange(0,1000,1)
fig,(ax1,ax2) = plt.subplots(1,2)
ax1.plot(df['xk'],df['yk'],'ob',label = 'Conductivity & T')
ax1.plot(x,m*x+b,'-r',label = 'linear')
ax1.set_title('Conductivity versus T')
ax1.set_xlabel('x')
ax1.set_ylabel('Conductivity')
ax1.legend(loc = 'upper right')
ax2.plot(df['xk'],df['yk'],'ob',label = 'Point')
ax2.plot(df['xk'],df['yk'],'-r',label = 'Curve')
ax2.set_title('Conductivity versus T')
ax2.set_xlabel('T')
ax2.set_ylabel('Conductivity')
ax2.legend(loc = 'upper right')
plt.tight_layout()
plt.show()
