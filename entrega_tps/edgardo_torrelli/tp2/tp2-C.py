import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np
import simpleaudio as sa


#-----------------------------------------------------------------------
fs =8000			# FRECUENCIA DE SAMPLEO Hz

#-----------------------------------------------------------------------
# FILTRA PASABAJOS CON CORTE A PARTIR DE 1500 Hz

fpb = [
-0.00034793347208506915,
0.0007571972993684927,
0.002209983304325619,
0.0032979570824389513,
0.0028459677837201474,
0.0009169656118662187,
-0.0009844919247816396,
-0.0013010247644017151,
-6.482383626660761e-05,
0.0011059958868505804,
0.0008172037033508352,
-0.0005061846321047353,
-0.0011680227857348599,
-0.0003089169275439712,
0.0009889063080048778,
0.001034563956943752,
-0.00029596037881681283,
-0.0013150790611803974,
-0.0006449239037239167,
0.0009360022048731121,
0.001381204113713546,
1.084003548866668e-05,
-0.0014808149716430857,
-0.0011065898262078496,
0.0007786133529521935,
0.0017701091829062411,
0.00047055890895894223,
-0.0015629522885638157,
-0.0016651560954789475,
0.00045304444715230416,
0.0021321514607493455,
0.0010895545461619808,
-0.001492822761237669,
-0.002279136997562397,
-7.688671706026534e-05,
0.0023984667456228314,
0.001855203145910834,
-0.0012120640219453072,
-0.002892284580751198,
-0.0008307712475341399,
0.002498926435775069,
0.0027371873593442664,
-0.0006689047869553002,
-0.0034363120621449424,
-0.0018132795021882984,
0.002358234570754257,
0.0036861181204050006,
0.00017960500979550477,
-0.003829457225406078,
-0.0030116008576995708,
0.0019000097465202374,
0.004635445955203978,
0.001367866488120852,
-0.003977082849748986,
-0.004395386319956272,
0.0010466116387261122,
0.005500115645121462,
0.002919121113361296,
-0.003775745964639875,
-0.005922192463864792,
-0.00028647906326917773,
0.006177212340315397,
0.004855363626031981,
-0.003098619770766443,
-0.007531556287443412,
-0.0021961027978376012,
0.00653916219379349,
0.0072036256281584376,
-0.0017836852104130023,
-0.009146480149925166,
-0.004813426069714107,
0.006415379682840321,
0.010001861870422074,
0.00037906397906030463,
-0.010696990455987621,
-0.008359271840071156,
0.005582390952618417,
0.013399655615628553,
0.00379238767102133,
-0.012095865349842812,
-0.013296616499128883,
0.0036179431679199256,
0.017744980141377587,
0.00928025596633299,
-0.013276341910933605,
-0.02079872521107068,
-0.0004452231230266563,
0.024112535270490804,
0.019181484607868556,
-0.014170016249827054,
-0.03474082195562374,
-0.009876735411212284,
0.03688761902417841,
0.04368870413684355,
-0.014727266747732675,
-0.07875170202666273,
-0.04965516041840214,
0.10512632971623648,
0.29774616305559015,
0.3850831481072023,
0.29774616305559015,
0.10512632971623648,
-0.04965516041840214,
-0.07875170202666273,
-0.014727266747732675,
0.04368870413684355,
0.03688761902417841,
-0.009876735411212284,
-0.03474082195562374,
-0.014170016249827054,
0.019181484607868556,
0.024112535270490804,
-0.0004452231230266563,
-0.02079872521107068,
-0.013276341910933605,
0.00928025596633299,
0.017744980141377587,
0.0036179431679199256,
-0.013296616499128883,
-0.012095865349842812,
0.00379238767102133,
0.013399655615628553,
0.005582390952618417,
-0.008359271840071156,
-0.010696990455987621,
0.00037906397906030463,
0.010001861870422074,
0.006415379682840321,
-0.004813426069714107,
-0.009146480149925166,
-0.0017836852104130023,
0.0072036256281584376,
0.00653916219379349,
-0.0021961027978376012,
-0.007531556287443412,
-0.003098619770766443,
0.004855363626031981,
0.006177212340315397,
-0.00028647906326917773,
-0.005922192463864792,
-0.003775745964639875,
0.002919121113361296,
0.005500115645121462,
0.0010466116387261122,
-0.004395386319956272,
-0.003977082849748986,
0.001367866488120852,
0.004635445955203978,
0.0019000097465202374,
-0.0030116008576995708,
-0.003829457225406078,
0.00017960500979550477,
0.0036861181204050006,
0.002358234570754257,
-0.0018132795021882984,
-0.0034363120621449424,
-0.0006689047869553002,
0.0027371873593442664,
0.002498926435775069,
-0.0008307712475341399,
-0.002892284580751198,
-0.0012120640219453072,
0.001855203145910834,
0.0023984667456228314,
-7.688671706026534e-05,
-0.002279136997562397,
-0.001492822761237669,
0.0010895545461619808,
0.0021321514607493455,
0.00045304444715230416,
-0.0016651560954789475,
-0.0015629522885638157,
0.00047055890895894223,
0.0017701091829062411,
0.0007786133529521935,
-0.0011065898262078496,
-0.0014808149716430857,
1.084003548866668e-05,
0.001381204113713546,
0.0009360022048731121,
-0.0006449239037239167,
-0.0013150790611803974,
-0.00029596037881681283,
0.001034563956943752,
0.0009889063080048778,
-0.0003089169275439712,
-0.0011680227857348599,
-0.0005061846321047353,
0.0008172037033508352,
0.0011059958868505804,
-6.482383626660761e-05,
-0.0013010247644017151,
-0.0009844919247816396,
0.0009169656118662187,
0.0028459677837201474,
0.0032979570824389513,
0.002209983304325619,
0.0007571972993684927,
-0.00034793347208506915,
]

