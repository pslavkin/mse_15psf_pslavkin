import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation
import os
import scipy.fftpack as sc
from   scipy.io.wavfile import write

fs=1000
CHORD_1=329.63  #E
CHORD_2=246.94  #B
CHORD_3=196.00  #G
CHORD_4=146.83  #D
CHORD_5=110.00  #A
CHORD_6= 82.41  #E
CHORD_WIDTh=2
chordsFrecs=[329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
chordsColors=["green","yellow","red","blue","magenta","black"]

fftLength  = 128
convLength = 2048

fig    = plt.figure ( )
adcAxe = fig.add_subplot ( 3,1,1 )
adcAxe.grid ( True )
adcLn, = plt.plot ( [0],[0],'r-' )
adcAxe.set_xlim     ( 0 ,fftLength         )
adcAxe.set_ylim     ( -0.6 ,0.6         )

ciaaDftAxe          = fig.add_subplot ( 3,1,3 )
ciaaDftLn , = plt.step ( [0] ,[0] ,'k-' )
ciaaMaxLn , = plt.plot ( 0   ,0   ,'bo')
ciaaDftAxe.grid ( True )
ciaaDftAxe.set_xlim ( 0  ,fs//2   )
ciaaDftAxe.legend(loc='upper center')

for i in range(6):
    ciaaDftAxe.fill_between([chordsFrecs[i]-CHORD_WIDTh,chordsFrecs[i]+CHORD_WIDTh],-10,2000,facecolor = chordsColors[i],alpha=0.4)


chordLn=[]
for i in range(6):
    chordAxe          = fig.add_subplot ( 3,6,7+i )
#    chordAxe.fill_between( chordsFrecs[i]-CHORD_WIDTh ,chordsFrecs[i]+CHORD_WIDTh,0,10,facecolor = "green",alpha   = 0.4)
    chordAxe.set_xlim ( chordsFrecs[i]-CHORD_WIDTh  ,chordsFrecs[i]+CHORD_WIDTh   )
    chordAxe.set_ylim ( 0  ,10   )
    Ln,  = plt.plot ( 0,0,'k',label=chordsFrecs[i])
    chordAxe.legend(loc='upper center',prop={'size': 20})
    chordLn.append(Ln)
    chordAxe.grid ( True )


maxIndex = 0
maxValue = 0
ciaaDft = [1]

def initFiles():
    global logFile
    logFile   = open("log.bin","w+b")
    logFile.seek(0, os.SEEK_END)

def fileForward(f):
    packetLegth=len(b'header')+4*fftLength+2+2
    oldPos = f.tell()
    f.seek(0, os.SEEK_END)
    size = f.tell()
    packetLoss=(size-oldPos)//packetLegth
    #print(packetLoss)
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
    global convLength,fftLength
    fileForward(f)
    findHeader(f)
    ciaaDft    = []
    adc        = []
    for chunk in range(fftLength):
        adc.append ( readInt4File(f )/(2**15))
        ciaaDft.append ( readInt4File(f ))
    for chunk in range(convLength-fftLength):
        adc.append (0)
    maxValue = readInt4File(f)/2**0
    maxIndex = readInt4File(f)
    maxPromIndex = readInt4File(f)*fs/(convLength*20)
    #print(maxIndex*fs/convLength)
    print(maxPromIndex)
    #print(maxValue)
    return maxPromIndex,maxIndex,maxValue,adc,ciaaDft

def init():
    global fftLength,convLength,dft,ciaaDft,maxIndex
    ciaaDftAxe.set_ylim ( 0  ,np.max(ciaaDft))
    plt.draw()
    return adcLn,ciaaDftLn,ciaaMaxLn

def update(t):
    global logFile,fftLength,convLength,dft,ciaaDft,fs,maxIndex,chordLn
    maxPromIndex,maxIndex,maxValue,adc,ciaaDft=readFile(logFile)
    time = np.arange(0,convLength,1)
    frec = np.linspace(0,fs//2,convLength//2)

    adcLn.set_data(time,adc)

    firstIndex=max(maxIndex-fftLength//2,0)
    lastIndex=min(convLength//2,firstIndex+fftLength)
    ciaaDftLn.set_data(frec[firstIndex:lastIndex],ciaaDft[:lastIndex-firstIndex])
    ciaaMaxLn.set_data(frec[maxIndex],maxValue)
    ciaaMaxLn.set_label(round(maxPromIndex,2))
    ciaaLegendLn=ciaaDftAxe.legend(loc='upper center',prop={'size': 26})

#    for i in chordLn:
#        i.set_data(maxPromIndex)
    multiIndex=np.full(10,maxPromIndex)
    multiData=np.arange(0,10,1)
    for i in chordLn:
        i.set_data(multiIndex,multiData)
        i.set_data(multiIndex,multiData)
        i.set_data(multiIndex,multiData)
        i.set_data(multiIndex,multiData)
        i.set_data(multiIndex,multiData)
        i.set_data(multiIndex,multiData)
    return adcLn,ciaaDftLn,ciaaMaxLn,ciaaLegendLn,chordLn[0],chordLn[1],chordLn[2],chordLn[3],chordLn[4],chordLn[5]


initFiles()
ani=FuncAnimation(fig, update, 10, init, blit=True, interval=20, repeat=True)
plt.show()

