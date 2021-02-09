import matplotlib.pyplot as plt
f = open('trigono.txt','r')
x = []
y = []
z = []
for i in f:
    spl = i.split()
    x.append(float(spl[0]))
    y.append(float(spl[1]))
    z.append(float(spl[2]))
    
f.close()
plt.plot(x,y,label = 'sine')
plt.plot(x,z,label = 'cosine')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sine and Cosine function')
plt.legend(loc = 'lower left')