import numpy as np
import scipy.signal as sci
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 20
N          = 20
#-----------CUADRADA----------------------
#def signal(f,n):
#    return 0.5*sci.square(f*(n/fs)*(2*np.pi),0.5)
#-----------TRIANGULAR----------------------
#def signal(f,n):
#    return sci.sawtooth(f*(n/fs)*(2*np.pi),0.5)
#-----------DELTA----------------------
#delta=np.zeros(100)
#delta[49]=1
#N=len(delta)
#def signal(f,n):
#    return delta[n]
#-----------CONJUGADO----------------------
#conjugado=np.zeros(100,dtype=complex)
#conjugado[2]=50j
#conjugado[100-2]=-50j
#N=len(conjugado)
#def signal(f,n):
#    return conjugado[n]
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
signalFrec = 2
signalData=[]
def signal(f,n):
    return np.cos(2*np.pi*f*n*1/fs)#+0.4j*np.sin(2*np.pi*f*n*1/fs)
#--------------------------------------
promAxe  = fig.add_subplot(2,2,3)
promRLn,promILn,promAbsLn  = plt.plot([],[],'b-o',[],[],'r-o',[],[],'y-')
promAxe.grid(True)
promAxe.set_xlim(-fs/2,fs/2)
promAxe.set_ylim(-1,1)
promData=np.zeros(N,dtype=complex)
#--------------------------------------
inversaAxe         = fig.add_subplot(2,2,4)
inversaLn,penLn,penRLn,penILn = plt.plot([],[],'m-o',[],[],'k-',[],[],'b-',[],[],'r-')
inversaAxe.grid(True)
inversaAxe.set_xlim(-1,1)
inversaAxe.set_ylim(-1,1)
inversaData,penData= [],[]
#--------------------------------------
tData=np.arange(0,N/fs,1/fs)

def init():
    return circleLn,circleLg,signalRLn,signalILn,massLn,promRLn,promILn,inversaLn,penILn,penRLn,

def updateF(n):
    global promData,fData,vectorData,frecIter,penData
    if aniT.repeat==True:
        return inversaLn,
    vectorData=[0]
    for f in range(N):
        vectorData.append(vectorData[-1]+circleInv(circleFrec[f],frecIter,promData[f]))
    inversaLn.set_data(np.imag(vectorData),np.real(vectorData))
    penData.insert(0,vectorData[-1])
    traceData=penData[0:N//2]
    t=np.linspace(0,1,len(traceData))
    penRLn.set_data(t,np.real(traceData))
    penILn.set_data(np.imag(traceData),t)
    penLn.set_data(np.imag(penData),np.real(penData))
    frecIter+=1
    if frecIter==N:
        frecIter=0
    return inversaLn,penLn,penILn,penRLn,promRLn,promILn,promAbsLn
def updateT(nn):
    global circleData,signalData,promData,frecIter,circleFrec,circleLg

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
    promAbsLn.set_data(circleFrec[:frecIter+1],np.abs(promData[:frecIter+1]))
    circleLn.set_label(circleFrec[frecIter])
    circleLg=circleAxe.legend()

    if frecIter == N-1:
        aniT.repeat=False
    else:
        frecIter+=1
    return circleLn,circleLg,signalRLn,signalILn,massLn,promRLn,promILn,promAbsLn

aniT=FuncAnimation(fig,updateT,N,init,interval=10  ,blit=True,repeat=True)
aniF=FuncAnimation(fig,updateF,N,init,interval=30 ,blit=True,repeat=True)
plt.show()
