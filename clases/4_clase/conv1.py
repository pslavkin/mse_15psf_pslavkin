import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 20
N   = 20
M=10
#--------------------------------------
xFrec = 3
def x(f,n):
    return np.sin(2*np.pi*f*n*1/fs)
tData=np.arange(-(M-1),N+(M-1),1)
xData=np.zeros(N+2*(M-1))
xData[M-1:M-1+N]=x(xFrec,tData[M-1:M-1+N])
xAxe  = fig.add_subplot(3,1,1)
xLn,xHighLn  = plt.plot(tData,xData,'r-o',[],[],'y-o')
xAxe.grid(True)
xAxe.set_xlim(-M,M+N-2)
xAxe.set_ylim(np.min(xData),np.max(xData))
#--------------------------------------
hData=[0.1*n for n in range(M)]
hAxe  = fig.add_subplot(3,1,2)
hLn,  = plt.plot([],[],'b-o')
hAxe.grid(True)
hAxe.set_xlim(-M,M+N-2)
hAxe.set_ylim(np.min(hData),np.max(hData))
#--------------------------------------
yAxe  = fig.add_subplot(3,1,3)
yLn,  = plt.plot([],[],'c-o')
yAxe.grid(True)
yAxe.set_xlim(-M,M+N-1)
yAxe.set_ylim(np.min(xData),np.max(xData))
yData=[]
#--------------------------------------
def init():
    global yData
    yData=np.zeros(N+2*(M-1))
    return hLn,xLn,xHighLn,yLn,

def update(i):
    global yData
    t=np.linspace(-(M-1)+i,i,M,endpoint=True)
    yData[i]=np.sum(xData[i:i+M]*hData[::-1])
    xHighLn.set_data(t,xData[i:i+M])
    hLn.set_data(t,hData[::-1])
    yLn.set_data(tData,yData)
    return hLn,xLn,xHighLn,yLn,

ani=FuncAnimation(fig,update,M+N-1,init,interval=1000 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
