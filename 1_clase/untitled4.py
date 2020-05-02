import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fs=100
N=100
signalFrec=2
circleFrec=-2*N/fs

t=np.arange(0,N/fs,1/fs)
signal=np.cos(2*np.pi*signalFrec*t)


def circleX(f,index):
    return np.sin(2*np.pi*f*t)[index]
def circleY(f,index):
    return np.cos(2*np.pi*f*t)[index]


fig=plt.figure()
circleAxe=fig.add_subplot(2,2,1)
circleLn,MixLn,=plt.plot([0],[0],'r-',[0],[0],'b-')
circleAxe.grid(True)
MixDataX,MixDataY=[],[]

signalAxe=fig.add_subplot(2,2,2)
signalLn,=plt.plot([],[],'g-')
signalAxe.grid(True)


def init():
    global circleFrec
    print("arranca")
    circleFrec+=N/fs
    circleAxe.set_xlim(-2,2)
    circleAxe.set_ylim(-2,2)
    signalAxe.set_ylim(-1,1)
    signalAxe.set_xlim(0,N/fs)
    return signalLn,circleLn,MixLn
    
def update(index):
    global circleFrec,MixDataX,MixDataY
    circleLn.set_data([0,2*circleX(circleFrec,index)],[0,2*circleY(circleFrec,index)])
    MixDataX.append(circleX(circleFrec,index)*signal[index])
    MixDataY.append(circleY(circleFrec,index)*signal[index])
    MixLn.set_data(MixDataX,MixDataY)
    signalLn.set_data(t[:index],signal[:index])

    return signalLn,circleLn,MixLn

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
ani=FuncAnimation(fig,func=update,frames=N,init_func=init,blit=True,interval=10,repeat=True)
plt.show()

                


