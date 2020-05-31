import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig             = plt.figure()
fs              = 20
N               = 80
signalFrec      = .4
firData,        = np.load("4_clase/low_pass.npy").astype(float)
firData         = np.insert(firData,0,firData[-1])
M               = len(firData)
impar           = ((N+M-1)%2)
#--------------------------------------
def x(f,n):
    return np.sin(2*np.pi*f*n)+np.sin(2*np.pi*5*n)

k=10
tData=np.linspace(0,(k*N+M-1)/fs,k*N+M-1,endpoint=False)
xData=x(signalFrec,tData[:k*N])
segment=0
#--------------------------------------
signalAxe  = fig.add_subplot(4,1,1)
signalLn,  = plt.plot(tData[:k*N],xData,'b-o',label="signal")
signalAxe.legend()
signalAxe.grid(True)
signalAxe.set_xlim(0,(k*N-1)/fs)
signalAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
convSignalZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)

tSegmentData=np.linspace(0,(N+M-1)/fs,N+M-1,endpoint=False)
fData=np.concatenate((np.linspace(-fs/2,0,(N+M-1)//2,endpoint=False),\
       np.linspace(0,fs/2,(N+M-1)//2+impar,endpoint=False)))
segmentData=np.zeros(N+M-1)

segmentAxe  = fig.add_subplot(4,1,2)
segmentLn,  = plt.plot([],[],'b-o',label="segment")
segmentAxe.legend()
segmentAxe.grid(True)
segmentAxe.set_xlim(0,(N+M-2)/fs)
segmentAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
convSegmentZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)

firAxe  = fig.add_subplot(4,1,3)
firLn,  = plt.plot([],[],'b-o',label="fir")
firAxe.legend()
firAxe.grid(True)
firAxe.set_xlim(0,(N+M-2)/fs)
firAxe.set_ylim(np.min(firData),np.max(firData))

convAxe         = fig.add_subplot(4,1,4)
convolveData    = np.convolve(xData,firData)
convLn,         = plt.plot(tData,convolveData,'b-',label = "conv")
realtimeConvLn, = plt.plot([],[],'g-o')
convAxe.legend()
convAxe.grid(True)
convAxe.set_xlim(0,(k*N+M-2)/fs)
#--------------------------------------
realtimeConv=np.zeros(k*N+M-1)
def init():
    global yData,realtimeConv
#    realtimeConv=np.zeros(N+M-1)
    convZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.51)
    return firLn,realtimeConvLn,convSegmentZoneLn,convSignalZoneLn

def update(i):
    global yData,b,realtimeConv,segment

    segmentData[:N]=x(signalFrec,tData[segment*N:(segment+1)*N])
    segmentLn.set_data(tSegmentData,segmentData)

    tSegmentDataNegative=np.linspace((-M+1)/fs,(N+M-1)/fs,N+2*(M-1),endpoint=False)
    segmentDataNegative=np.concatenate((np.zeros(M-1),segmentData))
    firLn.set_data(tSegmentDataNegative[i:i+M],firData[::-1])
    realtimeConv[segment*N+i]+=np.sum(segmentDataNegative[i:i+M]*firData[::-1])
    realtimeConvLn.set_data(tData,realtimeConv)
    convZoneLn = signalAxe.fill_between([tSegmentDataNegative[i],tSegmentDataNegative[i+M-1]],10,-10,facecolor="yellow",alpha=0.51)
    convSignalZoneLn = signalAxe.fill_between([tData[segment*N],tData[(segment+1)*N-1]],10,-10,facecolor="yellow",alpha=0.5)
    if i==N+M-2:
        if segment<(k-1):
            segment+=1
        else:
            ani.event_source.stop()
    return firLn,realtimeConvLn,convSegmentZoneLn,convSignalZoneLn,segmentLn

ani=FuncAnimation(fig,update,N+M-1,init,interval=10 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
