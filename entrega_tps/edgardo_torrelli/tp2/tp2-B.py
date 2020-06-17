import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np


#-----------------------------------------------------------------------
fs =200			# FRECUENCIA DE SAMPLEO Hz
signalFrec = 200	# RECUENCIA DE SEÑAL Hz
N =100			# NUMERO DE MUESTRAS
amp =1			# ESPECIFICA LA AMPLITUD DE LA SEÑAL


#-----------------------------------------------------------------------

corte = 100
plt.title('Corte en 100')
fig = plt.figure(1)



def fourier(datos):
	global fs
	fourier = np.fft.fft(datos)/len(datos)
	fourier = fourier[range(int(len(datos)/2))]

	tpCount = len(datos)
	values = np.arange(int(tpCount/2))
	timePeriod = tpCount/fs
	frequencies = values/timePeriod

	ax2 = fig.add_subplot(4,1,4)
	ax2.plot(frequencies/2, abs(fourier)**2,"r-")
	ax2.grid(True)

def fourier_graf(datos):

	fourier = datos[range(int(len(datos)/2))]
	ax2 = fig.add_subplot(4,1,4)
	ax2.plot(np.arange(len(datos)/2), abs(fourier)**2,"g-")
	ax2.grid(True)




def graf_ifft_2_axis(data, val_corte):							# SUPONE LA RECEPCION DE UN ARRAY DE COMPLEJOS
										# GRAFICA:
										# PARTE REAL (EN UN GRAFICO)
										# PARTE IMAGINARIA (EN UN GRAFICO)
	x_len = len(data)/2							# PARTE REAL E IMAGINARIA

	val_corte_neg = val_corte * -1

	x_real = []
	x_imag = []
	i = 0
	while i < x_len:
		if data[i].real < val_corte and data[i].real > val_corte_neg and data[i].imag < val_corte and data[i].imag > val_corte_neg:
			x_real.append(data[2*i].real)
			x_imag.append(data[2*i+1].imag)
		i+=1



	ax3 = fig.add_subplot(3,1,1)
	ax3.plot( np.arange(0,len(x_real),1), x_real,"b-")
	ax3.grid(True)

	ax4 = fig.add_subplot(3,1,2)
	ax4.plot( np.arange(0,len(x_imag),1), x_imag,"b-")
	ax4.grid(True)

	ax5 = fig.add_subplot(3,1,3)
	ax5.plot( x_real, x_imag,"r-")
	ax5.grid(True)





# PUNTO 3: ANTI TRANSFORMADA DISCRTA DE FOURIER
ti = np.load('fft_hjs.npy')							# OBTENCION DEL ARRAY
Nti = ti/2									# OBTENCION DEL NUMERO DE MUESTRAS
i_ti = np.fft.ifft(ti)

graf_ifft_2_axis(i_ti, corte)

#fourier_graf(ti)

#print(ti)
#print(len(ti))



plt.show()




