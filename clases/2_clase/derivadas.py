import numpy as np
import matplotlib.pyplot as plt

N    = 1000
dx   = 0.01
t    = np.arange(0,dx*N,dx)
f    = [t,t**2,np.sin(t),np.exp(t)]

fig  = plt.figure()

for i in range(len(f)):
    contiAxe = fig.add_subplot(4,1,i+1)
    y=np.real(np.diff(f[i])/dx)
    plt.plot(t,np.real(f[i]),'r-',t[:-1],y,'b-')

plt.show()
