import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fs = 100
N = 30
circleFrec=0.0
signalFrec=10
padd=2

fig = plt.figure()
circleAxe=fig.add_subplot(2,2,1)
circleLn,mixLn,massLn =plt.plot([],[],'r',[],[],'g',[],[],'bo')
circleAxe.grid(True)
circleLn.set_label(circleFrec)
circleLeg=circleAxe.legend()
mix=[]

signalAxe=fig.add_subplot(2,2,2)
signalLn,=plt.plot([],[],'b')
signalAxe.grid(True)

fAxe=fig.add_subplot(2,2,3)
fLn,=plt.plot([],[],'r-o')
fAxe.grid(True)
fData,fFrec=[],[]



t = np.arange(0,N/fs,1/fs)

def circle(f,n):
    return np.exp(-1j*2*np.pi*f*t)[n] 

signal = np.cos(2*np.pi*signalFrec*t)+0.3*np.sin(2*np.pi*2*signalFrec*t)
signal = np.hstack((signal[:-padd],np.zeros(padd)))
fftData=np.fft.fft(signal)
fftAxe=fig.add_subplot(2,2,4)
fftLn,=plt.plot(fs*t,(np.abs(fftData)/N)**2,'r-')
fftAxe.grid(True)


def init():
    print("arranca")
    circleAxe.set_xlim(-2,2)
    circleAxe.set_ylim(-2,2)
    signalAxe.set_xlim(0,N/fs)
    signalAxe.set_ylim(-2,2)
    fAxe.set_xlim(0,fs)
    fAxe.relim()
    fAxe.autoscale_view()
    plt.draw()
    return circleLn, signalLn, mixLn,massLn,circleLeg,fLn

def update(n):
    global circleFrec, mix,fData,fFrec
    circleLn.set_data([0,3*np.real(circle(circleFrec,n))],[0,3*np.imag(circle(circleFrec,n))])
    mix.append(circle(circleFrec,n)*signal[n])
    mixLn.set_data(np.real(mix),np.imag(mix))
    massLn.set_data(np.average(np.real(mix)),np.average(np.imag(mix)))
    signalLn.set_data(t[:n],signal[:n])
    circleLn.set_label(circleFrec)
    circleLeg=circleAxe.legend()
    if(n==(N-1)):
        fData.append(np.average(mix))
        fFrec.append(circleFrec)
        fLn.set_data(fFrec,np.abs(fData)**2)
        circleFrec+=fs/N
        mix=[]
#    fAxe.set_ylim(np.min(np.abs(fData)**2),np.max(np.abs(fData)**2)) 
    return circleLn, signalLn, mixLn,massLn,circleLeg,fLn

def updateF(n):
    global mix,fData
    circleFrec=n*(fs/N)
    for n in range(N):
        mix.append(circle(circleFrec,n)*signal[n])
        mixLn.set_data(np.real(mix),np.imag(mix))
        massLn.set_data(np.average(np.real(mix)),np.average(np.imag(mix)))
        signalLn.set_data(t[:n],signal[:n])
        circleLn.set_label(circleFrec)
        circleLeg=circleAxe.legend()

    fData.append(np.average(mix))
    fFrec.append(circleFrec)
    fLn.set_data(fFrec,np.abs(fData)**2)
    fAxe.relim()
    fAxe.autoscale_view()
    mix=[]
    return circleLn, signalLn, mixLn,massLn,circleLeg,fLn

#ani=FuncAnimation(fig,update,N,init,blit=True,interval=100,repeat=True)
ani=FuncAnimation(fig,updateF,N,init,blit=True,interval=100,repeat=False)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

