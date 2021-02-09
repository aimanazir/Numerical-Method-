"""
Created on Wed Nov  6 17:35:27 2019

@author: Ahmad Aiman Mohd Nazir
"""
#import the libraries 
import matplotlib.pyplot as plt
import numpy as np
x = [-1.0,-0.5,0.0,0.5,1.0]
fx = [1/26,4/29,1,4/29,1/26]
#define our approximate polyniminal for each mesh points
def p(y):
    if(y<-0.5):
        n=0
        return fx[n]+((fx[n+1]-fx[n])/(x[n+1]-x[n]))*(y-x[n])
    elif(y<0.5):
        n=1
        return fx[n]+((fx[n+1]-fx[n])/(x[n+1]-x[n]))*(y-x[n])

    elif(y<1):
        n=3
        return fx[n]+((fx[n+1]-fx[n])/(x[n+1]-x[n]))*(y-x[n])

       
print('q value are: q(-0.1)',p(-0.1),"and q(-0.2)",p(-0.2))

fxdiff = []
for i in x:
    fxdiff.append(abs((50*((75*i*i)-1))/(((25*i*i)+1)**3)))
errorbound = []
for i in range(0,4):
    errorbound.append(((1/8)*((x[i+1]-x[i])**2))*max(fxdiff[i]*(np.exp(-i*2)),fxdiff[i+1]*(np.exp((-i+1)*2))))


print('\nError bounds:')
for i in range(0,4):
    print('Between {:.2f} and {:.2f} = {:.4f}'.format(x[i],x[i+1],errorbound[i]))

#plot the apporimate graph
plt.plot([-0.1,-0.2],[p(-0.1),p(-0.2)],'xk')
plt.plot(x,fx,'-r',label = 'q(x)')
plt.plot(x,fx,'ob',label = 'nodes')

xtrue = []
fxtrue = []
for i in np.arange(-1.5,1.5,0.001):
    xtrue.append(i)
    fxtrue.append((1+(25*(i**2)))**(-1))

#plot the exact graph
plt.plot(xtrue,fxtrue,'-g',label = 'analytical')
plt.legend(loc = 'upper left')
plt.show()
