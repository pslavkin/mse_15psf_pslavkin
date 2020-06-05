#include "sapi.h"
#include "arm_math.h"
#include "arm_const_structs.h"
#include "fir.h" 

#define MAX_FFT_LENGTH 1024
int16_t fftLength = 128;
int16_t hLength = h_LENGTH;
int16_t adc [ MAX_FFT_LENGTH    ];
q15_t x     [ MAX_FFT_LENGTH    ];
q15_t fftOut[ 2* MAX_FFT_LENGTH ];
q15_t H     [ 2* MAX_FFT_LENGTH ];
q15_t hTemp [ 2* MAX_FFT_LENGTH ];

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
      sendStr           ( "header"   ,6        );
      sendBlock         ( &fftLength ,1        );
      sendBlock         ( &convLength   ,1     );
      sendBlock         ( adc ,convLength      );
      sendBlock         ( h ,convLength        );
      arm_rfft_init_q15 ( &S ,convLength ,0 ,1 );
      arm_rfft_q15      ( &S ,adc     ,fftOut  );
      for(int i=0;i<convLength;i++)
         hTemp[i]=h[i];
      arm_rfft_init_q15 ( &S ,convLength ,0 ,1 );
      arm_rfft_q15      ( &S ,hTemp     ,H    );
      for(int i=0;i<convLength;i++)
         H[i]=H[i]*convLength;
      arm_cmplx_mult_cmplx_q15(fftOut,H,H,convLength);
      sendBlock ( H    ,convLength );
      arm_cmplx_mag_squared_q15 ( H ,H ,convLength/2+1               );
      arm_max_q15               ( H ,convLength/2+1 ,&maxValue ,&maxIndex );
      sendBlock ( &maxValue  ,1 );
      sendBlock ( (q15_t* )&maxIndex ,1 );
      gpioToggle( LEDR);
   }
}
