import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 200
N1          =100
N2          =0
N=N1+N2
frecIter   = 0
signalFrec = 50
#--------------------------------------
tData      = np.arange(0,N/fs,1/fs)
n1Data      = np.arange(0,N1,1)
n2Data      = np.arange(N1,N1+N2,1)
circleFrec = np.arange(-fs/2,fs/2,fs/N)
#------------SIGNAL--------------------------
signalData1 = 0.5*np.sin(2*np.pi*signalFrec*n1Data*1/fs)+0.5*np.sin(2*np.pi*(2.5+signalFrec)*n1Data*1/fs)
signalData2 = np.zeros(abs(N2))
signalData=np.concatenate((signalData1,signalData2))
print(signalData)
#signalData = np.exp(-nData/fs)*np.sin(2*np.pi*signalFrec*nData*1/fs)+0.2j*np.sin(2*np.pi*1.2*signalFrec*nData*1/fs)
signalAxe  = fig.add_subplot(2,1,1)
signalRLn,signalILn,= plt.plot(tData,np.real(signalData),'b-o',tData,np.imag(signalData),'r-')
signalAxe.grid(True)
#------------FFT IFFT-----------------------
fftData  = np.fft.fft(signalData)
ifftData = np.fft.ifft(fftData)
fftData  = np.concatenate((fftData[N//2:N],fftData[0:N//2]))/N
#-----------FFT---------------------------
fftAxe                 = fig.add_subplot(2,1,2)
fftAbsLn = plt.plot(circleFrec,np.abs(fftData)**2,'k-o')
fftAxe.grid(True)
#----------IFFT----------------------------
#ifftAxe       = fig.add_subplot(2,2,4)
#penRLn,penILn = plt.plot(tData,np.real(ifftData),'b-',tData,np.imag(ifftData),'r-')
#ifftAxe.grid(True)
#--------------------------------------
plt.show()
