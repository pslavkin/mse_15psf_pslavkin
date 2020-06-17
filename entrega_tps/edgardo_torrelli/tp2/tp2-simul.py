import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np


#-----------------------------------------------------------------------
fs =200			# FRECUENCIA DE SAMPLEO Hz
signalFrec = 200	# RECUENCIA DE SEÑAL Hz
N =100			# NUMERO DE MUESTRAS
amp =1			# ESPECIFICA LA AMPLITUD DE LA SEÑAL


#-----------------------------------------------------------------------

fig = plt.figure(1)

def origSign( senial,fs, Nc,amp ):
	# SEÑAL ORIGINAL
	# senial: 0: SENOIDAL, 1: CUADRADA, 2: TRIANGULAR
												# MUESTRAS DE LA SEÑAL
	tc = np.arange(0,Nc/fs,1/fs)						# PUNTOS SOBRE EJE X
	ax1 = fig.add_subplot(2,1,1)
				
	if senial == 0:	
		ax1.plot(tc, amp*np.sin(2*np.pi*tc*signalFrec),"b-")		# OPCION 0: SENOIDE
	elif senial == 1:
		ax1.plot(tc, amp*sc.square(2*np.pi*tc*signalFrec),"b-")		# OPCION 1: CUADRADA
	elif senial == 2:
		ax1.plot(tc, amp*sc.sawtooth(2*np.pi*tc*signalFrec,0.5),"b-")	# OPCION 2: TRIANGULAR
	else:
		ti = amp*sc.unit_impulse(len(tc))				# OPCION 3: DELTA
		ax1.plot(tc, ti,"b-")
					
	ax1.grid(True)



def fourier(datos):
	global fs
	fourier = np.fft.fft(datos)/len(datos)
	fourier = fourier[range(int(len(datos)/2))]

	tpCount = len(datos)
	values = np.arange(int(tpCount/2))
	timePeriod = tpCount/fs
	frequencies = values/timePeriod

	ax2 = fig.add_subplot(2,1,2)
	ax2.plot(frequencies, abs(fourier)**2,"r-")
	ax2.grid(True)



def senoidal(fs,f0,amp,muestras,fase):
	origSign( 0, fs,muestras,amp )								# SE PASA VALOR FIJO PARA RESOLUCION
	td = np.arange(0,muestras,1/fs)
	td = amp*np.sin(2*np.pi*td*signalFrec)
	fourier(td)	


def cuadrada(fs,f0,amp,muestras):
	origSign( 1, fs,muestras,amp )								# SE PASA VALOR FIJO PARA RESOLUCION
	td = np.arange(0,muestras,1/fs)
	td = amp*sc.square(2*np.pi*td*signalFrec)
	fourier(td)


def triangular(fs,f0,amp,muestras):
	origSign( 2, fs,muestras,amp  )								# SE PASA VALOR FIJO PARA RESOLUCION

	td = np.arange(0,muestras,1/fs)
	td = amp*sc.sawtooth(2*np.pi*td*signalFrec,0.5)
	fourier(td)

def delta(fs,f0,amp,muestras):
	origSign( 3, fs,muestras,amp  )								# SE PASA VALOR FIJO PARA RESOLUCION

	td = np.arange(0,muestras,1/fs)	
	td = amp*sc.unit_impulse(len(td))
	fourier(td)

# ----------------------------------------------------------------------------------------------------------------------------------
# PUNTO 1
# VALORES UTILIZADOS:
# fs =10000		# FRECUENCIA DE SAMPLEO Hz
# signalFrec = 200	# RECUENCIA DE SEÑAL Hz
# N =100		# NUMERO DE MUESTRAS

#senoidal(fs,1,2,N,0)
#cuadrada(fs,1,2,N)
#triangular(fs,1,2,N)
#delta(fs,1,2,N)


# ----------------------------------------------------------------------------------------------------------------------------------
# PUNTO 2
# VALORES UTILIZADOS:
# fs = 200		# FRECUENCIA DE SAMPLEO Hz
# signalFrec = ?	# RECUENCIA DE SEÑAL Hz
# N =100		# NUMERO DE MUESTRAS

def sig_pto2(fs,N,data):
	tc = np.arange(0,N/fs,1/fs)						# PUNTOS SOBRE EJE X
	ax1 = fig.add_subplot(2,1,1)
	ax1.plot(tc, data,"b-")
	ax1.grid(True)

dt = [ 0.00000000e+00, 9.98458667e-01, -7.82172325e-02, -9.86184960e-01,
1.54508497e-01, 9.61939766e-01, -2.26995250e-01, -9.26320082e-01,
2.93892626e-01, 8.80202983e-01, -3.53553391e-01, -8.24724024e-01,
4.04508497e-01, 7.61249282e-01, -4.45503262e-01, -6.91341716e-01,
4.75528258e-01, 6.16722682e-01, -4.93844170e-01, -5.39229548e-01,
5.00000000e-01, 4.60770452e-01, -4.93844170e-01, -3.83277318e-01,
4.75528258e-01, 3.08658284e-01, -4.45503262e-01, -2.38750718e-01,
4.04508497e-01, 1.75275976e-01, -3.53553391e-01, -1.19797017e-01,
2.93892626e-01, 7.36799178e-02, -2.26995250e-01, -3.80602337e-02,
1.54508497e-01, 1.38150398e-02, -7.82172325e-02, -1.54133313e-03,
1.83758918e-15, 1.54133313e-03, 7.82172325e-02, -1.38150398e-02,
-1.54508497e-01, 3.80602337e-02, 2.26995250e-01, -7.36799178e-02,
-2.93892626e-01, 1.19797017e-01, 3.53553391e-01, -1.75275976e-01,
-4.04508497e-01, 2.38750718e-01, 4.45503262e-01, -3.08658284e-01,
-4.75528258e-01, 3.83277318e-01, 4.93844170e-01, -4.60770452e-01,
-5.00000000e-01, 5.39229548e-01, 4.93844170e-01, -6.16722682e-01,
-4.75528258e-01, 6.91341716e-01, 4.45503262e-01, -7.61249282e-01,
-4.04508497e-01, 8.24724024e-01, 3.53553391e-01, -8.80202983e-01,
-2.93892626e-01, 9.26320082e-01, 2.26995250e-01, -9.61939766e-01,
-1.54508497e-01, 9.86184960e-01, 7.82172325e-02, -9.98458667e-01,
5.63708916e-15, 9.98458667e-01, -7.82172325e-02, -9.86184960e-01,
1.54508497e-01, 9.61939766e-01, -2.26995250e-01, -9.26320082e-01,
2.93892626e-01, 8.80202983e-01, -3.53553391e-01, -8.24724024e-01,
4.04508497e-01, 7.61249282e-01, -4.45503262e-01, -6.91341716e-01,
4.75528258e-01, 6.16722682e-01, -4.93844170e-01, -5.39229548e-01]

# IMPLEMENTANDO CERO PADING
i = 0
while i < 0:
	i+=1
	dt.append(0)

sig_pto2(200,len(dt),dt)
fourier(dt)



plt.show()




