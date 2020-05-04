import numpy as np
import matplotlib.pyplot as plt

signalFrec = 50
NC         = 1000
fsC        = 3000
tC         = np.arange(0,NC/fsC,1/fsC)
signalC    = np.sin(2*np.pi*signalFrec*tC)
fsD        = [200,102,80,43]

fig      = plt.figure()
signalC    = np.sin(2*np.pi*signalFrec*tC)+0.5*np.sin(2*np.pi*210*tC)

for i in range(len(fsD)):
    contiAxe = fig.add_subplot(4,1,i+1)
    plt.plot(tC,signalC,'r-',tC[::fsC//fsD[i]],signalC[::fsC//fsD[i]],'b-o')
    contiAxe.set_ylabel(fsD[i])

plt.show()
