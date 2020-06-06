import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 100
N          = 100
#--------------------------------------
signalAxe  = fig.add_subplot(3,1,1)
signalLn,  = plt.plot([],[],'b-o')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalFrec = 103
signalData=[]

signal2Axe  = fig.add_subplot(3,1,2)
signal2Ln,  = plt.plot([],[],'r-o')
signal2Axe.grid(True)
signal2Axe.set_xlim(0,N/fs)
signal2Axe.set_ylim(-1,1)
signal2Frec = 55
signal2Data=[]


#--------------------------------------
def signal(f,n):
#    return np.sin(2*np.pi*f*n*1/fs)
    return sc.sawtooth(2*np.pi*f*n*1/fs,0.5)
#--------------------------------------
tData=np.arange(0,N/fs,1/fs)
fData=np.arange(0,fs,1)


fftData=np.abs(np.fft.fft(2*signal(signalFrec,fData)))+ \
        np.abs(np.fft.fft(signal(signal2Frec,fData)))

fftAxe  = fig.add_subplot(3,1,3)
fftLn,  = plt.plot(fData,fftData,'r-o')
fftAxe.grid(True)
fftAxe.set_xlim(0,fs)
#--------------------------------------

def init():
    global signalData,signal2Data
    signalData = []
    signal2Data = []
    return signalLn,signal2Ln
def update(n):
    global signalData,signal2Data
    signalData.append(2*signal(signalFrec,n))
    signalLn.set_data(tData[:n+1],signalData)

    signal2Data.append(signal(signal2Frec,n))
    signal2Ln.set_data(tData[:n+1],signal2Data)
    return signalLn,signal2Ln


ani=FuncAnimation(fig,update,N,init,interval=10 ,blit=True,repeat=False)
plt.get_current_fig_manager().window.showMaximized()
plt.show()
