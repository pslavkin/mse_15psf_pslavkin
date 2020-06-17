#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:26:48 2020

@author: jenny
"""
import numpy as np
import matplotlib.pyplot as plt
############################

N  = 1000 # muestras
fs = 1000 # Hz

a0 = 1 # Volts
p0 = 0 # radianes
f0 = 10   # Hz

############################
def generador_senoidal (fs, f0, N, a0, p0):
    
    ts=1/fs        #tiempo de muestreo
    
    tt = np.linspace(0, (N-1)*ts, N).flatten()
      
    x = np.array([], dtype=np.float).reshape(N,0)
    
    aux = a0* np.sin( 2*np.pi*f0*tt + p0 )
    
    x = np.hstack([x, aux.reshape(N,1)] )
    
    signal=x
    
    return tt, signal
############################
    
tt,x=generador_senoidal(fs,f0,N,a0,p0)

plt.figure(1)
line_hdls = plt.plot(tt, x)
plt.title('Señal Senoidal' )
plt.xlabel('tiempo [segundos]')
plt.ylabel('Amplitud [V]')
    
axes_hdl = plt.gca()
    
axes_hdl.legend(line_hdls, 'signal', loc='upper right'  )
    
plt.show()





