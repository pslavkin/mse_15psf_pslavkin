#include "sapi.h"
#include "arm_math.h"
#include "arm_const_structs.h"

#define MAX_FFT_LENGTH 2048         // maxima longitud para la fft y chunk de samples
#define BITS 10                     // cantidad de bits usado para cuantizar
#define FIR_LENGTH 162
int16_t fftLength = 32;             // longitud de la fft y samples variable
int16_t adc [ MAX_FFT_LENGTH ];     // guarda los samples
q15_t fftIn [ MAX_FFT_LENGTH ];     // guarda copia de samples en Q15 como in para la fft.La fft corrompe los datos de la entrada!
q15_t fftOut[ MAX_FFT_LENGTH*2 ];   // salida de la fft
q15_t fftMag[ MAX_FFT_LENGTH/2+1 ]; // magnitud de la FFT
//low_pass 1000hz 127
//q15_t fir[ FIR_LENGTH]={ 22, 21, 24, 19, 6, -14, -40, -66, -83, -86, -73, -43, -3, 36, 65, 73, 56, 16, -35, -84, -115, -114, -77, -13, 63, 128, 161, 147, 84, -13, -119, -200, -227, -186, -81, 62, 204, 299, 310, 224, 56, -152, -341, -445, -422, -259, 11, 320, 575, 687, 593, 287, -176, -683, -1083, -1220, -977, -305, 755, 2074, 3450, 4656, 5480, 5772, 5480, 4656, 3450, 2074, 755, -305, -977, -1220, -1083, -683, -176, 287, 593, 687, 575, 320, 11, -259, -422, -445, -341, -152, 56, 224, 310, 299, 204, 62, -81, -186, -227, -200, -119, -13, 84, 147, 161, 128, 63, -13, -77, -114, -115, -84, -35, 16, 56, 73, 65, 36, -3, -43, -73, -86, -83, -66, -40, -14, 6, 19, 24, 21, 22};
//bandpass 440hz 162
q15_t fir[ FIR_LENGTH]={ 1, 0, 0, -0, -2, -5, -9, -14, -19, -25, -29, -32, -33, -30, -24, -14, 0, 17, 37, 57, 76, 91, 101, 104, 98, 83, 60, 31, -1, -36, -68, -95, -113, -121, -117, -103, -81, -54, -26, -3, 11, 13, 2, -22, -58, -99, -140, -172, -186, -175, -135, -62, 41, 170, 315, 461, 593, 694, 748, 742, 667, 522, 312, 46, -254, -566, -864, -1118, -1303, -1396, -1383, -1260, -1028, -704, -310, 123, 561, 967, 1307, 1551, 1679, 1679, 1551, 1307, 967, 561, 123, -310, -704, -1028, -1260, -1383, -1396, -1303, -1118, -864, -566, -254, 46, 312, 522, 667, 742, 748, 694, 593, 461, 315, 170, 41, -62, -135, -175, -186, -172, -140, -99, -58, -22, 2, 13, 11, -3, -26, -54, -81, -103, -117, -121, -113, -95, -68, -36, -1, 31, 60, 83, 98, 104, 101, 91, 76, 57, 37, 17, 0, -14, -24, -30, -33, -32, -29, -25, -19, -14, -9, -5, -2, -0, 0, 0, 1};

q15_t firOut [ MAX_FFT_LENGTH+FIR_LENGTH+1 ];

uint32_t maxIndex = 0;              // indexador de maxima energia por cada fft
q15_t maxValue    = 0;              // maximo valor de energia del bin por cada fft
arm_rfft_instance_q15 S;
uint16_t sample   = 0;              // contador para samples

int main ( void ) {
   boardConfig        (                          );
   uartConfig         ( UART_USB, 460800         );
   adcConfig          ( ADC_ENABLE               );
   cyclesCounterInit  ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();                                                          // inicializa el conteo de ciclos de reloj
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample]    ,sizeof(adc[0]) );   // envia el sample ANTERIOR
      uartWriteByteArray ( UART_USB ,(uint8_t* )&fftOut[sample] ,sizeof(fftOut[0])); // envia la fft del sample ANTERIO
      //TODO hay que mandar fftLength/2 "+1" y solo estoy mandando fftLength/2. revisar
      adc[sample]   =(((int16_t )adcRead(CH1)-512)>>(10-BITS))<<(6+10-BITS);         // PISA el sample que se acaba de mandar con una nueva muestra
      fftIn[sample] = adc[sample];                                                   // copia del adc porque la fft corrompe el arreglo de entrada
      if ( ++sample==fftLength ) {                                                   // si es el ultimo
         sample = 0;                                                                 // arranca de nuevo
         uartWriteByteArray ( UART_USB ,(uint8_t* )&maxValue ,2);
         uartWriteByteArray ( UART_USB ,(uint8_t* )&maxIndex ,2);
         uartWriteByteArray ( UART_USB ,"header" ,6 );                               // manda el header que casualmente se llama "header" con lo que arranca una nueva trama
         uartWriteByteArray ( UART_USB ,(uint8_t* )&fftLength ,sizeof(fftLength));   // manda el largo de la fft que es variable
         arm_conv_fast_q15(fftIn,fftLength,fir,FIR_LENGTH,firOut);
         arm_rfft_init_q15 ( &S ,fftLength ,0 ,1 );                                  // inicializa una estructira que usa la funcion fft para procesar los datos. Notar el /2 para el largo
         arm_rfft_q15      ( &S ,&firOut[FIR_LENGTH]     ,fftOut    );                             // por fin.. ejecuta la rfft REAL fft
         arm_cmplx_mag_squared_q15 ( fftOut ,fftMag ,fftLength/2+1 );
         arm_max_q15 ( fftMag ,fftLength/2+1 ,&maxValue ,&maxIndex );
         gpioToggle( LEDR);
         if ( gpioRead(TEC1 )==0) {
            gpioToggle(LEDB);
            if((fftLength<<=1)>MAX_FFT_LENGTH)
               fftLength=32;
            while(gpioRead(TEC1)==0)
               ;
         }
      }
      while(cyclesCounterRead()< 20400) //clk de 204000000 => 10k samples x seg.
         ;
   }
}

//guitard air chord freq
//1ra (E): 329,63 Hz
//2da (B): 246,94 Hz
//3ra (G): 196,00 Hz
//4ta (D): 146,83 Hz
//5ta (A): 110,00 Hz
//6ta (E): 82,41 Hz
