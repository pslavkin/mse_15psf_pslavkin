import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt

signalFrec = 1
N          = 50
fs         = 10
Bits       = 2
t          = np.arange(0,N/fs,1/fs)
signalC    = np.array([(2**7-1)*np.sin(2*np.pi*signalFrec*t),
             (2**7-1)*sc.sawtooth(2*np.pi*t,1),
             (2**7-1)*np.random.normal(0,1,len(t)),
             (2**7-1)*sc.square(2*np.pi*t,0.5)])

signalQ  = np.copy(signalC).astype(np.int16)
signalC  /= 2**(8-Bits)
signalQ += (2**(8-Bits))//2
signalQ  >>= 8-Bits

fig      = plt.figure()
for i in range(len(signalC)):
    contiAxe = fig.add_subplot(4,1,i+1)
    plt.step(t,signalQ[i],'r-')
    plt.plot(t,signalC[i],'b-')

plt.show()
