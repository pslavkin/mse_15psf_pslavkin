#include "sapi.h"

#define LENGTH 512
int16_t adc [ LENGTH ];
uint16_t sample = 0;

int main ( void ) {
   boardConfig       (                          );
   uartConfig        ( UART_USB, 460800         );
   adcConfig         ( ADC_ENABLE               );
   cyclesCounterInit ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample] ,sizeof(adc[0]) );
      adc[sample] = ((int16_t )adcRead(CH1)-512);
      if ( ++sample==LENGTH ) { //22.7hz para 512
         sample = 0;
         uartWriteByteArray ( UART_USB ,"header" ,6 );
         gpioToggle         ( LEDR                  );
      }
   while(cyclesCounterRead()< 20400)  //clk 204000000
      ;
   }
}
