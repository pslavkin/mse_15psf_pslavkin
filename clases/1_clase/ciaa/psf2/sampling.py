import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os
import scipy.fftpack as sc
from   scipy.io.wavfile import write

fftLength       = 32
fs              = 1000
fig             = plt.figure()
adcAxe          = fig.add_subplot ( 2,1,1         )
adcLn,          = plt.plot        ( [0],[0],'r-'  )
dftAxe          = fig.add_subplot ( 2,2,3         )
dftLn,          = plt.step        ( [0],[0],'b-o' )
ciaaDftAxe      = fig.add_subplot ( 2,2,4         )
ciaaDftLn,ciaaMaxLn,        = plt.step        ( [0],[0],'g-',[0],[0],'ro')
adcAxe.grid         ( True       )
dftAxe.grid         ( True       )
ciaaDftAxe.grid     ( True       )
adcAxe.set_ylim     ( -0.5 ,0.5  )
dftAxe.set_ylim     ( -0.001    ,0.005 )
ciaaDftAxe.set_ylim ( -0.001    ,0.005 )

def initFiles():
    global logFile
    last      = 1000
    logFile   = open("log.bin","rb")
    logFile.seek(0, os.SEEK_END)

def fileForward(f):
    packetLegth=((4*fftLength)+0+len(b'header')+2)
    oldPos = f.tell()
    f.seek(0, os.SEEK_END)
    size = f.tell()
    f.seek(oldPos+((size-oldPos)//packetLegth)*packetLegth, os.SEEK_SET)

def findHeader(f):
    index  = 0
    sync   = False
    header = b'header'
    while sync==False:
        data=b''
        while len(data) <1:
            data = f.read(1)
        if data[0]==header[index]:
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

def readCiaaAdcDft(f):
    ciaaDft   = []
    adc       = []
    for chunk in range(fftLength):
        adc.append (readInt4File(f)/(2**15))
        if(chunk%2==0):
            real = readInt4File(f)/2**15
        else:
            im   = readInt4File(f)*1j/2**15
            ciaaDft.append (real+im)
    return adc,np.concatenate([ciaaDft,ciaaDft[::-1]])


def readFile(f):
    global fftLength
    fileForward ( f )
    findHeader  ( f )
    fftLength = readInt4File(f)
    adc,ciaaDft=readCiaaAdcDft(f)
    maxValue=readInt4File(f)/(2**13); #a la 13 porque el calculo se hace en el micro y devuelve 3.13
    maxIndex=readInt4File(f)*fs/fftLength;
    return adc,ciaaDft,fftLength,maxValue,maxIndex

def init():
    adcAxe.set_xlim     ( 0,fftLength/fs )
    dftAxe.set_xlim     ( 0,fs           )
    ciaaDftAxe.set_xlim ( 0,fs           )
    plt.draw            (                )
    return adcLn,dftLn,ciaaDftLn

def update(t):
    global logFile,fftLength
    adc,ciaaDft,fftLength,maxValue,maxIndex = readFile(logFile)
    time                  = np.linspace(0,fftLength/fs,fftLength)
    frec                  = np.linspace(0,fs,fftLength)
    dft                   = (np.abs(np.fft.fft(adc))/len(adc))**2

    print(maxIndex,maxValue)
    ciaaMaxLn.set_data     ( maxIndex,maxValue       )
    adcLn.set_data     ( time,adc       )
    dftLn.set_data     ( frec,dft       )
    ciaaDftLn.set_data ( frec,np.abs(ciaaDft)**2)
    return adcLn,dftLn,ciaaDftLn,ciaaMaxLn,

initFiles()
ani=FuncAnimation(fig,update,10,init,blit=True,interval=20,repeat=True)
plt.show()

