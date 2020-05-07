import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig  = plt.figure()
fs   = 20
N    = 40
#--------------------------------------
#conejo=np.array([0,0,0.25+0.25j,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.25-0.25j,0])
conejo=np.load("conejo.npy")[::2]
N=len(conejo)
signal=lambda f,n: conejo[n]
#--------------------------------------
circleAxe  = fig.add_subplot(2,2,1)
circleLn,promLn  = plt.plot([],[],'r-',[],[],'bo')
circleAxe.grid(True)
circleAxe.set_xlim(-2,2)
circleAxe.set_ylim(-2,2)
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
signalRealLn,signalImagLn  = plt.plot([],[],'b-',[],[],'r-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalFrec = 1
signalData=[]
#signal  = lambda f,n: 1*np.cos(2*np.pi*f*n*1/fs)#+0.5j*np.cos(2*np.pi*f*4*n*1/fs)
#--------------------------------------
fourierAxe  = fig.add_subplot(2,2,3)
fourierLn,  = plt.plot([],[],'g-o')
fourierAxe.grid(True)
fourierAxe.set_xlim(0,fs)
fourierAxe.set_ylim(0,0.5)
fourierData=[]
#--------------------------------------
inversaAxe         = fig.add_subplot(2,2,4)
inversaLn,vectorLn,slideRealLn,slideImagLn = plt.plot([],[],'y-o',[],[],'k-',[],[],'b-',[],[],'r-')
inversaAxe.grid(True)
inversaAxe.set_xlim(-1,1)
inversaAxe.set_ylim(-1,1)
inversaData = []
vectorData  = []
penData     = []
slideData   = []
#--------------------------------------
tData=[]
fData=[]

time = np.arange(0,N,1/fs)
#frec=np.arange(0,fs,fs/N)
#fftData=np.fft.fft(signal(signalFrec,time))/N

def init():
    return inversaLn,

def updateF(n):
    global fftData,vectorData,penData,fourierData
    if aniT.repeat==True or len(slideData)==N:
        return inversaLn,vectorLn,slideRealLn,slideImagLn
    vectorData=[0]
    for f in range(N):
        vectorData.append(vectorData[-1]+circleInv(fourierData[f],f*fs/N,n))
    inversaLn.set_data(np.imag(vectorData),np.real(vectorData))
    penData.append(vectorData[-1])
    slideData.insert(0,vectorData[-1])
    vectorLn.set_data(np.real(penData),np.imag(penData))
    slideRealLn.set_data(time[:len(slideData)],np.real(slideData))
    slideImagLn.set_data(np.imag(slideData),time[:len(slideData)])
    return inversaLn,vectorLn,slideRealLn,slideImagLn


def updateT(n):
    global circleData,signalData,tData,promData,frecIter,circleFrec,fourierData,fData
    circleData.append(circle(1,circleFrec,n)*(signal(signalFrec,n)))
    prom=np.average(circleData)
    promLn.set_data(np.real(prom),
                    np.imag(prom))
    circleLn.set_data(np.real(circleData),
                      np.imag(circleData))
    signalData.append(signal(signalFrec,n))
    tData.append(n/fs)
    signalRealLn.set_data(tData,np.real(signalData))
    signalImagLn.set_data(tData,np.imag(signalData))

    if n==N-1:
        circleData = []
        signalData = []
        tData      = []
        fourierData.append(prom)
        fData.append(circleFrec)
        fourierLn.set_data(fData,np.real(fourierData))
        prom       = 0
        frecIter+=1
        if frecIter == N:
            aniT.repeat=False
#            fourierData=np.array([0,0,0.25+0j,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.25-0j,0])
        circleFrec = frecIter*fs/N
    circleLn.set_label(circleFrec)
    circleLg=circleAxe.legend()
    return circleLn,signalImagLn,signalRealLn,promLn,fourierLn,circleLg

aniT=FuncAnimation(fig,updateT,N,init, interval=10 ,blit=True,repeat=True)
aniF=FuncAnimation(fig,updateF,N,init, interval=200 ,blit=True,repeat=True)
plt.show()
