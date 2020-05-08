#include "sapi.h"
#include "arm_math.h"

#define LENGTH 512
#define FS     10000
int16_t  adc[ LENGTH ];
uint16_t sample             = 0;
uint32_t maxIndex,minIndex  = 0;
q15_t maxValue,minValue,rms = 0;

int main ( void ) {
   boardConfig ( );
   uartConfig ( UART_USB ,460800 );
   adcConfig ( ADC_ENABLE );
   dacConfig ( DAC_ENABLE );
   cyclesCounterInit ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample] ,sizeof(adc[0]) );
      adc[sample] = ((adcRead(CH1)-512)>>6)<<12;
      if ( ++sample==LENGTH ) {
         arm_max_q15 ( adc, LENGTH, &maxValue,&maxIndex );
         arm_min_q15 ( adc, LENGTH, &minValue,&minIndex );
         arm_rms_q15 ( adc, LENGTH, &rms                );
         uartWriteByteArray ( UART_USB ,(uint8_t* )&maxValue ,2 );
         uartWriteByteArray ( UART_USB ,(uint8_t* )&minValue ,2 );
         uartWriteByteArray ( UART_USB ,(uint8_t* )&rms      ,2 );
         sample = 0;
         uartWriteByteArray ( UART_USB ,"header" ,6 );
         gpioToggle ( LEDG );
      }
      while(cyclesCounterRead()< EDU_CIAA_NXP_CLOCK_SPEED/FS)  //clk 204000000
         ;
   }
}
