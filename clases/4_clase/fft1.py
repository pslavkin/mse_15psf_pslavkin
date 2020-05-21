import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 100
N          = 100
frecIter   = 0
signalFrec = 2
#--------------------------------------
tData      = np.arange(0,N/fs,1/fs)
nData      = np.arange(0,N,1)
circleFrec = np.arange(-fs/2,fs/2,fs/N)
#------------SIGNAL--------------------------
signalData = np.exp(-nData/fs)*np.sin(2*np.pi*signalFrec*nData*1/fs)+0.2j*np.sin(2*np.pi*1.2*signalFrec*nData*1/fs)
signalAxe  = fig.add_subplot(2,2,2)
signalRLn,signalILn,= plt.plot(tData,np.real(signalData),'b-',tData,np.imag(signalData),'r-')
signalAxe.grid(True)
#------------FFT IFFT-----------------------
fftData  = np.fft.fft(signalData)
ifftData = np.fft.ifft(fftData)
fftData  = np.concatenate((fftData[N//2:N],fftData[0:N//2]))/N
#-----------FFT---------------------------
fftAxe                 = fig.add_subplot(2,2,3)
fftRLn,fftILn,fftAbsLn = plt.plot(circleFrec,np.real(fftData),'g-' ,circleFrec,np.imag(fftData),'y-' ,circleFrec,np.abs(fftData)**2,'k-')
fftAxe.grid(True)
#----------IFFT----------------------------
ifftAxe       = fig.add_subplot(2,2,4)
penRLn,penILn = plt.plot(tData,np.real(ifftData),'b-',tData,np.imag(ifftData),'r-')
ifftAxe.grid(True)
#--------------------------------------
plt.show()
