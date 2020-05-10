import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os

length = 512
fs     = 10000
header = b'header'
fig    = plt.figure (1 )
adcAxe = fig.add_subplot ( 1,1,1 )
time   = np.linspace(0,length/fs,length)
adcLn, = plt.plot ( [],[],'r' )
adcAxe.grid ( True )
adcAxe.set_ylim ( -512 ,512 )
adcAxe.set_xlim ( 0 ,length/fs )

def findHeader(f):
    index = 0
    sync  = False
    while sync==False:
        data=b''
        while len(data) <1:
            data = f.read(1)
        if data[0]==header[index]:
            index+=1
            if index>=len(header):
                sync=True
                print(sync)
        else:
            index=0
            print(sync)

def readInt4File(f):
    raw=b''
    while len(raw)<2:
        raw += f.read(1)
    return (int.from_bytes(raw[0:2],"little",signed=True))

def update(t):
    findHeader ( logFile )
    adc = []
    for chunk in range(length):
        adc.append (readInt4File(logFile))
    adcLn.set_data ( time,adc )
    return adcLn,

logFile=open("log.bin","w+b")
ani=FuncAnimation(fig,update,10,None,blit=True,interval=10,repeat=True)
plt.draw()
plt.show()

