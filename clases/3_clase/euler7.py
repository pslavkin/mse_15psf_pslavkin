import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 100
N          = 100
#--------------------------------------
#conejo=np.load("conejo.npy")[::10]
#N=len(conejo)
#signal=lambda f,n: conejo[n]
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,promLn  = plt.plot([],[],'r-',[],[],'bo')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleFrec = 0
circleLn.set_label(circleFrec)
circleLg   = circleAxe.legend()
circleData = []
prom       = 0
frecIter   = 0
circle     = lambda c,f,n: c*np.exp(-1j*2*np.pi*f*n*1/fs)
circleInv  = lambda c,f,n: c*np.exp(1j*2*np.pi*f*n*1/fs)
#--------------------------------------
signalAxe  = fig.add_subplot(2,2,2)
signalLn,  = plt.plot([],[],'b-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalFrec = 2
signalData=[]
signal  = lambda f,n: 0.5*np.sin(2*np.pi*f*n*1/fs)+0.1j*np.cos(2*np.pi*f*n*1/fs)
#--------------------------------------
fourierAxe  = fig.add_subplot(2,2,3)
fourierLn,  = plt.plot([],[],'g-o')
fourierAxe.grid(True)
fourierAxe.set_xlim(0,fs)
fourierAxe.set_ylim(0,0.5)
fourierData=[]
#--------------------------------------
inversaAxe         = fig.add_subplot(2,2,4)
inversaLn,vectorLn = plt.plot([],[],'y-o',[],[],'k-')
inversaAxe.grid(True)
inversaAxe.set_xlim(-1,1)
inversaAxe.set_ylim(-1,1)
inversaData = []
vectorData  = []
penData  = []
#--------------------------------------
tData=[]
fData=[]

time=np.arange(0,N,1)
frec=np.arange(0,fs,fs/N)
fftData=np.fft.fft(signal(signalFrec,time))/N

def updateF(n):
    global fftData,vectorData,penData,fourierData
    if aniT.repeat==True:
        return inversaLn,vectorLn
    vectorData=[0]
    for f in range(N):
        vectorData.append(vectorData[-1]+circleInv(fourierData[f],f*fs/N,n))
    inversaLn.set_data(np.real(vectorData),np.imag(vectorData))
    penData.append(vectorData[-1])
    vectorLn.set_data(np.real(penData),np.imag(penData))
    return inversaLn,vectorLn


def init():
    return circleLn,

def updateT(nn):
    global circleData,signalData,tData,promData,frecIter,circleFrec,fourierData,fData,fftData,circleLg
    for n in range(N):
        circleData.append(circle(1,circleFrec,n)*signal(signalFrec,n))
        prom=np.average(circleData)
        signalData.append(signal(signalFrec,n))
        tData.append(n/fs)
    signalLn.set_data(tData,np.real(signalData))
    promLn.set_data(np.real(prom),
                    np.imag(prom))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))

    circleData = []
    signalData = []
    tData      = []
    fourierData.append(prom)
    fData.append(circleFrec)

#    fourierLn.set_data(frec,np.abs(fftData)**2)
    fourierLn.set_data(fData,np.abs(fourierData)**2)
    prom       = 0
    frecIter+=1
    if frecIter == N:
        aniT.repeat=False
    else:
        circleFrec = frecIter*fs/N
        circleLn.set_label(circleFrec)
        circleLg=circleAxe.legend()
    return circleLn,signalLn,promLn,fourierLn,circleLg,

aniT=FuncAnimation(fig,updateT,N,init,interval=100 ,blit=True,repeat=True)
aniF=FuncAnimation(fig,updateF,N,init,interval=200 ,blit=True,repeat=True)
plt.show()
