import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig        = plt.figure()
fs         = 20
N          = 20

circleAxe  = fig.add_subplot(1,1,1)
circleLn,  = plt.plot([],[],'ro')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleFrec = 1

def circle(c,f,n):
    return c*np.exp(-1j*2*np.pi*f*n*1/fs)

def init():
    return circleLn,
def update(n):
    circleLn.set_data(np.real(circle(1,circleFrec,n)),
                      np.imag(circle(1,circleFrec,n)))

    return circleLn,

ani=FuncAnimation(fig,update,N,init,interval=100 ,blit=False,repeat=True)
plt.show()
