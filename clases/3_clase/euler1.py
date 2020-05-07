import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig        = plt.figure()
fs         = 10
N          = 10

circleAxe  = fig.add_subplot(1,1,1)
circleLn,  = plt.plot([],[],'ro')
circleAxe.grid(True)
circleAxe.set_xlim(-2,2)
circleAxe.set_ylim(-2,2)
circleFrec = 1

circle  = lambda c,f,n: c*np.exp(-1j*2*np.pi*f*n*1/fs)

def update(n):
    circleLn.set_data(np.real(circle(1,circleFrec,n)),
                      np.imag(circle(1,circleFrec,n)))

    return circleLn,

ani=FuncAnimation(fig,update,N,interval=1000 ,blit=False,repeat=True)
plt.show()
