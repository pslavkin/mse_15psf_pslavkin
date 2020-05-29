import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 10
N   = 10
#fir,=np.load("4_clase/low_pass_short.npy").astype(float)
#fir=np.insert(fir,0,fir[-1])
fir=np.zeros(10)
fir[0]=1
fir[1]=0.1
fir[2]=0.2
fir[4]=0.4
M=len(fir)
#--------------------------------------
def x(f,n):
    return 1*sc.sawtooth(2*np.pi*2*n/fs,0.5)
#    return 1*np.sin(2*np.pi*f*n/fs)

tData=np.arange(0,N+M-1,1)
fData=np.arange(0,N+M-1,1)
xData=np.zeros(N+M-1)
xData[:N]+=x(1,tData[:N])


xAxe  = fig.add_subplot(2,3,1)
xLn,xHighLn,  = plt.plot(tData,xData,'r-o',[],[],'yo')
xAxe.grid(True)
xAxe.set_xlim(0,N+M-2)
xAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
#--------------------------------------
hAxe  = fig.add_subplot(2,3,2)
hLn,  = plt.plot([],[],'b-o')
hAxe.grid(True)
hAxe.set_xlim(0,N+M-2)
hAxe.set_ylim(-2,2)
#--------------------------------------
yAxe  = fig.add_subplot(2,3,3)
yLn,yifftLn,yConvLn,  = plt.plot([],[],'b-o',[],[],'r-o',[],[],'g-o')
yAxe.grid(True)
yAxe.set_xlim(0,N+M-2)
yAxe.set_ylim(-2,2)
yData=np.zeros(N+M-1)
#--------------------------------------
HAxe  = fig.add_subplot(2,3,5)
HLn,  = plt.plot([],[],'b-o')
HAxe.grid(True)
HAxe.set_xlim(0,N+M-2)
HAxe.set_ylim(0,30)

XAxe  = fig.add_subplot(2,3,4)
XData = np.fft.fft(xData)
XLn,  = plt.plot(fData,np.abs(XData)**2,'r-o')
XAxe.grid(True)
XAxe.set_xlim(0,N+M-2)
#XAxe.set_ylim(-2,2)

YAxe  = fig.add_subplot(2,3,6)
YLn,YfftLn  = plt.plot([],[],'b-o',[],[],'r-o')
YAxe.grid(True)
YAxe.set_xlim(0,N+M-2)
YAxe.set_ylim(0,200)
YData=np.zeros(N+M-1)

def init():
    return yLn,hLn,xHighLn,HLn,XLn,YLn,

def update(i):
    global yData
    if i<N:
        hData=np.zeros(N+M-1)
        hData[i:i+M]=fir
        xHighLn.set_data(i,xData[i])

        hLn.set_data(tData,hData*xData[i])

        originalHData=np.zeros(N+M-1)
        originalHData[0:M]+=fir
        HData=np.fft.fft(originalHData)
        HLn.set_data(fData,np.abs(HData)**2)

        yData+=hData*xData[i]
        yLn.set_data(tData,yData)
        yConvLn.set_data(tData,np.convolve(xData[:N],fir))

        YData=XData*HData
        YLn.set_data(fData,np.abs(YData)**2)
#
        YfftData=np.fft.fft(yData)
        YfftLn.set_data(fData,np.abs(YfftData)**2)
#
        yifftData=np.fft.ifft(YData)
        yifftLn.set_data(tData,np.real(yifftData))
#        #if i==N-1:
#        #    yData=np.zeros(N+M-1)

    return yLn,hLn,xHighLn,HLn,XLn,YLn,yifftLn,YfftLn,yConvLn

ani=FuncAnimation(fig,update,100*N,init,interval=500 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
