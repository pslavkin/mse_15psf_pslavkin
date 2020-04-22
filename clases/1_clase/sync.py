import numpy as np
import matplotlib.pyplot as plt

signalFrec = 50
NC         = 30000
fsC        = 10000
tC         = np.arange(0,NC/fsC,1/fsC)
signalC    = np.sin(2*np.pi*signalFrec*tC)
fsD        = np.array([101])#,120,80,45])

fig        = plt.figure()
#signalC   = np.sin(2*np.pi*signalFrec*tC)+np.sin(2*np.pi*210*tC)

def sinc_interp(x, s, u):
    if len(x) != len(s):
        raise Exception('x and s must be the same length')
    ## Find the period
    T = s[1] - s[0]
    sincM = np.tile(u, (len(s), 1)) - np.tile(s[:, np.newaxis], (1, len(u)))
    y = np.dot(x, np.sinc(sincM/T))
    return y

def interpolate(Xn,B,tC):
    Xt=[]
    for t in tC:
        prom=0
        for n in range(len(Xn)):
           prom+=Xn[n]*np.sinc(2*B*t-n)
        Xt.append(prom)
    return Xt

for i in range(len(fsD)):
    contiAxe = fig.add_subplot(4,1,i+1)
    Xt=sinc_interp(signalC[::fsC//fsD[i]],tC[::fsC//fsD[i]],tC)

    #Xt=interpolate(signalC[::fsC//fsD[i]],fsD//2,tC)
    plt.plot(tC,signalC,'r-',tC,Xt,'b-')
    contiAxe = fig.add_subplot(4,1,i+2)
    plt.plot(tC,signalC,'r-',tC[::fsC//fsD[i]],signalC[::fsC//fsD[i]],'b-')
    contiAxe.set_ylabel(fsD[i])




plt.show()
