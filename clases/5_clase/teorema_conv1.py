import numpy as np
import scipy.signal as sci
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig        = plt.figure()
fs         = 100
N          = 100
#-----------DELTA----------------------
delta=np.zeros(100)
delta[10] =10
delta[9]  =0
N=len(delta)
def signal(f,n):
    return delta[n]
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,massLn,  = plt.plot([],[],'r-',[],[],'bo')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleFrec = np.arange(-fs/2,fs/2,fs/N)
circleLn.set_label(circleFrec[0])
circleLg=circleAxe.legend()
circleData = []
mass       = 0
frecIter   = 0
def circle(f,n):
    return np.exp(-1j*2*np.pi*f*n*1/fs)
def circleInv(f,n,c):
    return c*np.exp(-1j*2*np.pi*f*n*1/fs)
#--------------------------------------
signalAxe  = fig.add_subplot(2,2,2)
signalRLn,signalILn  = plt.plot([],[],'b-',[],[],'r-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)

signalAxe.set_ylim(-1,1)
signalAxe.set_ylim(-1,1)
signalFrec = 2
signalData=[]
#def signal(f,n):
#    return np.sin(2*np.pi*f*n*1/fs)#+0.4*np.sin(2*np.pi*f*n*1/fs)
#--------------------------------------
promAxe  = fig.add_subplot(2,2,3)
promRLn,promILn,promAbsLn,  = plt.plot([],[],'b-o',[],[],'r-o',[],[],'y-')
promAxe.grid(True)
promAxe.set_xlim(-fs/2,fs/2)
promAxe.set_ylim(-2,2)
promData=np.zeros(N,dtype=complex)
#--------------------------------------
inversaAxe         = fig.add_subplot(2,2,4)
inversaLn,penLn,penRLn,penILn = plt.plot([],[],'m-o',[],[],'k-',[],[],'b-',[],[],'r-')
inversaAxe.grid(True)
inversaAxe.set_xlim(-1,1)
inversaAxe.set_ylim(-1,1)
inversaData,penData= [],[]
harmonics=N//2
#--------------------------------------
tData=np.arange(0,N/fs,1/fs)

def init():
    return circleLn,circleLg,signalRLn,signalILn,massLn,promRLn,promILn,inversaLn,penILn,penRLn,

def updateF(n):
    global promData,fData,frecIter,penData,aniF,harmonics
    if aniT.repeat==True:
        return inversaLn,
    inversaData=[0]
    harmonicRange=range(N//2-harmonics,N//2+harmonics,1)
    for f in harmonicRange:
        inversaData.append(inversaData[-1]+circleInv(circleFrec[f],frecIter,promData[f]))
    inversaLn.set_data(np.imag(inversaData),np.real(inversaData))
    penData.insert(0,inversaData[-1])
    penData=penData[0:N]
    t=np.linspace(0,1,len(penData))
    penRLn.set_data(t,np.real(penData))
    penILn.set_data(np.imag(penData),t)
    penLn.set_data(np.imag(penData),np.real(penData))
    promHarmomicLn = promAxe.fill_between([circleFrec[harmonicRange[0]],circleFrec[harmonicRange[-1]]],1,-1,facecolor="green",alpha=0.1)
    frecIter+=1
    if frecIter==N:
        frecIter=0
        #harmonics+=1
        #if harmonics>=N//2:
        #    harmonics=1
    return inversaLn,penLn,penILn,penRLn,signalRLn,signalILn,promRLn,promILn,promHarmomicLn


def updateT(nn):
    global circleData,signalData,promData,frecIter,circleFrec,circleLg,aniF

    circleData = []
    signalData = []
    for n in range(N):
        circleData.append(circle(circleFrec[frecIter],n)*signal(signalFrec,n))
        mass=np.average(circleData)
        signalData.append(signal(signalFrec,n))
        promData[frecIter]=mass
    massLn.set_data(np.real(mass),
                    np.imag(mass))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalRLn.set_data(tData[:n+1],np.real(signalData))
    signalILn.set_data(tData[:n+1],np.imag(signalData))
    promRLn.set_data(circleFrec[:frecIter+1],np.real(promData[:frecIter+1]))
    promILn.set_data(circleFrec[:frecIter+1],np.imag(promData[:frecIter+1]))
   # promILn.set_data(np.real(promData[frecIter]),np.imag(promData[frecIter]))
    promAbsLn.set_data(circleFrec[:frecIter+1],np.abs(promData[:frecIter+1]))
    circleLn.set_label(circleFrec[frecIter])
    circleLg=circleAxe.legend()

    if frecIter == N-1:
        frecIter=0
        aniT.repeat=False
    else:
        frecIter+=1
    return circleLn,circleLg,signalRLn,signalILn,massLn,promRLn,promILn,promAbsLn

aniT=FuncAnimation(fig,updateT,N,init,interval=10 ,blit=True,repeat=True)
aniF=FuncAnimation(fig,updateF,N,init,interval=20 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,aniT,aniF)
plt.show()
