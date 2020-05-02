import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fs = 50
N = 100

t = np.arange(0,N/fs,1/fs)

signalFrec=3
signal = np.cos(2*np.pi*signalFrec*t)


fig=plt.figure()
plt.plot(t,signal)


mng = plt.get_current_fig_manager()
mng.full_screen_toggle()



