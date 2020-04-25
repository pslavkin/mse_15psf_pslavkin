import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 200
N          = 200
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,promLn  = plt.plot([],[],'r-',[],[],'bo')
circleAxe.grid(True)
circleAxe.set_xlim(-2,2)
circleAxe.set_ylim(-2,2)
circleFrec = 0
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
signal  = lambda f,n: 0.5*np.sin(2*np.pi*f*n*1/fs)+0.5j*np.sin(2*np.pi*f*2*n*1/fs)
#--------------------------------------
conejo=np.load("conejo.npy")
N=len(conejo)
signal=lambda f,n: conejo[n]
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
#    if aniT.repeat==True:
#        return 
    vectorData=[0]
    for f in range(N):
        vectorData.append(vectorData[-1]+circleInv(fftData[f],f*fs/N,n))
    inversaLn.set_data(np.real(vectorData),np.imag(vectorData))
    penData.append(vectorData[-1])
    vectorLn.set_data(np.real(penData),np.imag(penData))
    return inversaLn,vectorLn


def updateT(n):
    global circleData,signalData,tData,promData,frecIter,circleFrec,fourierData,fData
    circleData.append(circle(1,circleFrec,n)*signal(signalFrec,n))
    prom=np.average(circleData)
    promLn.set_data(np.real(prom),
                    np.imag(prom))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    tData.append(n/fs)
    signalLn.set_data(tData,np.real(signalData))

    if n==N-1:
        circleData = []
        signalData = []
        tData      = []
        fourierData.append(prom)
        fData.append(circleFrec)
        fourierLn.set_data(fData,np.abs(fourierData)**2)
        prom       = 0
        frecIter+=1
        if frecIter == N:
            aniT.repeat=False
        circleFrec = frecIter*fs/N
        circleLn.set_label(circleFrec)
        circleAxe.legend()
    return circleLn,circleAxe,signalLn,promLn,fourierLn

aniT=FuncAnimation(fig,updateT,N,interval=10 ,blit=False,repeat=True)
aniF=FuncAnimation(fig,updateF,N,interval=200 ,blit=False,repeat=True)
plt.show()
