import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return ((np.exp(x))-1)/x
def f1(x):
    return ((x-1)*(np.exp(x)))/(x**2) + 1/(x**2)
def f2(x):
    return ((x**2-2*x+2)*(np.exp(x)))/(x**3) - 2/(x**3)
def f3(x):
    return (((x**3)-(3*x**2)+(6*x)-6)*(np.exp(x)))/(x**4) + 6/(x**4)
x = []
y = []
z = []
n = 20
h = 1/n
for i in np.arange(0.001,0.6,h):
    x.append(i)
    y.append(f(i))
    z.append(f(i)+h*f1(i)+((h**2)/2)*f2(i)+((h**3)/6)*f3(i))
    print('{:8.4f}{:8.4f}{:8.4f}'.format(i,f(i),f(i)+h*f1(i)+((h**2)/2)*f2(i)+((h**3)/6)*f3(i)))
    

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y,'-r',label = 'exact plot') #exact plot 
plt.plot(x,z,'ok',label = 'poly approx') #polynomial approx
plt.legend(loc = 'upper left')
plt.savefig("SIF180004 A2.pdf")
