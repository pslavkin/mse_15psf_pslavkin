import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
#--------------------------------------
fig        = plt.figure()
fs         = 1000
N          = 2048
firData=np.transpose(np.load("7_clase/ciaa/psf2/band_pass.npy").astype(float))[0]

#firData=np.insert(firData,0,firData[-1]) #ojo que pydfa me guarda 1 dato menos...
M          = len(firData)

firExtendedData=np.concatenate((firData,np.zeros(N-1)))
impar=((N+M-1)%2)
#--------------------------------------
tData=np.linspace(0,(N+M-1)/fs,N+M-1,endpoint=False)
fData=np.concatenate((np.linspace(-fs/2,0,(N+M-1)//2,endpoint=False),\
       np.linspace(0,fs/2,(N+M-1)//2+impar,endpoint=False)))
#--------------------------------------
firAxe  = fig.add_subplot(2,1,1)
firLn,  = plt.plot(tData,firExtendedData,'b-o',label="h")
firAxe.legend()
firAxe.grid(True)
firAxe.set_xlim(0,(N+M-2)/fs)
firAxe.set_ylim(np.min(firData),np.max(firData))
#--------------------------------------
HData=np.fft.fft(firExtendedData)
circularHData=np.concatenate((HData[len(HData)//2+impar:],HData[0:len(HData)//2+impar]))
HAxe  = fig.add_subplot(2,1,2)
HLn,  = plt.plot(fData,np.abs(circularHData),'r-o',label="H")
HAxe.legend()
HAxe.grid(True)
HAxe.set_xlim(-fs/2,fs/2)
#--------------------------------------
def convertToC(h,H,fileName):
    cFile  = open(fileName,"w+")
    cFile.write("#define h_LENGTH {}\n".format(len(firData)))
    cFile.write("#define h_PADD_LENGTH {}\n".format(len(h)))
    cFile.write("#define H_PADD_LENGTH {}\n".format(len(H)))
    h*=2**15
    h=h.astype(np.int16)
    H*=2**15
    cFile.write("q15_t h[]={\n")
    for i in h:
        cFile.write("{},\n".format(i))
    cFile.write("};\n")
    cFile.write("q15_t H[]={\n")
    for i in H:
        cFile.write("{},{},\n".format(np.real(i).astype(np.int16),np.imag(i).astype(np.int16)))
    cFile.write("};\n")

convertToC(firExtendedData,HData,"7_clase/ciaa/psf2/src/fir.h")
plt.get_current_fig_manager().window.showMaximized()
plt.show()
