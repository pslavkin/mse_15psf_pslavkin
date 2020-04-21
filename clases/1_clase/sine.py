import matplotlib.pyplot as plt
import  numpy as np

fig = plt.figure(1)

TC=0.001
tc  = np.arange(0.0, 1.0, TC)
ax1 = fig.add_subplot(211)
ax1.plot(tc, np.sin(2*np.pi*tc),'b-')
ax1.grid(True)

TD=0.1
td  = np.arange(0.0, 1.0, TD)
ax2 = fig.add_subplot(212)
ax2.plot(td, np.sin(2*np.pi*td),'ro')
ax2.grid(True)

plt.show()
