import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np


#-----------------------------------------------------------------------
fs =1000		# FRECUENCIA DE SAMPLEO
signalFrec = 250		# RECUENCIA DE SEÑAL
N =1000			# NUMERO DE MUESTRAS
amp =1			# ESPECIFICA LA AMPLITUD DE LA SEÑAL


#-----------------------------------------------------------------------

fig = plt.figure(1)

def origSign( senial,fs, Nc ):
	# SEÑAL ORIGINAL
	# senial: 0: SENOIDAL, 1: CUADRADA, 2: TRIANGULAR
												# MUESTRAS DE LA SEÑAL
	tc = np.arange(0.95,Nc/fs,1/10000)						# PUNTOS SOBRE EJE X
	ax1 = fig.add_subplot(3,1,1)
				
	if senial == 0:	
		ax1.plot(tc, amp*np.sin(2*np.pi*tc*signalFrec),"b-")
	elif senial == 1:
		ax1.plot(tc, amp*sc.square(2*np.pi*tc*signalFrec),"b-")
	else:
		ax1.plot(tc, amp*sc.sawtooth(2*np.pi*tc*signalFrec,0.5),"b-")
	ax1.grid(True)
		

def senoidal(fs,f0,amp,muestras,fase):
	origSign( 0, 1000,1000 )								# SE PASA VALOR FIJO PARA RESOLUCION

	td = np.arange(0.95,muestras/fs,1/fs)
	ax2 = fig.add_subplot(3,1,2)
	ax2.plot(td, amp*np.sin(2*np.pi*(td + fase/2*np.pi*1/fs )*signalFrec),"r-")
	ax2.grid(True)

	f0 = f0*fs

	td2 = np.arange(0.95,muestras/fs,1/f0)

	ax3 = fig.add_subplot(3,1,3)
	ax3.plot(td2, amp*np.sin(2*np.pi*(td2 + fase/2*np.pi*1/f0 )*signalFrec),"r-")
	ax3.grid(True)

def cuadrada(fs,f0,amp,muestras):
	origSign( 1, 1000,1000 )								# SE PASA VALOR FIJO PARA RESOLUCION

	td = np.arange(0.95,muestras/fs,1/fs)
	ax2 = fig.add_subplot(3,1,2)
	ax2.plot(td, amp*sc.square(2*np.pi*td*signalFrec),"r-o")
	ax2.grid(True)

	f0 = f0*fs

	td2 = np.arange(0.95,muestras/fs,1/f0)
	ax3 = fig.add_subplot(3,1,3)
	ax3.plot(td2, amp*sc.square(2*np.pi*td2*signalFrec),"r-o")
	ax3.grid(True)

def triangular(fs,f0,amp,muestras):
	origSign( 2, 1000,1000 )								# SE PASA VALOR FIJO PARA RESOLUCION

	td = np.arange(0.95,muestras/fs,1/fs)
	ax2 = fig.add_subplot(3,1,2)
	ax2.plot(td, amp*sc.sawtooth(2*np.pi*td*signalFrec,0.5),"r-o")
	ax2.grid(True)

	f0 = f0*fs

	td2 = np.arange(0.95,muestras/fs,1/f0)
	ax3 = fig.add_subplot(3,1,3)
	ax3.plot(td2, amp*sc.sawtooth(2*np.pi*td2*signalFrec, 0.5),"r-o")
	ax3.grid(True)


#senoidal(1000,0.49,1,1000,0)
#cuadrada(1000,0.49,1,1000)
triangular(1000,0.49,1,1000)

plt.show()




