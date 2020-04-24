import numpy as np
import matplotlib.pyplot as plt

signalFrec = 1010
NC         = 300
fsC        = 1000
tC         = np.arange(-NC/fsC,NC/fsC,1/fsC)
#signalC    = np.sin(2*np.pi*signalFrec*tC)

fig        = plt.figure()
B=1/(2*(tC[1]-tC[0]))
B=signalFrec

sinc=np.sinc(2*B*tC)
contiAxe = fig.add_subplot(2,1,1)
plt.plot(tC,sinc,'b-')
contiAxe = fig.add_subplot(2,1,2)
plt.plot(NC*tC,np.abs(np.fft.fft(sinc)),'b-')

plt.show()
