import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os

N = 512
fs     = 10000
header = b'header'
fig    = plt.figure (1 )
adcAxe = fig.add_subplot ( 1,1,1 )
time   = np.linspace(0,N/fs,N)
adcLn, maxLn, minLn, rmsLn, \
= plt.plot ([],[],'r',[],[],'b',[],[],'b',[],[],'g')
adcAxe.grid ( True )
adcAxe.set_ylim ( -512 ,512 )
adcAxe.set_xlim ( 0 ,N/fs )

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
    for chunk in range(N):
        adc.append (readInt4File(logFile)/2**6)
    adcLn.set_data ( time,adc )
    maxLn.set_data ( time,np.full(N,readInt4File(logFile)/2**6))
    minLn.set_data ( time,np.full(N,readInt4File(logFile)/2**6))
    rmsValue=readInt4File(logFile)/2**6
    rmsLn.set_data ( time,np.full(N,rmsValue))
    rmsLn.set_label(rmsValue)
    rmsLg   = adcAxe.legend()
    return adcLn, maxLn, minLn, rmsLn,rmsLg

logFile=open("log.bin","w+b")
ani=FuncAnimation(fig,update,10,None,blit=True,interval=10,repeat=True)
plt.draw()
plt.show()

