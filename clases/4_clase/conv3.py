import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig = plt.figure()
fs  = 6
N   = 6
fir,=np.load("low_pass_short.npy").astype(float)
fir=np.insert(fir,0,fir[-1]) #ojo que pydfa me guarda 1 dato menos...
M=len(fir)
#--------------------------------------
def x(f,n):
    return 1+sc.sawtooth(2*np.pi*n/fs,0.5)

tData=np.arange(0,N+M-1,1)
#xData=np.zeros(N+2*(M-1))
#xData[M-1:M-1+N]=x(0,tData[M-1:M-1+N])
xData=x(0,tData[0:N])
xLnArray=[]

for i in range(N):
    xAxe  = fig.add_subplot(6,3,3*i+1)
    xLn,xHighLn,  = plt.plot(tData[0:N],xData,'r-',tData[i],xData[i],'yo')
    xLnArray.append(xLn)
    xAxe.grid(True)
    xAxe.set_xlim(0,N-1)
    xAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
#--------------------------------------
hData=fir
for i in range(N):
    hAxe  = fig.add_subplot(6,3,3*i+2)
    hLn,  = plt.plot(tData[i:M+i],hData*xData[i],'r-o')
    hAxe.grid(True)
    hAxe.set_xlim(0,N+M-2)
    hAxe.set_ylim(np.min(hData*xData[i])-0.1,np.max(hData*xData[i])+0.1)
#--------------------------------------
yData=np.zeros(N+M-1)
for i in range(N):
    yAxe  = fig.add_subplot(6,3,3*i+3)
    yData[i:i+M]+=hData*xData[i]
    yLn,  = plt.plot(tData[0:N+M-1],yData,'b-o')
    yAxe.grid(True)
    yAxe.set_xlim(0,N+M-2)
    yAxe.set_ylim(np.min(yData)-0.01,np.max(yData)+0.01)
#--------------------------------------
def init():
    return yLn,

def update(i):
    return yLn,

ani=FuncAnimation(fig,update,M+N-1,init,interval=500 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
plt.show()
