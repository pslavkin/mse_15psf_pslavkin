#include "sapi.h"
#include "arm_math.h"
#include "arm_const_structs.h"
#include "fir.h" 

enum CHORDS_FREC{
   CHORD_1E=32963,
   CHORD_2B=24694,
   CHORD_3G=19600,
   CHORD_4D=14683,
   CHORD_5A=11000,
   CHORD_6E= 8241,
};
#define fs 1000
//#define 50HZ=60*fs/convLength

#define MAX_FFT_LENGTH 2048
int16_t fftLength = 256;
int16_t hLength   = h_LENGTH;
int16_t adc  [ MAX_FFT_LENGTH];
q15_t x      [ MAX_FFT_LENGTH]        ;
q15_t fftOut [ MAX_FFT_LENGTH+2 ]  ;
q15_t fftMag [ MAX_FFT_LENGTH ];

uint32_t maxIndex   = 0;
uint32_t magIndex   = 0;
q15_t maxValue      = 0;
arm_rfft_instance_q15 S;
uint16_t convLength = 2048;
uint16_t sample     = 0;

int calcFftLength(int N,int M) {
   int convLength=N+M-1,i;
   for(i=MAX_FFT_LENGTH;i>=convLength;i>>=1)
      ;
   return i<<1;
}
int sendStr(char A[],int N) { uartWriteByteArray ( UART_USB ,A ,N ); }
int sendBlock(q15_t A[],int N) { uartWriteByteArray ( UART_USB ,(uint8_t* )A ,2*N ); }
void findFirstHarmonic(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex);
void findFirstLocalMax(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex);


int main ( void ) {
   boardConfig        (                          );
   uartConfig         ( UART_USB, 460800         );
   adcConfig          ( ADC_ENABLE               );
   cyclesCounterInit  ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample]    ,sizeof(adc[0]) );// envia el sample ANTERIOR
      uartWriteByteArray ( UART_USB ,(uint8_t* )&fftMag[magIndex-fftLength/2+sample] ,sizeof(fftOut[0])); // envia la fft del sample ANTERIO
      adc[sample] = ((int16_t )adcRead(CH1)-512)<<6;
      x[sample]=adc[sample];
      if ( ++sample==fftLength ) {                                                   // si es el ultimo
         sendBlock ( &maxValue  ,1 );
         sendBlock ( (q15_t* )&maxIndex ,1 );
         for(;sample<convLength;sample++)
            adc[sample]=0;
         sample = 0;                                                                 // arranca de nuevo
         sendStr   ( "header"   ,6    );
         //      arm_conv_fast_q15 ( adc,fftLength,h,convLength-fftLength+1,x );
         arm_rfft_init_q15 ( &S ,convLength ,0 ,1 );
         arm_rfft_q15      ( &S ,x     ,fftOut    );
         for(int i=0;i<(convLength+2);i++){
            fftOut[i]<<=5;
         }
         arm_cmplx_mag_squared_q15 ( fftOut ,fftMag ,convLength/2+1               );
         findFirstLocalMax(fftMag,convLength/2,50,&maxValue ,&maxIndex);
         magIndex=maxIndex>=(fftLength/2)?maxIndex:(fftLength/2);
         //findFirstHarmonic(fftMag,convLength/2,100,&maxValue ,&maxIndex);
         //arm_max_q15               ( fftMag ,convLength/2+1 ,&maxValue ,&maxIndex );
         gpioToggle( LEDB);
      }
      while(cyclesCounterRead()< 204000)
         ;
   }
}
void findFirstLocalMax(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex)
{
   int i=(convLength*60)/fs;
   q15_t localMax;
   *maxValue=0;
   *maxIndex=0;
   for (;i<length;i++)
      if(magFft[i]>threshold) 
         break;
   if(i>=length) return;
   localMax=magFft[i];
   for (;i<length;i++)
      if(magFft[i]>=localMax) 
         localMax=magFft[i];
      else {
       //  if((localMax-magFft[i])>(localMax/10) ) 
         {
            *maxValue=localMax;
            *maxIndex=i-1;
            return;
         }
      }
}
void findFirstHarmonic(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex)
{
   int i=(convLength*60)/fs;
   *maxValue=0;
   *maxIndex=0;
   
   for (;i<length;i++)
      if(magFft[i]>threshold) {
         *maxValue=magFft[i];
         *maxIndex=i;
         break; 
      }
}
