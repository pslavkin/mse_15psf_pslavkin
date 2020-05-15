import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N=40
fs=20

fig = plt.figure(1)

circleAxe = fig.add_subplot(2,2,1)
circleLn, = plt.plot([],[],'ro')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleLn.set_label(0)
circleLg=circleAxe.legend()
tData=[]

signalAxe = fig.add_subplot(2,2,2)
signalLn, = plt.plot([],[],'b-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalData=[]
signalFrec=4

def signal(f,n,c):
    return c*np.sin(2*np.pi*f*n*1/fs)
def circle(f,n,c):
    return c*np.exp(-2j*np.pi*f*n*1/fs)


def update(n):
    global tData, signalData
    tData.append(n/fs)
    signalData.append(signal(signalFrec,n,1))
    circleLn.set_data(np.real(circle(1,n,1)) ,np.imag(circle(1,n,1)))
    signalLn.set_data(tData ,signalData)

    circleLn.set_label(n)
    circleLg=circleAxe.legend()
    if n==N-1:
        tData=[]
        signalData=[]
    return circleLn,circleLg,signalLn,

ani=FuncAnimation(fig,update,N,None,interval=100,blit=True,repeat=True)
plt.show()
