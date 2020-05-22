import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig = plt.figure()
fs  = 100
N   = 400
fir,=np.load("4_clase/low_pass.npy").astype(float)
M=len(fir)
#fir,=np.load("diferenciador.npy").astype(float)
#M=len(fir)
#--------------------------------------
def x(f,n):
    return np.sin(2*np.pi*2*n*1/fs)+\
           np.sin(2*np.pi*5*n*1/fs)

xFrec = 3
tData=np.arange(-(M-1),N+(M-1),1)
xData=np.zeros(N+2*(M-1))
xData[M:M+N]=x(xFrec,tData[M:M+N])
xAxe  = fig.add_subplot(3,1,1)
xLn,xHighLn  = plt.plot(tData,xData,'r-',[],[],'y-')
xAxe.grid(True)
xAxe.set_xlim(-M,M+N-2)
xAxe.set_ylim(np.min(xData),np.max(xData))
#--------------------------------------
hData=fir
hAxe  = fig.add_subplot(3,1,2)
hLn,  = plt.plot([],[],'b-')
hAxe.grid(True)
hAxe.set_xlim(-M,M+N-2)
hAxe.set_ylim(np.min(hData),np.max(hData))
#--------------------------------------
yAxe  = fig.add_subplot(3,1,3)
yLn,  = plt.plot([],[],'c-')
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

ani=FuncAnimation(fig,update,M+N-1,init,interval=10 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
