import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
import matplotlib
from matplotlib.animation import FuncAnimation
from buttons import buttonOnFigure
#--------------------------------------
fig   = plt.figure()
fs    = 2

hData = np.zeros(2)
hData[:] = [1,2]
M     = len(hData)
xData = np.zeros(2)
xData[:] = [3,4]
N     = len(xData)
tData = np.arange(0,N+M-1,1)

xLnArray=[]
yData=np.zeros(N+M-1)
hLn=[]
yLn=[]
for i in range(N):
    xAxe  = fig.add_subplot(N+1,2,2*i+1)
    xLn,xHighLn,  = plt.plot(tData[0:N],xData,'r-',tData[i],xData[i],'yo')
    xLnArray.append(xLn)
    xAxe.grid(True)
    xAxe.set_xlim(0,N-1)
    xAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)
#--------------------------------------
    hAxe  = fig.add_subplot(N+1,2,2*i+2)
    Ln,  = plt.plot([],[],'b-o')
    hLn.append(Ln)
    hAxe.grid(True)
    hAxe.set_xlim(0,N+M-2)
    hAxe.set_ylim(np.min(hData*xData[i])-0.1,np.max(hData*xData[i])+0.1)
#--------------------------------------
yAxe  = fig.add_subplot(N+1,2,N*2+2)
yData=np.convolve(hData,xData)
yLn,  = plt.plot([],[],'b-o')
yAxe.grid(True)
yAxe.set_xlim(0,N+M-2)
yAxe.set_ylim(np.min(yData)-0.01,np.max(yData)+0.01)
yData=np.zeros(N+M-1)
#--------------------------------------
def init():
    return yLn,

def update(i):
    hLn[i].set_data(tData[i:M+i],hData*xData[i])
    yData[i:i+M]+=hData*xData[i]
    yLn.set_data(tData[0:N+M-1],yData)

    ani.event_source.stop()
    return yLn,

ani=FuncAnimation(fig,update,N,init,interval=50 ,blit=False,repeat=False)
plt.get_current_fig_manager().window.showMaximized()
b=buttonOnFigure(fig,ani)
plt.show()
