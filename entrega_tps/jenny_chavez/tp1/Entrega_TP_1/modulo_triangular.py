#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:41:39 2020

@author: jenny
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

N  = 1000
fs = 1000
a0 = 1
f0=10

t=np.linspace(0.0,(N-1)/fs,N)
# simetria de la señal triangular diente de sierra
simetria=0.5

senal = signal.sawtooth(2 * np.pi * f0 * t, simetria)

# SALIDA
plt.plot(t,senal)
plt.title('Señal Triangular')
plt.xlabel('Tiempo(t)')
plt.ylabel('Amplitud')
plt.show()