# FIN FILTRA PASABAJOS CON CORTE A PARTIR DE 1500 Hz
#-----------------------------------------------------------------------



plt.title('Convolucion')
fig = plt.figure(1)


def fourier(datos):
	global fs
	fourier = np.fft.fft(datos)/len(datos)
	fourier = fourier[range(int(len(datos)/2))]

	print(len(fourier))

	tpCount = len(datos)
	values = np.arange(int(tpCount/2))
	timePeriod = tpCount/fs
	frequencies = values/timePeriod

	ax2 = fig.add_subplot(1,1,1)

	#ax2.plot(np.arange(len(fourier)), abs(fourier)**2,"r-")			#GRAFICO DE FRECUENCIAS SOBRE LARGO MUESTRAS
	ax2.plot(frequencies, abs(fourier)**2,"r-")					#GRAFICO DE FRECUENCIAS EN Hz
	ax2.grid(True)


def grafico_signal(datos):
	ax1 = fig.add_subplot(1,1,1)
	ax1.set_ylim ( -20000 ,20000 )
	ax1.plot(np.arange(0,len(datos)/fs,1/fs), datos,"b-")


# ------------------------------------------------------------------------------

# PUNTO 4: CONVOLUCION
ti = np.load('chapu_noise.npy')							# OBTENCION DEL ARRAY DE SEÑAL
										# LONGITUD 18713

										# GRAFICO DE ESPECTRO SIN FILTRAR
										# GRAFICO DE FRECUENCIAS
#grafico_signal(ti)
#fourier(ti)

# ------------------------------------------------------------------------------
										# FILTRADO POR CONVOLUCION
#data_fourier = np.fft.fft(ti)							# FFT SEÑAL
#filtro_fourier = np.fft.fft(ti)
filtrado = np.convolve(ti,fpb)
print(len(ti))
print(len(filtrado))
#grafico_signal(filtrado)


audio = filtrado.astype(np.int16)
for i in range(10):
 play_obj = sa.play_buffer(audio,1,2,fs)
 play_obj.wait_done()


plt.show()



