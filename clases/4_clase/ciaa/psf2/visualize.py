import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os
import scipy.fftpack as sc
from   scipy.io.wavfile import write

fs=10000

fftLength           = 32
fig                 = plt.figure ( )
adcAxe            = fig.add_subplot ( 2,1,1 )
adcAxe.grid ( True )
adcLn,              = plt.plot ( [0],[0],'r-' )
adcAxe.set_ylim     ( -1 ,1         )

dftAxe              = fig.add_subplot ( 2,2,3 )
dftAxe.grid ( True )
dftLn,              = plt.step ( [0],[0],'b-o' )
dftAxe.set_xlim     ( 0  ,fs//2   )

ciaaDftAxe          = fig.add_subplot ( 2,2,4 )
ciaaDftLn,ciaaMaxLn = plt.step ( [0],[0],'g-o',0,0,'bo' )
ciaaDftAxe.grid ( True )
ciaaDftAxe.set_xlim ( 0  ,fs//2   )

maxIndex = 0
maxValue = 0
dft,ciaaDft = [1],[1]

def initFiles():
    global logFile
    logFile   = open("log.bin","rb")
    logFile.seek(0, os.SEEK_END)

def fileForward(f):
    packetLegth=((4*fftLength)+4+len(b'header')+2)
    oldPos = f.tell()
    f.seek(0, os.SEEK_END)
    size = f.tell()
    packetLoss=(size-oldPos)//packetLegth
    print(packetLoss)
    f.seek(oldPos+packetLoss*packetLegth, os.SEEK_SET)

def findHeader(f):
    index  = 0
    sync   = False
    header = b'header'
    while sync==False:
        data=b''
        while len(data) <1:
            data = f.read(1)
        if data[0] ==header[index]:
            index+=1
            if index>=len(header):
                sync=True
                #print(sync)
        else:
            index=0
            #print(sync)

def readInt4File(f):
    raw=b''
    while len(raw)<2:
        raw   += f.read(1)
    return (int.from_bytes(raw[0:2],"little",signed=True))

def readFile(f):
    fileForward(f)
    findHeader(f)
    fftLength= readInt4File(f)
    ciaaDft = []
    adc     = []
    for chunk in range(fftLength):
        adc.append ( readInt4File(f )/(2**15))
        if(chunk%2==0):
            real = readInt4File(f )/2**15
        else:
            im   = readInt4File(f )*1j/2**15
            ciaaDft.append (real+im)
    maxValue = readInt4File(f)/2**13
    maxIndex = readInt4File(f)
    #print(maxIndex)
    #maxValue = (np.abs(ciaaDft[maxIndex])**2)
    return maxIndex,maxValue,adc,ciaaDft,fftLength

def init():
    global fftLength,dft,ciaaDft
    adcAxe.set_xlim     ( 0  ,fftLength             )
    dftAxe.set_ylim     ( 0  ,np.max(dft            )+0.001)
    ciaaDftAxe.set_ylim ( 0  ,np.max(np.abs(ciaaDft )**2)+0.001)
    plt.draw()
    return adcLn,dftLn,ciaaDftLn,ciaaMaxLn

def update(t):
    global logFile,fftLength,dft,ciaaDft,fs
    maxIndex,maxValue,adc,ciaaDft,fftLength=readFile(logFile)
    time = np.arange(0,fftLength,1)
    frec = np.linspace(0,fs//2,fftLength//2)
    dft  = (np.abs(np.fft.fft(adc))/len(adc))**2

    adcLn.set_data(time,adc)
    dftLn.set_data(frec,dft[:fftLength//2])
    ciaaDftLn.set_data(frec,np.abs(ciaaDft)**2)
    ciaaMaxLn.set_data(frec[maxIndex],maxValue)
    return adcLn,dftLn,ciaaDftLn,ciaaMaxLn


initFiles()
ani=FuncAnimation(fig, update, 100, init, blit=True, interval=20, repeat=True)
plt.show()

