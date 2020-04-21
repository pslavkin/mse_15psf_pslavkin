EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R2
U 1 1 5E9F21B2
P 6000 3850
F 0 "R2" H 6150 3800 50  0000 C CNN
F 1 "100k" H 6150 3900 50  0000 C CNN
F 2 "" V 5930 3850 50  0000 C CNN
F 3 "" H 6000 3850 50  0000 C CNN
	1    6000 3850
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR1
U 1 1 5E9F21E0
P 6000 3050
F 0 "#PWR1" H 6000 2900 50  0001 C CNN
F 1 "+3.3V" H 6000 3190 50  0000 C CNN
F 2 "" H 6000 3050 50  0000 C CNN
F 3 "" H 6000 3050 50  0000 C CNN
	1    6000 3050
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR2
U 1 1 5E9F21FA
P 6000 4250
F 0 "#PWR2" H 6000 4000 50  0001 C CNN
F 1 "GNDA" H 6000 4100 50  0000 C CNN
F 2 "" H 6000 4250 50  0000 C CNN
F 3 "" H 6000 4250 50  0000 C CNN
	1    6000 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 3550 6000 3700
Wire Wire Line
	5450 3650 6300 3650
Connection ~ 6000 3650
$Comp
L C C2
U 1 1 5E9F228D
P 6750 3850
F 0 "C2" H 6775 3950 50  0000 L CNN
F 1 "33nF" H 6775 3750 50  0000 L CNN
F 2 "" H 6788 3700 50  0000 C CNN
F 3 "" H 6750 3850 50  0000 C CNN
	1    6750 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 3650 7050 3650
Wire Wire Line
	6750 3650 6750 3700
$Comp
L GNDA #PWR3
U 1 1 5E9F22FD
P 6750 4250
F 0 "#PWR3" H 6750 4000 50  0001 C CNN
F 1 "GNDA" H 6750 4100 50  0000 C CNN
F 2 "" H 6750 4250 50  0000 C CNN
F 3 "" H 6750 4250 50  0000 C CNN
	1    6750 4250
	1    0    0    -1  
$EndComp
Connection ~ 6750 3650
Text HLabel 7050 3650 2    60   Input ~ 0
ADC1
Text HLabel 4900 3650 0    60   Input ~ 0
Audio
Text Notes 4550 3550 0    60   ~ 0
+-1Vac
Text Notes 7150 3850 0    60   ~ 0
0-3.3Vdc\n
$Comp
L R R1
U 1 1 5E9F2549
P 6000 3400
F 0 "R1" H 6150 3350 50  0000 C CNN
F 1 "100k" H 6150 3450 50  0000 C CNN
F 2 "" V 5930 3400 50  0000 C CNN
F 3 "" H 6000 3400 50  0000 C CNN
	1    6000 3400
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5E9F2580
P 6450 3650
F 0 "R3" V 6350 3650 50  0000 C CNN
F 1 "1k" V 6550 3650 50  0000 C CNN
F 2 "" V 6380 3650 50  0000 C CNN
F 3 "" H 6450 3650 50  0000 C CNN
	1    6450 3650
	0    1    1    0   
$EndComp
Text Notes 4500 3450 0    60   ~ 0
0-100Khz\n
Text Notes 7150 4000 0    60   ~ 0
0-5Khz\n
$Comp
L C C1
U 1 1 5E9F278E
P 5300 3650
F 0 "C1" V 5450 3600 50  0000 L CNN
F 1 ">1uF" V 5100 3550 50  0000 L CNN
F 2 "" H 5338 3500 50  0000 C CNN
F 3 "" H 5300 3650 50  0000 C CNN
	1    5300 3650
	0    1    1    0   
$EndComp
Wire Wire Line
	5150 3650 4900 3650
Text Notes 6150 3250 0    60   ~ 0
fc=1/(2*pi*R*C)
Text Label 6000 3650 0    60   ~ 0
1.65v
$Comp
L D D?
U 1 1 5E9F29FA
P 5600 3500
F 0 "D?" H 5600 3600 50  0000 C CNN
F 1 "D" H 5600 3400 50  0000 C CNN
F 2 "" H 5600 3500 50  0000 C CNN
F 3 "" H 5600 3500 50  0000 C CNN
	1    5600 3500
	0    1    1    0   
$EndComp
$Comp
L D D?
U 1 1 5E9F2A93
P 5600 3200
F 0 "D?" H 5600 3300 50  0000 C CNN
F 1 "D" H 5600 3100 50  0000 C CNN
F 2 "" H 5600 3200 50  0000 C CNN
F 3 "" H 5600 3200 50  0000 C CNN
	1    5600 3200
	0    1    1    0   
$EndComp
$Comp
L D D?
U 1 1 5E9F2C2C
P 5600 3800
F 0 "D?" H 5600 3900 50  0000 C CNN
F 1 "D" H 5600 3700 50  0000 C CNN
F 2 "" H 5600 3800 50  0000 C CNN
F 3 "" H 5600 3800 50  0000 C CNN
	1    5600 3800
	0    -1   -1   0   
$EndComp
$Comp
L D D?
U 1 1 5E9F2C78
P 5600 4100
F 0 "D?" H 5600 4200 50  0000 C CNN
F 1 "D" H 5600 4000 50  0000 C CNN
F 2 "" H 5600 4100 50  0000 C CNN
F 3 "" H 5600 4100 50  0000 C CNN
	1    5600 4100
	0    -1   -1   0   
$EndComp
Connection ~ 5600 3650
$Comp
L +3.3V #PWR?
U 1 1 5E9F2D56
P 5600 3050
F 0 "#PWR?" H 5600 2900 50  0001 C CNN
F 1 "+3.3V" H 5600 3190 50  0000 C CNN
F 2 "" H 5600 3050 50  0000 C CNN
F 3 "" H 5600 3050 50  0000 C CNN
	1    5600 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 3250 6000 3050
$Comp
L GNDA #PWR?
U 1 1 5E9F2E0C
P 5600 4250
F 0 "#PWR?" H 5600 4000 50  0001 C CNN
F 1 "GNDA" H 5600 4100 50  0000 C CNN
F 2 "" H 5600 4250 50  0000 C CNN
F 3 "" H 5600 4250 50  0000 C CNN
	1    5600 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 4000 6000 4250
Wire Wire Line
	6750 4000 6750 4250
Text Notes 5450 4350 1    60   ~ 0
Proteccion\n
Text Notes 5050 3350 0    60   ~ 0
Desacple
Wire Notes Line
	4200 3050 4200 4200
Wire Notes Line
	4200 4200 5000 4200
Wire Notes Line
	5000 4200 5000 3050
Wire Notes Line
	5000 3050 4200 3050
Text Notes 4250 3150 0    60   ~ 0
PC/Mobil/etc
Wire Notes Line
	6950 3050 6950 4200
Wire Notes Line
	6950 4200 7700 4200
Wire Notes Line
	7700 4200 7700 3050
Wire Notes Line
	7700 3050 6950 3050
Text Notes 7250 3150 0    60   ~ 0
CIAA
$EndSCHEMATC
