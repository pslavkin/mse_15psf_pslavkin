import numpy as np
import scipy.signal as sc
import scipy.io.wavfile as sciw
import simpleaudio as sa
import matplotlib.pyplot as plt

fig        = plt.figure()
fs  = 8000
def noise(n):
    return ((2**13)+np.random.normal(scale=1000))*np.sin((1600+500*n)*n*(2*np.pi))

#fs,audio=sciw.read("tp2/chapu.wav")
#a=np.ndarray(len(audio)).astype(np.int16)
#
#for i in range(len(audio)):
#    a[i]=audio[i]+noise(i/fs)
#
#np.save("tp2/chapu_noise.npy",a)
a=np.load("tp2/chapu_noise.npy")

audioAxe  = fig.add_subplot(4,1,1)
audioLn,= plt.plot(np.linspace(0,3,len(a)),a,'b-')

play_obj = sa.play_buffer(a, 1, 2, fs)
play_obj.wait_done()
play_obj = sa.play_buffer(a, 1, 2, fs)
play_obj.wait_done()

signalAxe  = fig.add_subplot(4,1,2)
signalLn,  = plt.plot(np.linspace(0,len(a)/fs,len(a)),a,'b-')

fft=np.fft.fft(a)
fftAxe  = fig.add_subplot(4,1,3)
fftLn,= plt.plot(np.arange(0,len(fft),1),np.abs(fft),'b-')

lo_pass,=np.load("tp2/lo_pass.npy").astype(float)
out=np.convolve(a,lo_pass).astype(np.int16)

fft=np.fft.fft(out)
fftAxe  = fig.add_subplot(4,1,4)
fftLn,= plt.plot(np.arange(0,len(fft),1),np.abs(fft),'b-')

play_obj = sa.play_buffer(out, 1, 2, fs)
play_obj.wait_done()
plt.show()

