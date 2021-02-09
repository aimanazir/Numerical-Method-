import numpy as np
f = open('trigono.txt','w')
x = np.arange(0,2*np.pi,0.01)
for i in x:
    print('{:.4f}{:8.4f}{:8.4f}'.format(i,np.sin(i),np.cos(i)),file = f)
    
f.close()


