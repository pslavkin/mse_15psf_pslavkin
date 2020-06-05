import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig             = plt.figure()
fs              = 80
N               = 80
signalFrec      = 20
impar           = (N%2)
#--------------------------------------
def x(f,n):
    return 0.1*np.sin(2*np.pi*f*n)+0.5*np.random.normal(0,size=len(n))

k=100
tData=np.linspace(0,(k*N)/fs,k*N,endpoint=False)
xData=x(signalFrec,tData[:k*N])
segment=0
#--------------------------------------
signalAxe  = fig.add_subplot(3,1,1)
signalLn,  = plt.plot(tData[:k*N],xData,'b-',label="signal")
signalAxe.legend()
signalAxe.grid(True)
signalAxe.set_xlim(0,(k*N-1)/fs)
signalAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
convSignalZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)

tSegmentData=np.linspace(0,N/fs,N,endpoint=False)
fData=np.concatenate((np.linspace(-fs/2,0,N//2,endpoint=False),\
       np.linspace(0,fs/2,N//2+impar,endpoint=False)))
segmentData=np.zeros(N)

fftData=np.fft.fft(xData)

segmentYAxe  = fig.add_subplot(3,1,2)
segmentYLn, = plt.plot([],[],'r-',label="segment Y")
segmentYAxe.legend()
segmentYAxe.grid(True)
segmentYAxe.set_xlim(-fs/2,fs/2)
segmentYAxe.set_ylim(np.min(np.abs(fftData)),np.max(np.abs(fftData))/(0.5*k))

YAxe  = fig.add_subplot(3,1,3)
YLn, = plt.plot([],[],'b-o',label="average Y")
YAxe.legend()
YAxe.grid(True)
YAxe.set_xlim(-fs/2,fs/2)
YAxe.set_ylim(np.min(np.abs(fftData))/k+3,np.max(np.abs(fftData))/k+4)
lastSegmentFftData=np.zeros(N)

#--------------------------------------
def init():
    global yData
#    realtimeConv=np.zeros(N+M-1)
    return YLn,convSignalZoneLn,segmentYLn


def update(i):
    global yData,segment,lastSegmentFftData
    segment=i

    segmentData[:N]=x(signalFrec,tData[segment*N:(segment+1)*N])
    segmentFftData=np.abs(np.fft.fft(segmentData))
    lastSegmentFftData+=segmentFftData

    circularLastSegmentFftData=np.concatenate((lastSegmentFftData[len(lastSegmentFftData)//2+impar:],lastSegmentFftData[0:len(lastSegmentFftData)//2+impar]))

    YLn.set_data(fData,circularLastSegmentFftData/i)

    circularSegmentFftData=np.concatenate((segmentFftData[len(segmentFftData)//2+impar:],segmentFftData[0:len(segmentFftData)//2+impar]))
    segmentYLn.set_data(fData,circularSegmentFftData)


    convSignalZoneLn = signalAxe.fill_between([tData[segment*N],tData[(segment+1)*N-1]],10,-10,facecolor="yellow",alpha=0.5)
    return YLn,convSignalZoneLn,segmentYLn

ani=FuncAnimation(fig,update,k,init,interval=500 ,blit=True,repeat=False)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
