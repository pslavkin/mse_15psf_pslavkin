import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 20
N          = 20
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,massLn  = plt.plot([],[],'r-',[],[],'bo')
circleAxe.grid(True)
circleAxe.set_xlim(-2,2)
circleAxe.set_ylim(-2,2)
circleFrec = 3
circleLn.set_label(0)
circleLg   = circleAxe.legend()
circleData = []
mass       = 0
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
    return circleLn,circleLg,signalLn,massLn
def update(n):
    global circleData,signalData
    circleData.append(circle(circleFrec,n)*signal(signalFrec,n))
    mass=np.average(circleData)
    massLn.set_data(np.real(mass),
                    np.imag(mass))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    signalLn.set_data(tData[:n+1],signalData)

    if n==N-1:
        circleData = []
        signalData = []
    circleLn.set_label(n)
    circleLg=circleAxe.legend()
    return circleLn,circleLg,signalLn,massLn

ani=FuncAnimation(fig,update,N,init,interval=100 ,blit=True,repeat=True)
plt.show()
