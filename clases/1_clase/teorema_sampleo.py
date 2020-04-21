import numpy as np
import matplotlib.pyplot as plt

signalFrec = 50
fsD        = 200
NC         = 1000
fsC        = 3000
ND         = NC/fsC*fsD
tC         = np.arange(0,NC/fsC,1/fsC)
tD         = np.arange(0,ND/fsD,1/fsD)
signalD    = np.sin(2*np.pi*signalFrec*tD)
signalC    = np.sin(2*np.pi*signalFrec*tC)

fig      = plt.figure()
contiAxe = fig.add_subplot(4,1,1)
contiLn,dicLn = plt.plot(tC,signalC,'r-',tD,signalD,'b-o')
contiAxe.set_ylabel(fsD)

fsD           = 120
ND           = NC/fsC*fsD
tD            = np.arange(0,ND/fsD,1/fsD)
signalD       = np.sin(2*np.pi*signalFrec*tD)
discAxe       = fig.add_subplot(4,1,2)
contiLn,dicLn = plt.plot(tC,signalC,'r-',tD,signalD,'b-o')
discAxe.set_ylabel(fsD)

fsD           = 80
ND            = NC/fsC*fsD
tD            = np.arange(0,ND/fsD,1/fsD)
signalD       = np.sin(2*np.pi*signalFrec*tD)
discAxe       = fig.add_subplot(4,1,3)
contiLn,dicLn = plt.plot(tC,signalC,'r-',tD,signalD,'b-o')
discAxe.set_ylabel(fsD)

fsD           = 45
ND            = NC/fsC*fsD
tD            = np.arange(0,ND/fsD,1/fsD)
signalD       = np.sin(2*np.pi*signalFrec*tD)
discAxe       = fig.add_subplot(4,1,4)
contiLn,dicLn = plt.plot(tC,signalC,'r-',tD,signalD,'b-o')
discAxe.set_ylabel(fsD)

plt.show()
