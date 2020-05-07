EESchema Schematic File Version 4
LIBS:acondicionamiento-cache
EELAYER 26 0
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
L acondicionamiento-rescue:R R2
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
L power:GNDA #PWR04
U 1 1 5E9F21FA
P 6000 4250
F 0 "#PWR04" H 6000 4000 50  0001 C CNN
F 1 "GNDA" H 6000 4100 50  0000 C CNN
F 2 "" H 6000 4250 50  0000 C CNN
F 3 "" H 6000 4250 50  0000 C CNN
	1    6000 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 3550 6000 3650
Connection ~ 6000 3650
$Comp
L acondicionamiento-rescue:C C2
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
	6600 3650 6750 3650
Wire Wire Line
	6750 3650 6750 3700
$Comp
L power:GNDA #PWR05
U 1 1 5E9F22FD
P 6750 4250
F 0 "#PWR05" H 6750 4000 50  0001 C CNN
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
L acondicionamiento-rescue:R R1
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
L acondicionamiento-rescue:R R3
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
L acondicionamiento-rescue:C C1
U 1 1 5E9F278E
P 5650 3650
F 0 "C1" V 5800 3600 50  0000 L CNN
F 1 ">1uF" V 5450 3550 50  0000 L CNN
F 2 "" H 5688 3500 50  0000 C CNN
F 3 "" H 5650 3650 50  0000 C CNN
	1    5650 3650
	0    1    1    0   
$EndComp
Text Notes 6150 3250 0    60   ~ 0
fc=1/(2*pi*R*C)
Text Label 6000 3650 0    60   ~ 0
1.65v
$Comp
L acondicionamiento-rescue:D D2
U 1 1 5E9F29FA
P 5300 3500
F 0 "D2" H 5300 3600 50  0000 C CNN
F 1 "D" H 5300 3400 50  0000 C CNN
F 2 "" H 5300 3500 50  0000 C CNN
F 3 "" H 5300 3500 50  0000 C CNN
	1    5300 3500
	0    1    1    0   
$EndComp
$Comp
L acondicionamiento-rescue:D D1
U 1 1 5E9F2A93
P 5300 3200
F 0 "D1" H 5300 3300 50  0000 C CNN
F 1 "D" H 5300 3100 50  0000 C CNN
F 2 "" H 5300 3200 50  0000 C CNN
F 3 "" H 5300 3200 50  0000 C CNN
	1    5300 3200
	0    1    1    0   
$EndComp
$Comp
L acondicionamiento-rescue:D D3
U 1 1 5E9F2C2C
P 5300 3800
F 0 "D3" H 5300 3900 50  0000 C CNN
F 1 "D" H 5300 3700 50  0000 C CNN
F 2 "" H 5300 3800 50  0000 C CNN
F 3 "" H 5300 3800 50  0000 C CNN
	1    5300 3800
	0    -1   -1   0   
$EndComp
$Comp
L acondicionamiento-rescue:D D4
U 1 1 5E9F2C78
P 5300 4100
F 0 "D4" H 5300 4200 50  0000 C CNN
F 1 "D" H 5300 4000 50  0000 C CNN
F 2 "" H 5300 4100 50  0000 C CNN
F 3 "" H 5300 4100 50  0000 C CNN
	1    5300 4100
	0    -1   -1   0   
$EndComp
Connection ~ 5300 3650
Wire Wire Line
	6000 3250 6000 3050
$Comp
L power:GNDA #PWR02
U 1 1 5E9F2E0C
P 5300 4250
F 0 "#PWR02" H 5300 4000 50  0001 C CNN
F 1 "GNDA" H 5305 4077 50  0000 C CNN
F 2 "" H 5300 4250 50  0000 C CNN
F 3 "" H 5300 4250 50  0000 C CNN
	1    5300 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 4000 6000 4250
Wire Wire Line
	6750 4000 6750 4250
Text Notes 5150 4200 1    60   ~ 0
Proteccion\n
Text Notes 5500 3350 0    60   ~ 0
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
Wire Wire Line
	6000 3650 6000 3700
Wire Wire Line
	6000 3650 6300 3650
Wire Wire Line
	6750 3650 7050 3650
Wire Wire Line
	4900 3650 5300 3650
Wire Wire Line
	5300 3650 5500 3650
Wire Wire Line
	5800 3650 6000 3650
$Comp
L power:VDDA #PWR?
U 1 1 5EADD8C7
P 6000 3050
F 0 "#PWR?" H 6000 2900 50  0001 C CNN
F 1 "VDDA" H 6017 3223 50  0000 C CNN
F 2 "" H 6000 3050 50  0001 C CNN
F 3 "" H 6000 3050 50  0001 C CNN
	1    6000 3050
	1    0    0    -1  
$EndComp
$Comp
L power:VDDA #PWR?
U 1 1 5EADD944
P 5300 3050
F 0 "#PWR?" H 5300 2900 50  0001 C CNN
F 1 "VDDA" H 5317 3223 50  0000 C CNN
F 2 "" H 5300 3050 50  0001 C CNN
F 3 "" H 5300 3050 50  0001 C CNN
	1    5300 3050
	1    0    0    -1  
$EndComp
Text Notes 5150 3550 1    60   ~ 0
Proteccion\n
Text Notes 6550 3950 2    60   ~ 0
FAA
$EndSCHEMATC
