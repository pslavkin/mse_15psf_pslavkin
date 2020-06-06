
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os
import scipy.fftpack as sc
from   scipy.io.wavfile import write

fs=10000

fftLength           = 32
convLength             = 0
fig                 = plt.figure ( )

adcAxe            = fig.add_subplot ( 3,1,1 )
adcAxe.grid ( True )
adcLn,              = plt.plot ( [0],[0],'r-' )
adcAxe.set_ylim     ( -1 ,1         )

hAxe            = fig.add_subplot ( 3,1,2 )
hAxe.grid ( True )
hLn,              = plt.plot ( [0],[0],'b-' )
hAxe.set_ylim     ( -0.02 ,0.2         )

dftAxe              = fig.add_subplot ( 3,2,5 )
dftAxe.grid ( True )
dftLn,              = plt.step ( [0],[0],'b-o' )
dftAxe.set_xlim     ( 0  ,fs//2   )

ciaaDftAxe          = fig.add_subplot ( 3,2,6 )
ciaaDftLn,ciaaMaxLn = plt.step ( [0],[0],'g-o',0,0,'bo' )
ciaaDftAxe.grid ( True )
ciaaDftAxe.set_xlim ( 0  ,fs//2   )


maxIndex = 0
maxValue = 0
dft,ciaaDft = [1],[1]

def initFiles():
    global logFile
    logFile   = open("log.bin","w+b")
    logFile.seek(0, os.SEEK_END)

def fileForward(f):
    packetLegth=len(b'header')+2+2+6*convLength+2+2
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
                print(sync)
        else:
            index=0
            print(sync)

def readInt4File(f):
    raw=b''
    while len(raw)<2:
        raw   += f.read(1)
    return (int.from_bytes(raw[0:2],"little",signed=True))

def readFile(f):
    fileForward(f)
    findHeader(f)
    fftLength  = readInt4File(f)
    convLength = readInt4File(f)
    ciaaDft = []
    adc     = []
    h     = []
    for chunk in range(convLength):
        adc.append ( readInt4File(f )/(2**15))
    for chunk in range(convLength):
        h.append ( readInt4File(f )/(2**15))
    for chunk in range(convLength):
        if(chunk%2==0):
            real = readInt4File(f )/2**13
        else:
            im   = readInt4File(f )*1j/2**13
            ciaaDft.append (real+im)
    maxValue = readInt4File(f)/2**5
    maxIndex = readInt4File(f)
    print(convLength)
    #q6rint(maxIndex)
    #maxValue = (np.abs(ciaaDft[maxIndex])**2)
    return maxIndex,maxValue,adc,h,ciaaDft,fftLength,convLength

def init():
    global fftLength,convLength,dft,ciaaDft
    adcAxe.set_xlim     ( 0  ,convLength)
    hAxe.set_xlim     ( 0  ,convLength)
    dftAxe.set_ylim     ( 0  ,np.max(dft            )+0.001)
    ciaaDftAxe.set_ylim ( 0  ,np.max(np.abs(ciaaDft ))+0.001)
    plt.draw()
    return adcLn,dftLn,ciaaDftLn,ciaaMaxLn,hLn

def update(t):
    global logFile,fftLength,convLength,dft,ciaaDft,fs
    maxIndex,maxValue,adc,h,ciaaDft,fftLength,convLength=readFile(logFile)
    time = np.arange(0,convLength,1)
    frec = np.linspace(0,fs//2,convLength//2)
    dft  = (np.abs(np.fft.fft(adc))/len(adc))

    adcLn.set_data(time,adc)
    hLn.set_data(time,h)
    dftLn.set_data(frec,dft[:convLength//2])
    ciaaDftLn.set_data(frec,np.abs(ciaaDft))
    ciaaMaxLn.set_data(frec[maxIndex],maxValue)
    return adcLn,dftLn,ciaaDftLn,ciaaMaxLn,hLn


initFiles()
ani=FuncAnimation(fig, update, 100, init, blit=True, interval=20, repeat=True)
plt.show()

