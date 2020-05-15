import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N= 40
fs= 40

fig = plt.figure(1)

circleAxe = fig.add_subplot(2,2,1)
circleLn,massLn = plt.plot([],[],'r-',[],[],'go')
circleAxe.grid(True)
circleAxe.set_xlim(-1,1)
circleAxe.set_ylim(-1,1)
circleLn.set_label(0)
circleLg=circleAxe.legend()
circleData=[]
circleFrec=[-fs/2]
tData=[]

signalAxe = fig.add_subplot(2,2,2)
signalLn, = plt.plot([],[],'b-')
signalAxe.grid(True)
signalAxe.set_xlim(0,N/fs)
signalAxe.set_ylim(-1,1)
signalData=[]
signalFrec=4
frecIter=0

promAxe = fig.add_subplot(2,2,3)
promLn, = plt.plot([],[],'g-o')
promAxe.grid(True)
promAxe.set_xlim(-fs/2,fs/2)
promAxe.set_ylim(-1,1)
promData=[0]

def signal(f,n,c):
    return c*np.cos(2*np.pi*f*n*1/fs)
def circle(f,n,c):
    return c*np.exp(-2j*np.pi*f*n*1/fs)


def update(n):
    global tData, signalData, circleData,frecIter
    tData.append(n/fs)
    circleData.append(circle(circleFrec[-1],n,1)*signal(signalFrec,n,1))
    massData=np.average(circleData)
    promData[-1]=massData
    circleLn.set_data(np.real(circleData) ,np.imag(circleData))
    massLn.set_data(np.real(massData) ,np.imag(massData))

    signalData.append(signal(signalFrec,n,1))
    signalLn.set_data(tData ,signalData)

    circleLn.set_label(circleFrec[-1])
    circleLg=circleAxe.legend()
    promLn.set_data(circleFrec,np.real(promData))
    if n==N-1:
        frecIter+=1
        if frecIter == N:
            ani.repeat=False
        else:
            promData.append(0)
            circleFrec.append(-fs/2+frecIter*fs/N)
            promLn.set_data(circleFrec,np.real(promData))
        tData=[]
        signalData=[]
        circleData=[]
    return circleLn,circleLg,signalLn,massLn,promLn

ani=FuncAnimation(fig,update,N,None,interval=100,blit=True,repeat=True)
plt.show()
