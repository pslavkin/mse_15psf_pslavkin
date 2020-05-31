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
signalFrec      = 0.4
firData,        = np.load("4_clase/low_pass.npy").astype(float)
firData         = np.insert(firData,0,firData[-1])
M               = len(firData)
firExtendedData = np.concatenate((firData,np.zeros(N-1)))
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


fftData=np.fft.fft(xData)
circularfftData=np.concatenate((fftData[len(fftData)//2+impar:],fftData[0:len(fftData)//2+impar]))
segmentFftAxe  = fig.add_subplot(4,2,3)
segmentFftLn,  = plt.plot([],[],'r-o',label="segment FFT")
segmentFftAxe.legend()
segmentFftAxe.grid(True)
segmentFftAxe.set_xlim(-fs/2,fs/2)
segmentFftAxe.set_ylim(np.min(np.abs(fftData)),50)#np.max(fftData))

HData=np.fft.fft(firExtendedData)
circularHData=np.concatenate((HData[len(HData)//2+impar:],HData[0:len(HData)//2+impar]))
HAxe  = fig.add_subplot(4,2,5)
HLn,  = plt.plot(fData,np.abs(circularHData),'b-o',label="H")
HAxe.legend()
HAxe.grid(True)
HAxe.set_xlim(-fs/2,fs/2)
HAxe.set_ylim(np.min(np.abs(HData)),np.max(np.abs(HData)))



YAxe  = fig.add_subplot(4,2,4)
YLn,  = plt.plot([],[],'b-o',label="segment Y")
YAxe.legend()
YAxe.grid(True)
YAxe.set_xlim(-fs/2,fs/2)
YAxe.set_ylim(np.min(np.abs(fftData)),50)#np.max(fftData))

ifftAxe  = fig.add_subplot(4,2,6)
ifftLn,  = plt.plot([],[],'b-o',label="segment ifft")
ifftAxe.legend()
ifftAxe.grid(True)
ifftAxe.set_xlim(0,(N+M-1)/fs)
ifftAxe.set_ylim(np.min(xData),np.max(xData))

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
    return YLn,realtimeConvLn,convSignalZoneLn,segmentFftLn,ifftLn


def update(i):
    global yData,b,realtimeConv,segment
    segment=i

    segmentData[:N]=x(signalFrec,tData[segment*N:(segment+1)*N])

    segmentFftData=np.fft.fft(segmentData)
    circularSegmentFftData=np.concatenate((segmentFftData[len(segmentFftData)//2+impar:],segmentFftData[0:len(segmentFftData)//2+impar]))
    segmentFftLn.set_data(fData,np.abs(circularSegmentFftData))

    YData=segmentFftData*HData
    YLn.set_data(fData,np.abs(circularSegmentFftData*circularHData))

    ifftData=np.fft.ifft(YData)
    ifftLn.set_data(tSegmentData,np.real(ifftData))

    realtimeConv[segment*N:segment*N+N+M-1]+=np.real(ifftData)
    realtimeConvLn.set_data(tData,realtimeConv)

    convSignalZoneLn = signalAxe.fill_between([tData[segment*N],tData[(segment+1)*N-1]],10,-10,facecolor="yellow",alpha=0.5)
    return YLn,realtimeConvLn,convSignalZoneLn,segmentFftLn,ifftLn

ani=FuncAnimation(fig,update,k,init,interval=2000 ,blit=True,repeat=False)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
