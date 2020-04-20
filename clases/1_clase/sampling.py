import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig        = plt.figure()

time, adc = [], []
ax2       = fig.add_subplot ( 2,2,2        )
ln2,      = plt.plot        ( [],[],'b-'   )
ax1       = fig.add_subplot ( 2,2,1        )
ln1,      = plt.plot        ( [0],[0],'r-' )
ax2.grid(True)
ax1.grid(True)
f      = 0
sample = 0
header = 0xAA
ax1.set_ylim(0 ,1024)
ax2.set_ylim(0 ,1024)

def initFile():
    global f;
    last=1000
    f=open("log.bin","rb")
    f.seek(0,2)
    fileSize=f.tell()
    if(fileSize>last):
        fileSize=last
    f.seek(-fileSize,2)

def init():
    return ln1,ln2

def readFile(size):
    global f,time,adc,sample,header;
    for chunk in range(1000):
        sync=False
        while sync==False:
            data = f.read(1)
            if len(data) == 1:
                if data[0] == header:
                    header^=0xFF
                    sync=True
            else:
                break
        while len(data)!=3:
            data+=f.read(1)
        sample+=1
        time.append(sample)
        adc.append (int.from_bytes(data[1:3],"little"))
    if len(time)>size:
        adc  = adc[len(adc)-size:]
        time = time[len(time)-size:]

def update(t):
    global time,adc
    readFile(20)
    ln1.set_data(time,adc)
    ln2.set_data(time,adc)
    ax1.set_xlim(np.min(time) ,np.max(time))
    ax2.set_xlim(np.min(time) ,np.max(time))
    return ln1,ln2


initFile()
ani = FuncAnimation(fig, update, 1000, init_func=init, blit=True, interval=10, repeat=True)
plt.show()

