import numpy as np
import matplotlib.pyplot as plt

signalFrec = 50
NC         = 300
fsC        = 2000
tC         = np.arange(0,NC/fsC,1/fsC)
signalC    = np.sin(2*np.pi*signalFrec*tC)
fsD        = np.array([300,120,80,45])


fig        = plt.figure()
signalC   = np.sin(2*np.pi*signalFrec*tC)+0.5*np.sin(2*np.pi*110*tC)

def interpolate(x, s, u):
    y=[]
    B = 1/((s[1] - s[0])*2)
    for t in u:
        prom=0
        for n in range(len(x)):
           prom+=x[n]*np.sinc(2*B*t-n)
        y.append(prom)
    return y

for i in range(len(fsD)):
    contiAxe = fig.add_subplot(4,1,i+1)
    Xt=interpolate(signalC[::fsC//fsD[i]],tC[::fsC//fsD[i]],tC)
    plt.plot(tC,signalC,'r-',tC,Xt,'b-')

plt.show()
