import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt

signalFrec = 1
NC         = 200
fsC        = 100
Bits       = 2
tC         = np.arange(0,NC/fsC,1/fsC)
signalC    = np.array([(2**7-1)*np.sin(2*np.pi*signalFrec*tC),
             (2**7-1)*sc.sawtooth(2*np.pi*tC,1),
             (2**7-1)*np.random.normal(0,1,len(tC)),
             100*sc.square(2*np.pi*tC,0.5)],dtype='int16')

signalQ  = np.copy(signalC)
signalQ += (2**(8-Bits))//2
signalQ  &= 0xFFFF<<(8-Bits)

fig      = plt.figure()
for i in range(len(signalC)):
    contiAxe = fig.add_subplot(4,1,i+1)
    plt.step(tC,signalQ[i],'r-')
    plt.plot(tC,signalC[i],'b-')

plt.show()
