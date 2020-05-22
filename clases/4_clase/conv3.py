import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 6
N   = 6
fir,=np.load("4_clase/low_pass_short.npy").astype(float)
fir=np.insert(fir,0,fir[-1]) #ojo que pydfa me guarda 1 dato menos...
#fir=(fir[:]/max(fir))
M=len(fir)
#--------------------------------------
def x(f,n):
    return 1*sc.sawtooth(2*np.pi*n/fs,0.5)

tData=np.arange(0,N+M-1,1)
#xData=np.zeros(N+2*(M-1))
#xData[M-1:M-1+N]=x(0,tData[M-1:M-1+N])
xData=x(0,tData[0:N])
xLnArray=[]

#para dibujar signal vs h solos
xAxe  = fig.add_subplot(1,2,1)
xLn,  = plt.plot(tData[0:N],xData,'g-o')
xAxe.grid(True)
hAxe  = fig.add_subplot(1,2,2)
hLn,  = plt.plot(tData[0:M],fir,'r-o')
hAxe.grid(True)

#for i in range(N):
#    xAxe  = fig.add_subplot(6,3,3*i+1)
#    xLn,xHighLn,  = plt.plot(tData[0:N],xData,'r-',tData[i],xData[i],'yo')
#    xLnArray.append(xLn)
#    xAxe.grid(True)
#    xAxe.set_xlim(0,N-1)
#    xAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
##--------------------------------------
#hData=fir
#yData=np.zeros(N+M-1)
#hLn=[]
#yLn=[]
#for i in range(N):
#    hAxe  = fig.add_subplot(6,3,3*i+2)
#    Ln,  = plt.plot([],[],'b-o')
#    #Ln,  = plt.plot(tData[i:M+i],hData*xData[i],'r-o')
#    hLn.append(Ln)
#    hAxe.grid(True)
#    hAxe.set_xlim(0,N+M-2)
#    hAxe.set_ylim(np.min(hData*xData[i])-0.1,np.max(hData*xData[i])+0.1)
##--------------------------------------
#    yAxe  = fig.add_subplot(6,3,3*i+3)
#    yData[i:i+M]+=hData*xData[i]
#    Ln,  = plt.plot([],[],'b-o')
#    #Ln,  = plt.plot(tData[0:N+M-1],yData,'b-o')
#    yLn.append(Ln)
#    yAxe.grid(True)
#    yAxe.set_xlim(0,N+M-2)
#    yAxe.set_ylim(np.min(yData)-0.01,np.max(yData)+0.01)
##--------------------------------------
#yData=np.zeros(N+M-1)
#def init():
#    return yLn,hLn
#
#def update(i):
#    hLn[i].set_data(tData[i:M+i],hData*xData[i])
#    yData[i:i+M]+=hData*xData[i]
#    yLn[i].set_data(tData[0:N+M-1],yData)
#    ani.event_source.stop()
#    return yLn,hLn
#
#ani=FuncAnimation(fig,update,N,init,interval=50 ,blit=False,repeat=False)
#plt.get_current_fig_manager().window.showMaximized()
#b=buttonOnFigure(fig,ani)
plt.show()
