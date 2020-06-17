#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:39:48 2020

@author: jenny
"""
import numpy as np
from scipy import signal as sp
import matplotlib.pyplot as plt

N  = 1000
fs = 1000
a0 = 1
f0=10

t=np.linspace(0.0,(N-1)/fs,N)
funcion = sp.square(2 *np.pi*f0*t)

plt.plot(t, funcion)
plt.title('Señal Cuadrada')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo(t)')

plt.show()
