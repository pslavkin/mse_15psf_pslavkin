// Inclusiones
#include <stdio.h>
#include <stdlib.h>

#include "sapi.h"
#include "arm_math.h"

#define LENGTH 512
#define FS 10000
#define BITS 2

//#define BITS 2 digitalizar con 2
//#define BITS 6 digitalizar con 4
//#define BITS 8 digitalizar con 8
//#define BITS 10 digitalizar con 10

int16_t adc  [ LENGTH];
int16_t dac;
int16_t error;
uint16_t sample = 0;
uint32_t tick   = 0;
uint16_t f      = 440;
float t         = 0;
float32_t  tono = 0;
float32_t  tono2 = 0;
int16_t t1         = 0;


int16_t muestra_original      = 0;
uint32_t maxIndex, minIndex   = 0;
q15_t maxValue, minValue, rms = 0;

int main(void) {
   boardConfig       (                          );
   uartConfig        ( UART_USB, 460800         );
   adcConfig         ( ADC_ENABLE               );
   dacConfig         ( DAC_ENABLE               );
   cyclesCounterInit ( EDU_CIAA_NXP_CLOCK_SPEED );

   while (1) {
      cyclesCounterReset();

      dac = abs((tick % 1024) - 512);

      if (dac>=512)
         dac=511;                                                              // el rango va de -512 a 511
      dacWrite(DAC, dac+512);                                                  // escribe el dato + 512, va de 0 a 1023
                                                                               // adc[sample] = ((adcRead(CH1)+(1024/(1<<BITS))/2)>>(10-BITS)<<(10-BITS))-512; //analizar
                                                                               // esta opcion como redondeo
      adc[sample] = (adcRead(CH1)>>(10-BITS)<<(10-BITS))-512;                  // elimino bits
      error = dac-adc[sample];                                                 // calculo diferencia

      uartWriteByteArray ( UART_USB ,(uint8_t* )&adc[sample] ,sizeof(adc[0])); // envio el adc capturado
      uartWriteByteArray ( UART_USB ,(uint8_t* )&dac         ,sizeof(dac))  ;  // envio el dac como referencia
      uartWriteByteArray ( UART_USB ,(uint8_t* )&error       ,sizeof(error));  // envio TODOS los erorres entre el dac y el adc


      if (++sample == LENGTH) {
         sample = 0;
         arm_max_q15(adc, LENGTH, &maxValue, &maxIndex);
         arm_min_q15(adc, LENGTH, &minValue, &minIndex);
         arm_rms_q15(adc, LENGTH, &rms);
         uartWriteByteArray(UART_USB, (uint8_t*) &maxValue, 2);
         uartWriteByteArray(UART_USB, (uint8_t*) &minValue, 2);
         uartWriteByteArray(UART_USB, (uint8_t*) &rms, 2);
         uartWriteByteArray(UART_USB, "header", 6);
         gpioToggle(LEDG);
      }

      tick++;
      while (
         cyclesCounterRead()< EDU_CIAA_NXP_CLOCK_SPEED/FS); //clk204000000;
   }
}

