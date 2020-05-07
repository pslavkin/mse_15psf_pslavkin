import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 50
N          = 50
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,  = plt.plot([],[],'r-')
circleAxe.grid(True)
circleAxe.set_xlim(-2,2)
circleAxe.set_ylim(-2,2)
circleLn.set_label(0)
legendLn   = circleAxe.legend()
circleFrec = 1
circleData = []
circle     = lambda c,f,n: c*np.exp(-1j*2*np.pi*f*n*1/fs)
#--------------------------------------
signalAxe  = fig.add_subplot(2,2,2)
signalLn,  = plt.plot([],[],'b-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalFrec = 2
signalData=[]
signal  = lambda f,n: np.cos(2*np.pi*f*n*1/fs)
#--------------------------------------
tData=[]

def init():
    return circleLn,
def update(n):
    global circleData,signalData,tData,legendLn
    circleData.append(circle(1,circleFrec,n))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    tData.append(n/fs)
    signalLn.set_data(tData,signalData)

    if n==N-1:
        circleData=[]
        signalData=[]
        tData=[]
    circleLn.set_label(n)
    legendLn=circleAxe.legend()
    return circleLn,signalLn,legendLn,

ani=FuncAnimation(fig,update,N,init,interval=10 ,blit=True,repeat=True)
plt.show()
