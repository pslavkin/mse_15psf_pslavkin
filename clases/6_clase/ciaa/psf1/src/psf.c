#include "sapi.h"
#include "arm_math.h"
#include "arm_const_structs.h"
#include "fir.h" 

#define MAX_FFT_LENGTH 2048
int16_t fftLength = 512;
int16_t hLength = h_LENGTH;
int16_t adc  [ MAX_FFT_LENGTH];
q15_t x      [ MAX_FFT_LENGTH]        ;
q15_t fftOut [ ( MAX_FFT_LENGTH)*2 ]  ;
q15_t fftMag [ ( MAX_FFT_LENGTH)/2+1 ];

uint32_t maxIndex   = 0;
q15_t maxValue      = 0;
arm_rfft_instance_q15 S;
uint16_t convLength = 0;
uint16_t sample     = 0;

int calcFftLength(int N,int M) {
   int convLength=N+M-1,i;
   for(i=MAX_FFT_LENGTH;i>=convLength;i>>=1)
      ;
   return i<<1;
}
int sendStr(char A[],int N) { uartWriteByteArray ( UART_USB ,A ,N ); }
int sendBlock(q15_t A[],int N) { uartWriteByteArray ( UART_USB ,(uint8_t* )A ,2*N ); }


int main ( void ) {
   boardConfig        (                          );
   uartConfig         ( UART_USB, 460800         );
   adcConfig          ( ADC_ENABLE               );
   cyclesCounterInit  ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      convLength=calcFftLength(fftLength,hLength);
      for(sample=0;sample<fftLength;sample++) {
         cyclesCounterReset();
         adc[sample] = ((int16_t )adcRead(CH1)-512)<<6;
         gpioToggle( LEDB);
         while(cyclesCounterRead()< 20400)
            ;
      }
      for(sample=fftLength;sample<convLength;sample++)
         adc[sample]=0;
      sendStr   ( "header"   ,6    );
      sendBlock ( &fftLength ,1    );
      sendBlock ( &convLength   ,1 );
      sendBlock ( adc ,convLength  );
      sendBlock ( h ,convLength    );
      arm_conv_fast_q15 ( adc,fftLength,h,convLength-fftLength+1,x );
      arm_rfft_init_q15 ( &S ,convLength ,0 ,1 );
      arm_rfft_q15      ( &S ,x     ,fftOut    );
      arm_cmplx_mag_squared_q15 ( fftOut ,fftMag ,convLength/2+1               );
      arm_max_q15               ( fftMag ,convLength/2+1 ,&maxValue ,&maxIndex );
      sendBlock ( fftOut    ,convLength );
      sendBlock ( &maxValue  ,1 );
      sendBlock ( (q15_t* )&maxIndex ,1 );
      gpioToggle( LEDR);
   }
}
