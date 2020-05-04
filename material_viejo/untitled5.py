import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fs = 10
N = 10
circleFrec=1
signalFrec=2

t = np.arange(0,N/fs,1/fs)
signal = np.exp(-1j*2*np.pi*circleFrec*t) #1 + np.cos(2*np.pi*signalFrec*t) + np.sin(2*np.pi*signalFrec*2*t)

plt.plot(np.real(signal),np.imag(signal),'ro')


