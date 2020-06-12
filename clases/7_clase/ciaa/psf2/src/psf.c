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
#define fs                 1000
#define INTERPOL_WIDTH     10
#define MAX_FFT_LENGTH     2048
#define CONVOLUTION_LENGTH 2048
int16_t fftLength = 128;
int16_t hLength   = h_LENGTH;
int16_t adc  [ MAX_FFT_LENGTH];
q15_t x      [ MAX_FFT_LENGTH]        ;
q15_t fftOut [ MAX_FFT_LENGTH+2 ]  ;
q15_t fftMag [ MAX_FFT_LENGTH ];
q15_t fftPromMag [ MAX_FFT_LENGTH ]={0};

uint32_t maxIndex   = 0;
uint16_t maxPromIndex    = 0;
uint32_t magIndex   = 0;
q15_t maxValue      = 0;
arm_rfft_instance_q15 S;
uint16_t convLength = CONVOLUTION_LENGTH;
uint16_t sample     = 0;

int calcFftLength(int N,int M) {
   int convLength=N+M-1,i;
   for(i=MAX_FFT_LENGTH;i>=convLength;i>>=1)
      ;
   return i<<1;
}
int sendStr(char A[],int N) { uartWriteByteArray ( UART_USB ,A ,N ); }
int sendBlock(q15_t A[],int N) { uartWriteByteArray ( UART_USB ,(uint8_t* )A ,2*N ); }
void findFirstLocalMax(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex);
void interpol(q15_t* magFft,uint16_t* maxIndex);
void promVector(q15_t* promMagFft,q15_t* magFft,uint16_t length);


int main ( void ) {
   boardConfig        (                          );
   uartConfig         ( UART_USB, 460800         );
   adcConfig          ( ADC_ENABLE               );
   cyclesCounterInit  ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample]    ,sizeof(adc[0]) );// envia el sample ANTERIOR
      uartWriteByteArray ( UART_USB ,(uint8_t* )&fftPromMag[magIndex-fftLength/2+sample] ,sizeof(fftOut[0])); // envia la fft del sample ANTERIO
      adc[sample] = ((int16_t )adcRead(CH1)-512)<<6;
      if ( ++sample==fftLength ) {                                                   // si es el ultimo
         sendBlock ( &maxValue  ,1 );
         sendBlock ( (q15_t* )&maxIndex ,1 );
         sendBlock ( (q15_t* )&maxPromIndex ,1 );
         for(;sample<convLength;sample++)
            adc[sample]=0;
         sample = 0;                                                                 // arranca de nuevo
         sendStr   ( "header"   ,6    );
         arm_conv_fast_q15 ( adc,fftLength,h,convLength-fftLength+1,x );
         arm_rfft_init_q15 ( &S ,convLength ,0 ,1 );
         arm_rfft_q15      ( &S ,x     ,fftOut    );
         for(int i=0;i<(convLength+2);i++){
            fftOut[i]<<=5;
         }
         arm_cmplx_mag_squared_q15 ( fftOut ,fftMag ,convLength/2+1               );
         promVector(fftPromMag,fftMag,convLength/2);
         arm_max_q15               ( fftPromMag ,convLength/2+1 ,&maxValue ,&maxIndex );
         findFirstLocalMax(fftPromMag,convLength/2,maxValue/10,&maxValue ,&maxIndex);
         maxPromIndex=maxIndex;
         interpol(fftPromMag,&maxPromIndex);
         magIndex=maxIndex>=(fftLength/2)?maxIndex:(fftLength/2);
         gpioToggle( LEDB);
      }
      while(cyclesCounterRead()< 204000)
         ;
   }
}
void findFirstLocalMax(q15_t* magFft,int length,q15_t threshold,q15_t* maxValue,uint32_t* maxIndex)
{
   int i=(convLength*60)/fs;
   *maxValue=0;
   *maxIndex=0;
   length-=INTERPOL_WIDTH; //para interpol
   if(threshold<5) threshold=5;
   for (;i<length;i++)
      if(magFft[i]>threshold) 
         break;
   if(i>=length) return;
   for (;i<length;i++)
      if(magFft[i]>=*maxValue) {
            *maxValue=magFft[i];
            *maxIndex=i;
      }
      else
         break;
}
void interpol(q15_t* magFft,uint16_t* maxIndex)
{
   q15_t interpolF [ 2*INTERPOL_WIDTH+1 ];
   uint32_t f=0;
   uint32_t sum=0;

   for (int i=0;i<(2*INTERPOL_WIDTH+1);i++) {
      interpolF[i]=magFft[*maxIndex-INTERPOL_WIDTH+i];
      sum+=interpolF[i];
      f += interpolF[i]*(*maxIndex-INTERPOL_WIDTH+i);
   }
   *maxIndex=(f*20)/sum;
}
void promVector(q15_t* promMagFft,q15_t* magFft,uint16_t length)
{
   for (int i=0;i<length;i++)
      promMagFft[i]=(promMagFft[i]+magFft[i])/2;
}
