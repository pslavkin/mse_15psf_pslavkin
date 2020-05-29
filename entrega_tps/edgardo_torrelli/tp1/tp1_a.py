from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#----------------------------------------------------------------------
fs =100		# FRECUENCIA DE LA SEÑAL
N =10			# NUMERO DE MUESTRAS
fase =0
amp =1			# ESPECIFICA LA AMPLITUD DE LA SEÑAL

ciclos =4		# NUMERO DE CICLOS

#-----------------------------------------------------------------------

# VALOR DEL EJE X
X = []
Y = []
Xs = []
Ys = []


iG =0

# VALOR DEL EJE Y


fig, ax = plt.subplots(1,1)
ax.grid(True)

# AMPLITUD EN X - GRAFICADOR
ax.set_xlim([0, ciclos*1/fs])

# AMPLITUD EN Y - GRAFICADOR
ax.set_ylim([-amp-1, amp+1])


#SEÑAL
def mysignal(f,n):
  return np.sin(2*np.pi*n/f*fs/N)

def my_square_signal(f,n):
  return signal.square(2*np.pi*n/f*fs/N)

def my_triangle_signal(f,n):
  return signal.sawtooth(2*np.pi*n/f*fs/N, 0.5)


# SIMIL ARRAYLIST PARA ALMACENAMIENTO DE DATOS DE Fx1
sinegraph, = ax.plot([], [],'b')
dot, = ax.plot([], [], 'o', color='blue')

# SIMIL ARRAYLIST PARA ALMACENAMIENTO DE DATOS DE Fx2
sinegraph2, = ax.plot([], [],'r')

dot2, = ax.plot([], [], 'o', color='red')

def senoidal(fs,f0,amp,muestras,fase):
    global X,Y,Xs,Ys,iG
    X.append(1/fs*(iG*1/muestras))
    Xs.append(1/fs*(iG-fase)*1/muestras)
    Y.append(mysignal(fs,iG))				# CALCULO DE Y PARA FS
    Ys.append(mysignal(f0,iG))				# CALCULO DE Y PARA F0
#    sinegraph.set_data(X,Y)
    dot.set_data(X[iG],Y[iG])
    sinegraph2.set_data(Xs,Ys)
    dot2.set_data(Xs[iG],Ys[iG])
    if iG == ciclos*N-1:
       X=[]
       Y=[]
       Xs=[]
       Ys=[]
 
def cuadrada(fs,f0,amp,muestras):
    global X,Y,Ys,iG

    X.append(1/fs*(iG*1/muestras))
    Y.append(mysignal(fs,iG))
    Ys.append(my_square_signal(fs,iG))
    sinegraph.set_data(X,Y)
    dot.set_data(X[iG],Y[iG])
    sinegraph2.set_data(X,Ys)
    dot2.set_data(X[iG],Ys[iG])
    if iG == ciclos*N-1:
       X=[]
       Y=[]
       Ys=[]

def triangular(fs,f0,amp,muestras):
    global X,Y,Ys,iG

    X.append(1/fs*(iG*1/muestras))
    Y.append(mysignal(fs,iG))
    Ys.append(my_triangle_signal(fs,iG))
    sinegraph.set_data(X,Y)
    dot.set_data(X[iG],Y[iG])
    sinegraph2.set_data(X,Ys)
    dot2.set_data(X[iG],Ys[iG])
    if iG == ciclos*N-1:
       X=[]
       Y=[]
       Ys=[]




def update(i):
    global iG
    iG = i
    senoidal(fs,fs*0.51,1,N,0)
    #cuadrada(fs,fs,1,N)
    #triangular(fs,fs,1,N)




anim = animation.FuncAnimation(fig,update, ciclos*N, interval=10)
plt.show()
