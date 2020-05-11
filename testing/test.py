import matplotlib.pyplot as plt
import numpy as np

N  = 100
fs= 1000
t  = np.arange(0.02, 0.05, 1/fs)
fig = plt.figure(1)
ax1 = fig.add_subplot(1,1,1)
ax1.plot(t, np.sin(2*np.pi*t*0.1*fs),"b-")
ax1.grid(True)
#
ax2 = fig.add_subplot(1,1,1)
ax2.plot(t, np.sin(2*np.pi*t*1.1*fs),"r-")
ax2.grid(True)

N  = 100
fs2= 100*fs
t2  = np.arange(0.02, 0.05, 1/fs2)
fig = plt.figure(1)
ax1 = fig.add_subplot(1,1,1)
ax1.plot(t2, np.sin(2*np.pi*t2*0.1*fs),"g-")
ax1.grid(True)

ax2 = fig.add_subplot(1,1,1)
ax2.plot(t2, np.sin(2*np.pi*t2*1.1*fs),"y-")
ax2.grid(True)
plt.show()
