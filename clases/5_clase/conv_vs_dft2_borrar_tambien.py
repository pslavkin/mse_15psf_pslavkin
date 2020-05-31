import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 200
N   = 200
signalFrec = 50
#firData,=np.load("5_clase/hi_pass_short.npy").astype(float)
firData,=np.load("4_clase/low_pass.npy").astype(float)
firData=np.insert(firData,0,firData[-1]) #ojo que pydfa me guarda 1 dato menos...
M=len(firData)
firExtendedData=np.concatenate((firData,np.zeros(N-1)))
impar=((N+M-1)%2)
#--------------------------------------
def x(f,n):
#    return 1*sc.sawtooth(2*np.pi*2*n,0.5)
    return np.sin(2*np.pi*f*n)+np.sin(2*np.pi*f*2*n)

tData=np.linspace(0,(N+M-1)/fs,N+M-1,endpoint=False)
fData=np.concatenate((np.linspace(-fs/2,0,(N+M-1)//2,endpoint=False),\
       np.linspace(0,fs/2,(N+M-1)//2+impar,endpoint=False)))
xData=np.zeros(N+M-1)
xData[:N]+=x(signalFrec,tData[:N])
#--------------------------------------
signalAxe  = fig.add_subplot(3,3,1)
signalLn,  = plt.plot(tData,xData,'b-o')
signalAxe.grid(True)
signalAxe.set_xlim(0,(N+M-2)/fs)
signalAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
convZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)

firAxe  = fig.add_subplot(3,3,4)
firLn,  = plt.plot([],[],'b-o')
firAxe.grid(True)
firAxe.set_xlim(0,(N+M-2)/fs)
firAxe.set_ylim(np.min(firData)-0.2,np.max(firData)+0.2)

convAxe  = fig.add_subplot(3,3,7)
convolveData=np.convolve(xData[0:N],firData)
convLn,yifftLn,realtimeConvLn,  = plt.plot(tData,convolveData,'b-',[],[],'r-o',[],[],'g-o')
convAxe.grid(True)
convAxe.set_xlim(0,(N+M-2)/fs)
#--------------------------------------

xAxe  = fig.add_subplot(3,3,2)
xLn,xHighLn,  = plt.plot(tData,xData,'b-o',[],[],'ko')
xAxe.grid(True)
xAxe.set_xlim(0,(N+M-2)/fs)
xAxe.set_ylim(np.min(xData)*1.1,np.max(xData)*1.1)
xZoneLn = xAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)

hAxe  = fig.add_subplot(3,3,5)
hLn,  = plt.plot([],[],'g-o')
hAxe.grid(True)
hAxe.set_xlim(0,(N+M-2)/fs)
hAxe.set_ylim(np.min(convolveData)-0.1,np.max(convolveData)+0.1)

yAxe  = fig.add_subplot(3,3,8)
yLn,  = plt.plot([],[],'b-o')
yAxe.grid(True)
yAxe.set_xlim(0,(N+M-2)/fs)
yAxe.set_ylim(-0.05,0.05)
yData=np.zeros(N+M-1)
#--------------------------------------
XAxe  = fig.add_subplot(3,3,3)
XData = np.fft.fft(xData)

circularXData=np.concatenate((XData[len(XData)//2+impar:],XData[0:len(XData)//2+impar]))
XLn,  = plt.plot(fData,np.abs(circularXData),'r-o')
XAxe.grid(True)
XAxe.set_xlim(-fs/2,fs/2)

HData=np.fft.fft(firExtendedData)
circularHData=np.concatenate((HData[len(HData)//2+impar:],HData[0:len(XData)//2+impar]))
HAxe  = fig.add_subplot(3,3,6)
HLn,  = plt.plot(fData,np.abs(circularHData),'r-o')
HAxe.grid(True)
HAxe.set_xlim(-fs/2,fs/2)

YAxe  = fig.add_subplot(3,3,9)
YData=XData*HData
circularYData=np.concatenate((YData[len(YData)//2+impar:],YData[0:len(YData)//2+impar]))
YLn,YfftLn  = plt.plot(fData,np.abs(circularYData),'r-o',[],[],'b-o')
YAxe.grid(True)
YAxe.set_xlim(-fs/2,fs/2)

def init():
    global yData,realtimeConv,xZoneLn
    yData=np.zeros(N+M-1)
    realtimeConv=np.zeros(N+M-1)
    convZoneLn = signalAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.51)
    xZoneLn = xAxe.fill_between([0,0],10,-10,facecolor="yellow",alpha=0.5)
    return yLn,xHighLn,hLn,XLn,HLn,YLn,yifftLn,YfftLn,firLn,realtimeConvLn,convZoneLn,xZoneLn

def update(i):
    global yData,b,realtimeConv,xZoneLn
    if i<=N-1:
        xHighLn.set_data(i,xData[i])
        hLn.set_data(tData[i:i+M],firData*xData[i])
        xZoneLn = xAxe.fill_between([tData[i],tData[i+M-1]],10,-10,facecolor="yellow",alpha=0.5)


        hData=np.zeros(N+M-1)
        hData[i:i+M]=firData
        yData+=hData*xData[i]
        yLn.set_data(tData,yData)

        YfftData=np.fft.fft(yData)
        circularYfftData=np.concatenate((YfftData[len(YfftData)//2+impar:],YfftData[0:len(YfftData)//2+impar]))
        YfftLn.set_data(fData,np.abs(circularYfftData))

#        yifftData=np.fft.ifft(YfftData)
#        yifftLn.set_data(tData,np.real(yifftData))

    tDataNegative=np.linspace((-M+1)/fs,(N+M-1)/fs,N+2*(M-1),endpoint=False)
    xDataNegative=np.concatenate((np.zeros(M-1),xData))
    firLn.set_data(tDataNegative[i:i+M],firData[::-1])
    realtimeConv[i]=np.sum(xDataNegative[i:i+M]*firData[::-1])
    realtimeConvLn.set_data(tData,realtimeConv)
    convZoneLn = signalAxe.fill_between([tDataNegative[i],tDataNegative[i+M-1]],10,-10,facecolor="yellow",alpha=0.51)


#    if i==N+M-1:
#        b.pauseFunc(None)

    return yLn,xHighLn,hLn,XLn,HLn,YLn,yifftLn,YfftLn,firLn,realtimeConvLn,convZoneLn,xZoneLn

ani=FuncAnimation(fig,update,N+M-1,init,interval=10 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
