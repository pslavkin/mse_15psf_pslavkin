import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fs=10
N=100
frecCircle = -2/fs #cob blit en True la fucnion init se lanza 2 veces antes al arrancar...chan.
fig        = plt.figure()
frec2      = 2

t   = np.arange(0, N/fs, 1/fs)
f   = np.arange(0, fs, fs/N)

xfft, yfft               = [], []
xmass, ymass             = [1], [1]
xCircle, yCircle         = [0,0,0], [0,0,0]
xdata, ydata             = [], []
signalXdata, signalYdata = [], []
ax2                      = fig.add_subplot ( 2,2,2      )
ln2,                     = plt.plot       ( [],[],'b-' )
ax2.grid(True)


ax4                      = fig.add_subplot ( 2,2,4      )
actualFftLn,             = plt.plot       ( [1],[1],'b-' )
ax4.grid(True)
#actualFft=np.abs(np.fft.fft(signal(t)/len(f)**2))
actualFft=np.fft.fft(signal(t))
actualFftLn.set_data(f, actualFft)
ax4.set_ylim(min(actualFft),max(actualFft))
ax4.set_xlim(0,fs)

ax1=fig.add_subplot(2,2,1)
ln1,ln3,ln4 =plt.plot([],[],'r-',[],[],'b-o',[],[],'go')
ax1.grid(True)
ln1.set_label(frecCircle)
ax1Legend=ax1.legend()

ax3=fig.add_subplot(2,2,3)
fft, =plt.plot([],[],'bo-')
ax3.grid(True)

ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax2.set_xlim(0, N/fs)
ax2.set_ylim(0, 2)
ax3.set_xlim(0, fs)
ax3.set_ylim(0, 2)




def init():
    global frecCircle,xdata,ydata,signalXdata,signalYdata


    xfft.append(fs*frecCircle)
#    yfft.append(xmass[0])
    yfft.append(math.sqrt(xmass[0]**2+ymass[0]**2))
    frecCircle+=1/fs
    if(frecCircle==1):
        exit
    xdata=[0]
    ydata=[0]
    signalXdata=[0]
    signalYdata=[0]
    return ln1,ln2,ln3,ln4,fft,ax1Legend


def signal(t):
    return 1+np.cos (frec2*2*np.pi*t)#+np.sin(frec2*3*np.pi*t)

#def signal (t ):
#    percent= ( t%(1/frec2 ))/(1/frec2) * 100
#    ans=0
#    #si me paso de lo pedido...pongo el valor positivo.
#    if percent < 50:
#        ans=1
#    return ans
def circleX(t):
    return np.cos(-frecCircle*2*np.pi*t)
def circleY(t):
    return np.sin(-frecCircle*2*np.pi*t)

def update(t):
    global frecCircle,xdata,ydata,signalXdata,signalYdata
    xdata.append(circleX(t)*signal(t))
    ydata.append(circleY(t)*signal(t))
    signalXdata.append(t)
    signalYdata.append(signal(t))
    xCircle[1]=circleX(t)*signal(t)
    yCircle[1]=circleY(t)*signal(t)
    xCircle[2]=5*circleX(t)
    yCircle[2]=5*circleY(t)

    xmass[0]=np.average(xdata)
    ymass[0]=np.average(ydata)

    ln1.set_data(xdata,ydata)
    ln2.set_data(signalXdata,signalYdata)
    ln3.set_data(xCircle,yCircle)
    ln4.set_data(xmass,ymass)
    fft.set_data(xfft,yfft)
    ln1.set_label(frecCircle)
    ax1Legend=ax1.legend()
    return ln1,ln2,ln3,ln4,fft,ax1Legend

def updateFft(f):
    global frecCircle,xdata,ydata,signalXdata,signalYdata
    xdata=circleX(t)*signal(t)
    ydata=circleY(t)*signal(t)
    frecCircle=f
    

    
    signalXdata=t
    signalYdata=signal(t)

    xmass[0]=np.average(xdata)
    ymass[0]=np.average(ydata)

    xfft.append(frecCircle)
#    yfft.append(xmass[0])
    yfft.append(math.sqrt(xmass[0]**2+ymass[0]**2))
    ln1.set_data(xdata,ydata)
    ln2.set_data(signalXdata,signalYdata)
    ln3.set_data(xCircle,yCircle)
    ln4.set_data(xmass,ymass)
    fft.set_data(xfft,yfft)

    return ln1,ln2,ln3,ln4,fft


ani = FuncAnimation(fig, update, t, init_func=init, blit=True, interval=100, repeat=True)
#ani = FuncAnimation(fig, updateFft, f, init_func=init, blit=True, interval=1000, repeat=False)
plt.show()

