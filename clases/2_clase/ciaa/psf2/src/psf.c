#include "sapi.h"
#include "arm_math.h"

#define LENGTH 512
#define FS     10000
int16_t  adc[ LENGTH ];
uint16_t sample = 0   ;
uint32_t tick   = 0   ;
uint16_t f      = 100 ;
uint16_t B      = 5000;
uint16_t sweept = 1;
float t         = 0;

int main ( void ) {
   boardConfig ( );
   uartConfig ( UART_USB ,460800 );
   adcConfig ( ADC_ENABLE );
   dacConfig ( DAC_ENABLE );
   cyclesCounterInit ( EDU_CIAA_NXP_CLOCK_SPEED );
   while(1) {
      cyclesCounterReset();
      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample] ,sizeof(adc[0]) );
      adc[sample] = adcRead(CH1)-512;
      t=((tick%(sweept*FS))/(float)FS);
      //dacWrite( DAC, 512*arm_sin_f32 (t*B*(t/sweept)*2*PI)+512); //sweept
      dacWrite( DAC, 512*arm_sin_f32 (t*f*2*PI)+512); //tono
      if ( ++sample==LENGTH ) {
         sample = 0;
         uartWriteByteArray ( UART_USB ,"header" ,6 );
         gpioToggle ( LEDG );
      }
      tick++;
      while(cyclesCounterRead()< EDU_CIAA_NXP_CLOCK_SPEED/FS)  //clk 204000000
         ;
   }
}
