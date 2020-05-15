import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 20
N          = 20
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,  = plt.plot([],[],'r-')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleLn.set_label(0)
circleLg=circleAxe.legend()
circleFrec = 1
circleData = []
def circle(f,n):
    return np.exp(-1j*2*np.pi*f*n*1/fs)
#--------------------------------------
signalAxe  = fig.add_subplot(2,2,2)
signalLn,  = plt.plot([],[],'b-o')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalFrec = 2
signalData=[]
def signal(f,n):
    return np.cos(2*np.pi*f*n*1/fs)
#--------------------------------------
tData=np.arange(0,N/fs,1/fs)

def init():
    return circleLn,circleLg,signalLn,
def update(n):
    global circleData,signalData
    circleData.append(circle(circleFrec,n))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    signalLn.set_data(tData[:n+1],signalData)

    if n==N-1:
        circleData=[]
        signalData=[]
    circleLn.set_label(n)
    circleLg=circleAxe.legend()
    return circleLn,circleLg,signalLn,

ani=FuncAnimation(fig,update,N,init,interval=100 ,blit=True,repeat=True)
plt.show()
