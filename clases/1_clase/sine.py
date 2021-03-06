import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1)
Nc=1000
tc = np.linspace(0, 1, Nc)
ax1 = fig.add_subplot(2,1,1)
ax1.plot(tc, np.sin(2*np.pi*tc),"b-")
ax1.grid(True)

Nd=10
td = np.linspace(0, 1, Nd)
ax2 = fig.add_subplot(2,1,2)
ax2.plot(td, np.sin(2*np.pi*td),"ro")
ax2.grid(True)

plt.show()
