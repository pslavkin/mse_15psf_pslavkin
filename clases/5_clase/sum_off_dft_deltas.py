import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
fig        = plt.figure()
fs         = 200
N          =100
signalFrec = 50
#-----------DELTA----------------------
delta=np.zeros(N)
delta[10] =N
delta2=np.zeros(N)
delta2[11] =0
#--------------------------------------
tData      = np.arange(0,N/fs,1/fs)
nData      = np.arange(0,N,1)
circleFrec = np.arange(-fs/2,fs/2,fs/N)
#------------SIGNAL--------------------------
signalData = delta
signal2Data = delta2
signalAxe  = fig.add_subplot(2,1,1)
signalRLn,signalILn,= plt.plot(tData,np.real(signalData),'b-o',tData,np.imag(signalData),'r-')
signalAxe.grid(True)
#------------FFT IFFT-----------------------
fftData  = np.fft.fft(signalData)
fft2Data  = np.fft.fft(signal2Data)
ifftData = np.fft.ifft(fftData)
fftData  = np.concatenate((fftData[N//2:N],fftData[0:N//2]))/N
fft2Data  = np.concatenate((fft2Data[N//2:N],fft2Data[0:N//2]))/N
#-----------FFT---------------------------
fftAxe                 = fig.add_subplot(2,1,2)
fftAbsLn, = plt.plot(circleFrec,np.real(fftData)**2+np.real(fft2Data)**2,'k-o')
fftAxe.grid(True)
#----------IFFT----------------------------
#ifftAxe       = fig.add_subplot(2,2,4)
#penRLn,penILn = plt.plot(tData,np.real(ifftData),'b-',tData,np.imag(ifftData),'r-')
#ifftAxe.grid(True)
#--------------------------------------
plt.show()
