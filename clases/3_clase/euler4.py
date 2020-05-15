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
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleFrec = np.arange(-fs/2,fs/2,fs/N)
circleLn.set_label(circleFrec[0])
circleLg   = circleAxe.legend()
circleData = []
mass       = 0
frecIter   = 0
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
    return np.sin(2*np.pi*f*n*1/fs)
#--------------------------------------
promAxe  = fig.add_subplot(2,2,3)
promRLn,promILn,  = plt.plot([],[],'g-o',[],[],'y-o')
promAxe.grid(True)
promAxe.set_xlim(-fs/2,fs/2)
promAxe.set_ylim(-1,1)
promData=np.zeros(N,dtype=complex)
#--------------------------------------
tData=np.arange(0,N/fs,1/fs)

def init():
    return circleLn,circleLg,signalLn,massLn,promRLn,promILn
def update(n):
    global circleData,signalData,promData,frecIter,circleFrec,circleLg
    circleData.append(circle(circleFrec[frecIter],n)*signal(signalFrec,n))
    mass=np.average(circleData)
    massLn.set_data(np.real(mass),
                    np.imag(mass))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    signalLn.set_data(tData[:n+1],signalData)
    promData[frecIter]=mass
    promRLn.set_data(circleFrec[:frecIter+1],np.real(promData[:frecIter+1]))
    promILn.set_data(circleFrec[:frecIter+1],np.imag(promData[:frecIter+1]))

    if n==N-1:
        circleData = []
        signalData = []
        circleLn.set_label(circleFrec[frecIter])
        circleLg=circleAxe.legend()
        if frecIter == N-1:
            ani.repeat=False
        else:
            frecIter+=1
    return circleLn,circleLg,signalLn,massLn,promRLn,promILn,

ani=FuncAnimation(fig,update,N,init,interval=100 ,blit=True,repeat=True)
plt.show()
