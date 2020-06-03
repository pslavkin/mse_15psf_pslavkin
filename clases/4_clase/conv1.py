import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 6
N   = 6
xFrec = 1

hData,=np.load("4_clase/hi_pass_short.npy").astype(float)
hData=np.insert(hData,0,hData[-1]) #ojo que pydfa me guarda 1 dato menos...
hData[2]=1

M=len(hData)
#--------------------------------------
def x(f,n):
    return 1*sc.sawtooth(2*np.pi*xFrec*n/fs,0.5)

tData            = np.arange(-M+1,N+M-1,1)
xData            = np.zeros(N+2*(M-1))
xData[M-1:N+M-1] = x(xFrec,tData[M-1:N+M-1])
xAxe             = fig.add_subplot(3,1,1)
xLn,xHighLn      = plt.plot(tData,xData,'r-o',[],[],'y-o')
xAxe.grid(True)
xAxe.set_xlim(0,M+N-2)
xAxe.set_ylim(np.min(xData),np.max(xData))
#--------------------------------------
hAxe = fig.add_subplot(3,1,2)
hLn, = plt.plot([],[],'b-o')
hAxe.grid(True)
hAxe.set_xlim(0,M+N-2)
hAxe.set_ylim(np.min(hData),np.max(hData))
#--------------------------------------
yAxe       = fig.add_subplot(3,1,3)
yLn,yDotLn = plt.plot([],[],'c-o',[],[],'ko')
yAxe.grid(True)
yAxe.set_xlim(0,M+N-2)
yAxe.set_ylim(np.min(xData),np.max(xData))
yData=[]
#--------------------------------------
def init():
    global yData
    yData=np.zeros(N+M-1)
    return hLn,xLn,xHighLn,yLn,yDotLn

def update(i):
    global yData
    t=np.linspace(-M+1+i,i,M,endpoint=True)
    yData[i]=np.sum(xData[i:i+M]*hData[::-1])
    xHighLn.set_data(t,xData[i:i+M])
    hLn.set_data(t,hData[::-1])
    yLn.set_data(tData[M-1:],yData)
    yDotLn.set_data(tData[M-1+i],yData[i])
    return hLn,xLn,xHighLn,yLn,yDotLn

ani=FuncAnimation(fig,update,M+N-1,init,interval=1000 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
