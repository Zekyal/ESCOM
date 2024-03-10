
;CodeVisionAVR C Compiler V2.05.0 Professional
;(C) Copyright 1998-2010 Pavel Haiduc, HP InfoTech s.r.l.
;http://www.hpinfotech.com

;Chip type                : ATmega8535
;Program type             : Application
;Clock frequency          : 1.000000 MHz
;Memory model             : Small
;Optimize for             : Size
;(s)printf features       : int, width
;(s)scanf features        : int, width
;External RAM size        : 0
;Data Stack size          : 128 byte(s)
;Heap size                : 0 byte(s)
;Promote 'char' to 'int'  : Yes
;'char' is unsigned       : Yes
;8 bit enums              : Yes
;global 'const' stored in FLASH: No
;Enhanced core instructions    : On
;Smart register allocation     : On
;Automatic register allocation : On

	#pragma AVRPART ADMIN PART_NAME ATmega8535
	#pragma AVRPART MEMORY PROG_FLASH 8192
	#pragma AVRPART MEMORY EEPROM 512
	#pragma AVRPART MEMORY INT_SRAM SIZE 607
	#pragma AVRPART MEMORY INT_SRAM START_ADDR 0x60

	.LISTMAC
	.EQU UDRE=0x5
	.EQU RXC=0x7
	.EQU USR=0xB
	.EQU UDR=0xC
	.EQU SPSR=0xE
	.EQU SPDR=0xF
	.EQU EERE=0x0
	.EQU EEWE=0x1
	.EQU EEMWE=0x2
	.EQU EECR=0x1C
	.EQU EEDR=0x1D
	.EQU EEARL=0x1E
	.EQU EEARH=0x1F
	.EQU WDTCR=0x21
	.EQU MCUCR=0x35
	.EQU GICR=0x3B
	.EQU SPL=0x3D
	.EQU SPH=0x3E
	.EQU SREG=0x3F

	.DEF R0X0=R0
	.DEF R0X1=R1
	.DEF R0X2=R2
	.DEF R0X3=R3
	.DEF R0X4=R4
	.DEF R0X5=R5
	.DEF R0X6=R6
	.DEF R0X7=R7
	.DEF R0X8=R8
	.DEF R0X9=R9
	.DEF R0XA=R10
	.DEF R0XB=R11
	.DEF R0XC=R12
	.DEF R0XD=R13
	.DEF R0XE=R14
	.DEF R0XF=R15
	.DEF R0X10=R16
	.DEF R0X11=R17
	.DEF R0X12=R18
	.DEF R0X13=R19
	.DEF R0X14=R20
	.DEF R0X15=R21
	.DEF R0X16=R22
	.DEF R0X17=R23
	.DEF R0X18=R24
	.DEF R0X19=R25
	.DEF R0X1A=R26
	.DEF R0X1B=R27
	.DEF R0X1C=R28
	.DEF R0X1D=R29
	.DEF R0X1E=R30
	.DEF R0X1F=R31

	.EQU __SRAM_START=0x0060
	.EQU __SRAM_END=0x025F
	.EQU __DSTACK_SIZE=0x0080
	.EQU __HEAP_SIZE=0x0000
	.EQU __CLEAR_SRAM_SIZE=__SRAM_END-__SRAM_START+1

	.MACRO __CPD1N
	CPI  R30,LOW(@0)
	LDI  R26,HIGH(@0)
	CPC  R31,R26
	LDI  R26,BYTE3(@0)
	CPC  R22,R26
	LDI  R26,BYTE4(@0)
	CPC  R23,R26
	.ENDM

	.MACRO __CPD2N
	CPI  R26,LOW(@0)
	LDI  R30,HIGH(@0)
	CPC  R27,R30
	LDI  R30,BYTE3(@0)
	CPC  R24,R30
	LDI  R30,BYTE4(@0)
	CPC  R25,R30
	.ENDM

	.MACRO __CPWRR
	CP   R@0,R@2
	CPC  R@1,R@3
	.ENDM

	.MACRO __CPWRN
	CPI  R@0,LOW(@2)
	LDI  R30,HIGH(@2)
	CPC  R@1,R30
	.ENDM

	.MACRO __ADDB1MN
	SUBI R30,LOW(-@0-(@1))
	.ENDM

	.MACRO __ADDB2MN
	SUBI R26,LOW(-@0-(@1))
	.ENDM

	.MACRO __ADDW1MN
	SUBI R30,LOW(-@0-(@1))
	SBCI R31,HIGH(-@0-(@1))
	.ENDM

	.MACRO __ADDW2MN
	SUBI R26,LOW(-@0-(@1))
	SBCI R27,HIGH(-@0-(@1))
	.ENDM

	.MACRO __ADDW1FN
	SUBI R30,LOW(-2*@0-(@1))
	SBCI R31,HIGH(-2*@0-(@1))
	.ENDM

	.MACRO __ADDD1FN
	SUBI R30,LOW(-2*@0-(@1))
	SBCI R31,HIGH(-2*@0-(@1))
	SBCI R22,BYTE3(-2*@0-(@1))
	.ENDM

	.MACRO __ADDD1N
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	SBCI R22,BYTE3(-@0)
	SBCI R23,BYTE4(-@0)
	.ENDM

	.MACRO __ADDD2N
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	SBCI R24,BYTE3(-@0)
	SBCI R25,BYTE4(-@0)
	.ENDM

	.MACRO __SUBD1N
	SUBI R30,LOW(@0)
	SBCI R31,HIGH(@0)
	SBCI R22,BYTE3(@0)
	SBCI R23,BYTE4(@0)
	.ENDM

	.MACRO __SUBD2N
	SUBI R26,LOW(@0)
	SBCI R27,HIGH(@0)
	SBCI R24,BYTE3(@0)
	SBCI R25,BYTE4(@0)
	.ENDM

	.MACRO __ANDBMNN
	LDS  R30,@0+(@1)
	ANDI R30,LOW(@2)
	STS  @0+(@1),R30
	.ENDM

	.MACRO __ANDWMNN
	LDS  R30,@0+(@1)
	ANDI R30,LOW(@2)
	STS  @0+(@1),R30
	LDS  R30,@0+(@1)+1
	ANDI R30,HIGH(@2)
	STS  @0+(@1)+1,R30
	.ENDM

	.MACRO __ANDD1N
	ANDI R30,LOW(@0)
	ANDI R31,HIGH(@0)
	ANDI R22,BYTE3(@0)
	ANDI R23,BYTE4(@0)
	.ENDM

	.MACRO __ANDD2N
	ANDI R26,LOW(@0)
	ANDI R27,HIGH(@0)
	ANDI R24,BYTE3(@0)
	ANDI R25,BYTE4(@0)
	.ENDM

	.MACRO __ORBMNN
	LDS  R30,@0+(@1)
	ORI  R30,LOW(@2)
	STS  @0+(@1),R30
	.ENDM

	.MACRO __ORWMNN
	LDS  R30,@0+(@1)
	ORI  R30,LOW(@2)
	STS  @0+(@1),R30
	LDS  R30,@0+(@1)+1
	ORI  R30,HIGH(@2)
	STS  @0+(@1)+1,R30
	.ENDM

	.MACRO __ORD1N
	ORI  R30,LOW(@0)
	ORI  R31,HIGH(@0)
	ORI  R22,BYTE3(@0)
	ORI  R23,BYTE4(@0)
	.ENDM

	.MACRO __ORD2N
	ORI  R26,LOW(@0)
	ORI  R27,HIGH(@0)
	ORI  R24,BYTE3(@0)
	ORI  R25,BYTE4(@0)
	.ENDM

	.MACRO __DELAY_USB
	LDI  R24,LOW(@0)
__DELAY_USB_LOOP:
	DEC  R24
	BRNE __DELAY_USB_LOOP
	.ENDM

	.MACRO __DELAY_USW
	LDI  R24,LOW(@0)
	LDI  R25,HIGH(@0)
__DELAY_USW_LOOP:
	SBIW R24,1
	BRNE __DELAY_USW_LOOP
	.ENDM

	.MACRO __GETD1S
	LDD  R30,Y+@0
	LDD  R31,Y+@0+1
	LDD  R22,Y+@0+2
	LDD  R23,Y+@0+3
	.ENDM

	.MACRO __GETD2S
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	LDD  R24,Y+@0+2
	LDD  R25,Y+@0+3
	.ENDM

	.MACRO __PUTD1S
	STD  Y+@0,R30
	STD  Y+@0+1,R31
	STD  Y+@0+2,R22
	STD  Y+@0+3,R23
	.ENDM

	.MACRO __PUTD2S
	STD  Y+@0,R26
	STD  Y+@0+1,R27
	STD  Y+@0+2,R24
	STD  Y+@0+3,R25
	.ENDM

	.MACRO __PUTDZ2
	STD  Z+@0,R26
	STD  Z+@0+1,R27
	STD  Z+@0+2,R24
	STD  Z+@0+3,R25
	.ENDM

	.MACRO __CLRD1S
	STD  Y+@0,R30
	STD  Y+@0+1,R30
	STD  Y+@0+2,R30
	STD  Y+@0+3,R30
	.ENDM

	.MACRO __POINTB1MN
	LDI  R30,LOW(@0+(@1))
	.ENDM

	.MACRO __POINTW1MN
	LDI  R30,LOW(@0+(@1))
	LDI  R31,HIGH(@0+(@1))
	.ENDM

	.MACRO __POINTD1M
	LDI  R30,LOW(@0)
	LDI  R31,HIGH(@0)
	LDI  R22,BYTE3(@0)
	LDI  R23,BYTE4(@0)
	.ENDM

	.MACRO __POINTW1FN
	LDI  R30,LOW(2*@0+(@1))
	LDI  R31,HIGH(2*@0+(@1))
	.ENDM

	.MACRO __POINTD1FN
	LDI  R30,LOW(2*@0+(@1))
	LDI  R31,HIGH(2*@0+(@1))
	LDI  R22,BYTE3(2*@0+(@1))
	LDI  R23,BYTE4(2*@0+(@1))
	.ENDM

	.MACRO __POINTB2MN
	LDI  R26,LOW(@0+(@1))
	.ENDM

	.MACRO __POINTW2MN
	LDI  R26,LOW(@0+(@1))
	LDI  R27,HIGH(@0+(@1))
	.ENDM

	.MACRO __POINTBRM
	LDI  R@0,LOW(@1)
	.ENDM

	.MACRO __POINTWRM
	LDI  R@0,LOW(@2)
	LDI  R@1,HIGH(@2)
	.ENDM

	.MACRO __POINTBRMN
	LDI  R@0,LOW(@1+(@2))
	.ENDM

	.MACRO __POINTWRMN
	LDI  R@0,LOW(@2+(@3))
	LDI  R@1,HIGH(@2+(@3))
	.ENDM

	.MACRO __POINTWRFN
	LDI  R@0,LOW(@2*2+(@3))
	LDI  R@1,HIGH(@2*2+(@3))
	.ENDM

	.MACRO __GETD1N
	LDI  R30,LOW(@0)
	LDI  R31,HIGH(@0)
	LDI  R22,BYTE3(@0)
	LDI  R23,BYTE4(@0)
	.ENDM

	.MACRO __GETD2N
	LDI  R26,LOW(@0)
	LDI  R27,HIGH(@0)
	LDI  R24,BYTE3(@0)
	LDI  R25,BYTE4(@0)
	.ENDM

	.MACRO __GETB1MN
	LDS  R30,@0+(@1)
	.ENDM

	.MACRO __GETB1HMN
	LDS  R31,@0+(@1)
	.ENDM

	.MACRO __GETW1MN
	LDS  R30,@0+(@1)
	LDS  R31,@0+(@1)+1
	.ENDM

	.MACRO __GETD1MN
	LDS  R30,@0+(@1)
	LDS  R31,@0+(@1)+1
	LDS  R22,@0+(@1)+2
	LDS  R23,@0+(@1)+3
	.ENDM

	.MACRO __GETBRMN
	LDS  R@0,@1+(@2)
	.ENDM

	.MACRO __GETWRMN
	LDS  R@0,@2+(@3)
	LDS  R@1,@2+(@3)+1
	.ENDM

	.MACRO __GETWRZ
	LDD  R@0,Z+@2
	LDD  R@1,Z+@2+1
	.ENDM

	.MACRO __GETD2Z
	LDD  R26,Z+@0
	LDD  R27,Z+@0+1
	LDD  R24,Z+@0+2
	LDD  R25,Z+@0+3
	.ENDM

	.MACRO __GETB2MN
	LDS  R26,@0+(@1)
	.ENDM

	.MACRO __GETW2MN
	LDS  R26,@0+(@1)
	LDS  R27,@0+(@1)+1
	.ENDM

	.MACRO __GETD2MN
	LDS  R26,@0+(@1)
	LDS  R27,@0+(@1)+1
	LDS  R24,@0+(@1)+2
	LDS  R25,@0+(@1)+3
	.ENDM

	.MACRO __PUTB1MN
	STS  @0+(@1),R30
	.ENDM

	.MACRO __PUTW1MN
	STS  @0+(@1),R30
	STS  @0+(@1)+1,R31
	.ENDM

	.MACRO __PUTD1MN
	STS  @0+(@1),R30
	STS  @0+(@1)+1,R31
	STS  @0+(@1)+2,R22
	STS  @0+(@1)+3,R23
	.ENDM

	.MACRO __PUTB1EN
	LDI  R26,LOW(@0+(@1))
	LDI  R27,HIGH(@0+(@1))
	RCALL __EEPROMWRB
	.ENDM

	.MACRO __PUTW1EN
	LDI  R26,LOW(@0+(@1))
	LDI  R27,HIGH(@0+(@1))
	RCALL __EEPROMWRW
	.ENDM

	.MACRO __PUTD1EN
	LDI  R26,LOW(@0+(@1))
	LDI  R27,HIGH(@0+(@1))
	RCALL __EEPROMWRD
	.ENDM

	.MACRO __PUTBR0MN
	STS  @0+(@1),R0
	.ENDM

	.MACRO __PUTBMRN
	STS  @0+(@1),R@2
	.ENDM

	.MACRO __PUTWMRN
	STS  @0+(@1),R@2
	STS  @0+(@1)+1,R@3
	.ENDM

	.MACRO __PUTBZR
	STD  Z+@1,R@0
	.ENDM

	.MACRO __PUTWZR
	STD  Z+@2,R@0
	STD  Z+@2+1,R@1
	.ENDM

	.MACRO __GETW1R
	MOV  R30,R@0
	MOV  R31,R@1
	.ENDM

	.MACRO __GETW2R
	MOV  R26,R@0
	MOV  R27,R@1
	.ENDM

	.MACRO __GETWRN
	LDI  R@0,LOW(@2)
	LDI  R@1,HIGH(@2)
	.ENDM

	.MACRO __PUTW1R
	MOV  R@0,R30
	MOV  R@1,R31
	.ENDM

	.MACRO __PUTW2R
	MOV  R@0,R26
	MOV  R@1,R27
	.ENDM

	.MACRO __ADDWRN
	SUBI R@0,LOW(-@2)
	SBCI R@1,HIGH(-@2)
	.ENDM

	.MACRO __ADDWRR
	ADD  R@0,R@2
	ADC  R@1,R@3
	.ENDM

	.MACRO __SUBWRN
	SUBI R@0,LOW(@2)
	SBCI R@1,HIGH(@2)
	.ENDM

	.MACRO __SUBWRR
	SUB  R@0,R@2
	SBC  R@1,R@3
	.ENDM

	.MACRO __ANDWRN
	ANDI R@0,LOW(@2)
	ANDI R@1,HIGH(@2)
	.ENDM

	.MACRO __ANDWRR
	AND  R@0,R@2
	AND  R@1,R@3
	.ENDM

	.MACRO __ORWRN
	ORI  R@0,LOW(@2)
	ORI  R@1,HIGH(@2)
	.ENDM

	.MACRO __ORWRR
	OR   R@0,R@2
	OR   R@1,R@3
	.ENDM

	.MACRO __EORWRR
	EOR  R@0,R@2
	EOR  R@1,R@3
	.ENDM

	.MACRO __GETWRS
	LDD  R@0,Y+@2
	LDD  R@1,Y+@2+1
	.ENDM

	.MACRO __PUTBSR
	STD  Y+@1,R@0
	.ENDM

	.MACRO __PUTWSR
	STD  Y+@2,R@0
	STD  Y+@2+1,R@1
	.ENDM

	.MACRO __MOVEWRR
	MOV  R@0,R@2
	MOV  R@1,R@3
	.ENDM

	.MACRO __INWR
	IN   R@0,@2
	IN   R@1,@2+1
	.ENDM

	.MACRO __OUTWR
	OUT  @2+1,R@1
	OUT  @2,R@0
	.ENDM

	.MACRO __CALL1MN
	LDS  R30,@0+(@1)
	LDS  R31,@0+(@1)+1
	ICALL
	.ENDM

	.MACRO __CALL1FN
	LDI  R30,LOW(2*@0+(@1))
	LDI  R31,HIGH(2*@0+(@1))
	RCALL __GETW1PF
	ICALL
	.ENDM

	.MACRO __CALL2EN
	LDI  R26,LOW(@0+(@1))
	LDI  R27,HIGH(@0+(@1))
	RCALL __EEPROMRDW
	ICALL
	.ENDM

	.MACRO __GETW1STACK
	IN   R26,SPL
	IN   R27,SPH
	ADIW R26,@0+1
	LD   R30,X+
	LD   R31,X
	.ENDM

	.MACRO __GETD1STACK
	IN   R26,SPL
	IN   R27,SPH
	ADIW R26,@0+1
	LD   R30,X+
	LD   R31,X+
	LD   R22,X
	.ENDM

	.MACRO __NBST
	BST  R@0,@1
	IN   R30,SREG
	LDI  R31,0x40
	EOR  R30,R31
	OUT  SREG,R30
	.ENDM


	.MACRO __PUTB1SN
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1SN
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1SN
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1SNS
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	ADIW R26,@1
	ST   X,R30
	.ENDM

	.MACRO __PUTW1SNS
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	ADIW R26,@1
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1SNS
	LDD  R26,Y+@0
	LDD  R27,Y+@0+1
	ADIW R26,@1
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1PMN
	LDS  R26,@0
	LDS  R27,@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1PMN
	LDS  R26,@0
	LDS  R27,@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1PMN
	LDS  R26,@0
	LDS  R27,@0+1
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1PMNS
	LDS  R26,@0
	LDS  R27,@0+1
	ADIW R26,@1
	ST   X,R30
	.ENDM

	.MACRO __PUTW1PMNS
	LDS  R26,@0
	LDS  R27,@0+1
	ADIW R26,@1
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1PMNS
	LDS  R26,@0
	LDS  R27,@0+1
	ADIW R26,@1
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1RN
	MOVW R26,R@0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1RN
	MOVW R26,R@0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1RN
	MOVW R26,R@0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1RNS
	MOVW R26,R@0
	ADIW R26,@1
	ST   X,R30
	.ENDM

	.MACRO __PUTW1RNS
	MOVW R26,R@0
	ADIW R26,@1
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1RNS
	MOVW R26,R@0
	ADIW R26,@1
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1RON
	MOV  R26,R@0
	MOV  R27,R@1
	SUBI R26,LOW(-@2)
	SBCI R27,HIGH(-@2)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1RON
	MOV  R26,R@0
	MOV  R27,R@1
	SUBI R26,LOW(-@2)
	SBCI R27,HIGH(-@2)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1RON
	MOV  R26,R@0
	MOV  R27,R@1
	SUBI R26,LOW(-@2)
	SBCI R27,HIGH(-@2)
	RCALL __PUTDP1
	.ENDM

	.MACRO __PUTB1RONS
	MOV  R26,R@0
	MOV  R27,R@1
	ADIW R26,@2
	ST   X,R30
	.ENDM

	.MACRO __PUTW1RONS
	MOV  R26,R@0
	MOV  R27,R@1
	ADIW R26,@2
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1RONS
	MOV  R26,R@0
	MOV  R27,R@1
	ADIW R26,@2
	RCALL __PUTDP1
	.ENDM


	.MACRO __GETB1SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	LD   R30,Z
	.ENDM

	.MACRO __GETB1HSX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	LD   R31,Z
	.ENDM

	.MACRO __GETW1SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	LD   R0,Z+
	LD   R31,Z
	MOV  R30,R0
	.ENDM

	.MACRO __GETD1SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	LD   R0,Z+
	LD   R1,Z+
	LD   R22,Z+
	LD   R23,Z
	MOVW R30,R0
	.ENDM

	.MACRO __GETB2SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R26,X
	.ENDM

	.MACRO __GETW2SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R0,X+
	LD   R27,X
	MOV  R26,R0
	.ENDM

	.MACRO __GETD2SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R0,X+
	LD   R1,X+
	LD   R24,X+
	LD   R25,X
	MOVW R26,R0
	.ENDM

	.MACRO __GETBRSX
	MOVW R30,R28
	SUBI R30,LOW(-@1)
	SBCI R31,HIGH(-@1)
	LD   R@0,Z
	.ENDM

	.MACRO __GETWRSX
	MOVW R30,R28
	SUBI R30,LOW(-@2)
	SBCI R31,HIGH(-@2)
	LD   R@0,Z+
	LD   R@1,Z
	.ENDM

	.MACRO __GETBRSX2
	MOVW R26,R28
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	LD   R@0,X
	.ENDM

	.MACRO __GETWRSX2
	MOVW R26,R28
	SUBI R26,LOW(-@2)
	SBCI R27,HIGH(-@2)
	LD   R@0,X+
	LD   R@1,X
	.ENDM

	.MACRO __LSLW8SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	LD   R31,Z
	CLR  R30
	.ENDM

	.MACRO __PUTB1SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	ST   X+,R30
	ST   X+,R31
	ST   X+,R22
	ST   X,R23
	.ENDM

	.MACRO __CLRW1SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	ST   X+,R30
	ST   X,R30
	.ENDM

	.MACRO __CLRD1SX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	ST   X+,R30
	ST   X+,R30
	ST   X+,R30
	ST   X,R30
	.ENDM

	.MACRO __PUTB2SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	ST   Z,R26
	.ENDM

	.MACRO __PUTW2SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	ST   Z+,R26
	ST   Z,R27
	.ENDM

	.MACRO __PUTD2SX
	MOVW R30,R28
	SUBI R30,LOW(-@0)
	SBCI R31,HIGH(-@0)
	ST   Z+,R26
	ST   Z+,R27
	ST   Z+,R24
	ST   Z,R25
	.ENDM

	.MACRO __PUTBSRX
	MOVW R30,R28
	SUBI R30,LOW(-@1)
	SBCI R31,HIGH(-@1)
	ST   Z,R@0
	.ENDM

	.MACRO __PUTWSRX
	MOVW R30,R28
	SUBI R30,LOW(-@2)
	SBCI R31,HIGH(-@2)
	ST   Z+,R@0
	ST   Z,R@1
	.ENDM

	.MACRO __PUTB1SNX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R0,X+
	LD   R27,X
	MOV  R26,R0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X,R30
	.ENDM

	.MACRO __PUTW1SNX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R0,X+
	LD   R27,X
	MOV  R26,R0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X+,R30
	ST   X,R31
	.ENDM

	.MACRO __PUTD1SNX
	MOVW R26,R28
	SUBI R26,LOW(-@0)
	SBCI R27,HIGH(-@0)
	LD   R0,X+
	LD   R27,X
	MOV  R26,R0
	SUBI R26,LOW(-@1)
	SBCI R27,HIGH(-@1)
	ST   X+,R30
	ST   X+,R31
	ST   X+,R22
	ST   X,R23
	.ENDM

	.MACRO __MULBRR
	MULS R@0,R@1
	MOVW R30,R0
	.ENDM

	.MACRO __MULBRRU
	MUL  R@0,R@1
	MOVW R30,R0
	.ENDM

	.MACRO __MULBRR0
	MULS R@0,R@1
	.ENDM

	.MACRO __MULBRRU0
	MUL  R@0,R@1
	.ENDM

	.MACRO __MULBNWRU
	LDI  R26,@2
	MUL  R26,R@0
	MOVW R30,R0
	MUL  R26,R@1
	ADD  R31,R0
	.ENDM

;NAME DEFINITIONS FOR GLOBAL VARIABLES ALLOCATED TO REGISTERS
	.DEF _rand=R4
	.DEF _cont1=R6
	.DEF _cont2=R8
	.DEF _puntos1=R10
	.DEF _puntos2=R12

	.CSEG
	.ORG 0x00

;START OF CODE MARKER
__START_OF_CODE:

;INTERRUPT VECTORS
	RJMP __RESET
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00
	RJMP 0x00

_0x3:
	.DB  0x40,0x79,0x24,0x30,0x19,0x12,0x2,0x78
	.DB  0x0,0x10,0xC0,0xCF,0xA4,0x86,0x8B,0x92
	.DB  0x90,0xC7,0x80,0x82

__GLOBAL_INI_TBL:
	.DW  0x14
	.DW  _tabla7segmentos
	.DW  _0x3*2

_0xFFFFFFFF:
	.DW  0

__RESET:
	CLI
	CLR  R30
	OUT  EECR,R30

;INTERRUPT VECTORS ARE PLACED
;AT THE START OF FLASH
	LDI  R31,1
	OUT  GICR,R31
	OUT  GICR,R30
	OUT  MCUCR,R30

;DISABLE WATCHDOG
	LDI  R31,0x18
	OUT  WDTCR,R31
	OUT  WDTCR,R30

;CLEAR R2-R14
	LDI  R24,(14-2)+1
	LDI  R26,2
	CLR  R27
__CLEAR_REG:
	ST   X+,R30
	DEC  R24
	BRNE __CLEAR_REG

;CLEAR SRAM
	LDI  R24,LOW(__CLEAR_SRAM_SIZE)
	LDI  R25,HIGH(__CLEAR_SRAM_SIZE)
	LDI  R26,__SRAM_START
__CLEAR_SRAM:
	ST   X+,R30
	SBIW R24,1
	BRNE __CLEAR_SRAM

;GLOBAL VARIABLES INITIALIZATION
	LDI  R30,LOW(__GLOBAL_INI_TBL*2)
	LDI  R31,HIGH(__GLOBAL_INI_TBL*2)
__GLOBAL_INI_NEXT:
	LPM  R24,Z+
	LPM  R25,Z+
	SBIW R24,0
	BREQ __GLOBAL_INI_END
	LPM  R26,Z+
	LPM  R27,Z+
	LPM  R0,Z+
	LPM  R1,Z+
	MOVW R22,R30
	MOVW R30,R0
__GLOBAL_INI_LOOP:
	LPM  R0,Z+
	ST   X+,R0
	SBIW R24,1
	BRNE __GLOBAL_INI_LOOP
	MOVW R30,R22
	RJMP __GLOBAL_INI_NEXT
__GLOBAL_INI_END:

;HARDWARE STACK POINTER INITIALIZATION
	LDI  R30,LOW(__SRAM_END-__HEAP_SIZE)
	OUT  SPL,R30
	LDI  R30,HIGH(__SRAM_END-__HEAP_SIZE)
	OUT  SPH,R30

;DATA STACK POINTER INITIALIZATION
	LDI  R28,LOW(__SRAM_START+__DSTACK_SIZE)
	LDI  R29,HIGH(__SRAM_START+__DSTACK_SIZE)

	RJMP _main

	.ESEG
	.ORG 0

	.DSEG
	.ORG 0xE0

	.CSEG
;/*****************************************************
;This program was produced by the
;CodeWizardAVR V2.05.0 Professional
;Automatic Program Generator
;© Copyright 1998-2010 Pavel Haiduc, HP InfoTech s.r.l.
;http://www.hpinfotech.com
;
;Project :
;Version :
;Date    : 24/01/2021
;Author  : NeVaDa
;Company :
;Comments:
;
;
;Chip type               : ATmega8535
;Program type            : Application
;AVR Core Clock frequency: 1.000000 MHz
;Memory model            : Small
;External RAM size       : 0
;Data Stack size         : 128
;*****************************************************/
;
;#include <mega8535.h>
	#ifndef __SLEEP_DEFINED__
	#define __SLEEP_DEFINED__
	.EQU __se_bit=0x40
	.EQU __sm_mask=0xB0
	.EQU __sm_powerdown=0x20
	.EQU __sm_powersave=0x30
	.EQU __sm_standby=0xA0
	.EQU __sm_ext_standby=0xB0
	.EQU __sm_adc_noise_red=0x10
	.SET power_ctrl_reg=mcucr
	#endif
;#include <delay.h>
;#define izquierda1 PINB.1
;#define derecha1 PINB.2
;#define izquierda2 PINB.3
;#define derecha2 PINB.4
;
;eeprom short random;
;eeprom short barra1;
;eeprom short barra2;
;int rand;
;int cont1,cont2;
;int puntos1,puntos2;
;int i,j;
;int x,y;
;int direccion, dsplz, stay, cols, inst, win, rapidez;
;const char tabla7segmentos[2][10]={
;{0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x00,0x10},
;{0xc0,0xcf,0xa4,0x86,0x8b,0x92,0x90,0xc7,0x80,0x82}
;};

	.DSEG
;
;void main(void)
; 0000 002E {

	.CSEG
_main:
; 0000 002F // Declare your local variables here
; 0000 0030 
; 0000 0031 // Input/Output Ports initialization
; 0000 0032 // Port A initialization
; 0000 0033 // Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out
; 0000 0034 // State7=0 State6=1 State5=0 State4=0 State3=0 State2=0 State1=0 State0=0
; 0000 0035 PORTA=0x40;
	LDI  R30,LOW(64)
	OUT  0x1B,R30
; 0000 0036 DDRA=0xFF;
	LDI  R30,LOW(255)
	OUT  0x1A,R30
; 0000 0037 
; 0000 0038 // Port B initialization
; 0000 0039 // Func7=Out Func6=In Func5=In Func4=In Func3=In Func2=In Func1=In Func0=Out
; 0000 003A // State7=1 State6=P State5=P State4=P State3=P State2=P State1=P State0=1
; 0000 003B PORTB=0xFF;
	OUT  0x18,R30
; 0000 003C DDRB=0x81;
	LDI  R30,LOW(129)
	OUT  0x17,R30
; 0000 003D 
; 0000 003E // Port C initialization
; 0000 003F // Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out
; 0000 0040 // State7=0 State6=1 State5=1 State4=0 State3=0 State2=0 State1=0 State0=0
; 0000 0041 PORTC=0x60;
	LDI  R30,LOW(96)
	OUT  0x15,R30
; 0000 0042 DDRC=0xFF;
	LDI  R30,LOW(255)
	OUT  0x14,R30
; 0000 0043 
; 0000 0044 // Port D initialization
; 0000 0045 // Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=In Func1=Out Func0=Out
; 0000 0046 // State7=1 State6=1 State5=1 State4=1 State3=1 State2=P State1=1 State0=1
; 0000 0047 PORTD=0xFF;
	OUT  0x12,R30
; 0000 0048 DDRD=0xFB;
	LDI  R30,LOW(251)
	OUT  0x11,R30
; 0000 0049 
; 0000 004A // Timer/Counter 0 initialization
; 0000 004B // Clock source: System Clock
; 0000 004C // Clock value: Timer 0 Stopped
; 0000 004D // Mode: Normal top=0xFF
; 0000 004E // OC0 output: Disconnected
; 0000 004F TCCR0=0x00;
	LDI  R30,LOW(0)
	OUT  0x33,R30
; 0000 0050 TCNT0=0x00;
	OUT  0x32,R30
; 0000 0051 OCR0=0x00;
	OUT  0x3C,R30
; 0000 0052 
; 0000 0053 // Timer/Counter 1 initialization
; 0000 0054 // Clock source: System Clock
; 0000 0055 // Clock value: Timer1 Stopped
; 0000 0056 // Mode: Normal top=0xFFFF
; 0000 0057 // OC1A output: Discon.
; 0000 0058 // OC1B output: Discon.
; 0000 0059 // Noise Canceler: Off
; 0000 005A // Input Capture on Falling Edge
; 0000 005B // Timer1 Overflow Interrupt: Off
; 0000 005C // Input Capture Interrupt: Off
; 0000 005D // Compare A Match Interrupt: Off
; 0000 005E // Compare B Match Interrupt: Off
; 0000 005F TCCR1A=0x00;
	OUT  0x2F,R30
; 0000 0060 TCCR1B=0x00;
	OUT  0x2E,R30
; 0000 0061 TCNT1H=0x00;
	OUT  0x2D,R30
; 0000 0062 TCNT1L=0x00;
	OUT  0x2C,R30
; 0000 0063 ICR1H=0x00;
	OUT  0x27,R30
; 0000 0064 ICR1L=0x00;
	OUT  0x26,R30
; 0000 0065 OCR1AH=0x00;
	OUT  0x2B,R30
; 0000 0066 OCR1AL=0x00;
	OUT  0x2A,R30
; 0000 0067 OCR1BH=0x00;
	OUT  0x29,R30
; 0000 0068 OCR1BL=0x00;
	OUT  0x28,R30
; 0000 0069 
; 0000 006A // Timer/Counter 2 initialization
; 0000 006B // Clock source: System Clock
; 0000 006C // Clock value: Timer2 Stopped
; 0000 006D // Mode: Normal top=0xFF
; 0000 006E // OC2 output: Disconnected
; 0000 006F ASSR=0x00;
	OUT  0x22,R30
; 0000 0070 TCCR2=0x00;
	OUT  0x25,R30
; 0000 0071 TCNT2=0x00;
	OUT  0x24,R30
; 0000 0072 OCR2=0x00;
	OUT  0x23,R30
; 0000 0073 
; 0000 0074 // External Interrupt(s) initialization
; 0000 0075 // INT0: On
; 0000 0076 // INT0 Mode: Falling Edge
; 0000 0077 // INT1: Off
; 0000 0078 // INT2: On
; 0000 0079 // INT2 Mode: Falling Edge
; 0000 007A GICR|=0x60;
	IN   R30,0x3B
	ORI  R30,LOW(0x60)
	OUT  0x3B,R30
; 0000 007B MCUCR=0x02;
	LDI  R30,LOW(2)
	OUT  0x35,R30
; 0000 007C MCUCSR=0x00;
	LDI  R30,LOW(0)
	OUT  0x34,R30
; 0000 007D GIFR=0x60;
	LDI  R30,LOW(96)
	OUT  0x3A,R30
; 0000 007E 
; 0000 007F // Timer(s)/Counter(s) Interrupt(s) initialization
; 0000 0080 TIMSK=0x00;
	LDI  R30,LOW(0)
	OUT  0x39,R30
; 0000 0081 
; 0000 0082 // USART initialization
; 0000 0083 // USART disabled
; 0000 0084 UCSRB=0x00;
	OUT  0xA,R30
; 0000 0085 
; 0000 0086 // Analog Comparator initialization
; 0000 0087 // Analog Comparator: Off
; 0000 0088 // Analog Comparator Input Capture by Timer/Counter 1: Off
; 0000 0089 ACSR=0x80;
	LDI  R30,LOW(128)
	OUT  0x8,R30
; 0000 008A SFIOR=0x00;
	LDI  R30,LOW(0)
	OUT  0x30,R30
; 0000 008B 
; 0000 008C // ADC initialization
; 0000 008D // ADC disabled
; 0000 008E ADCSRA=0x00;
	OUT  0x6,R30
; 0000 008F 
; 0000 0090 // SPI initialization
; 0000 0091 // SPI disabled
; 0000 0092 SPCR=0x00;
	OUT  0xD,R30
; 0000 0093 
; 0000 0094 // TWI initialization
; 0000 0095 // TWI disabled
; 0000 0096 TWCR=0x00;
	OUT  0x36,R30
; 0000 0097 
; 0000 0098 // Global enable interrupts
; 0000 0099 #asm("sei")
	sei
; 0000 009A if(random<1){
	RCALL SUBOPT_0x0
	RCALL __EEPROMRDW
	SBIW R30,1
	BRGE _0x4
; 0000 009B     random=1;
	RCALL SUBOPT_0x0
	RCALL SUBOPT_0x1
	RCALL __EEPROMWRW
; 0000 009C }
; 0000 009D 
; 0000 009E //multiplicar por numero primo
; 0000 009F random=(random*7)+2;
_0x4:
	RCALL SUBOPT_0x0
	RCALL __EEPROMRDW
	RCALL SUBOPT_0x2
	ADIW R30,2
	RCALL SUBOPT_0x3
; 0000 00A0 random=random%17;
	MOVW R26,R30
	LDI  R30,LOW(17)
	LDI  R31,HIGH(17)
	RCALL __MODW21
	RCALL SUBOPT_0x3
; 0000 00A1 
; 0000 00A2 //definir direccion
; 0000 00A3 rand=(int)random;
	MOVW R4,R30
; 0000 00A4 rand*=7;
	MOVW R30,R4
	RCALL SUBOPT_0x2
	RCALL SUBOPT_0x4
; 0000 00A5 direccion=rand%4;
	LDI  R30,LOW(4)
	LDI  R31,HIGH(4)
	RCALL SUBOPT_0x5
; 0000 00A6 
; 0000 00A7 //definir x
; 0000 00A8 x=2;
	RCALL SUBOPT_0x6
	RCALL SUBOPT_0x7
; 0000 00A9 //definir y
; 0000 00AA y=3;
; 0000 00AB 
; 0000 00AC barra1=0;
	RCALL SUBOPT_0x8
	RCALL SUBOPT_0x9
	RCALL __EEPROMWRW
; 0000 00AD barra2=3;
	RCALL SUBOPT_0xA
	RCALL SUBOPT_0xB
; 0000 00AE 
; 0000 00AF cont1=0;
	CLR  R6
	CLR  R7
; 0000 00B0 cont2=0;
	CLR  R8
	CLR  R9
; 0000 00B1 i=j=0;
	RCALL SUBOPT_0x9
	STS  _j,R30
	STS  _j+1,R31
	STS  _i,R30
	STS  _i+1,R31
; 0000 00B2 dsplz=0;
	RCALL SUBOPT_0xC
; 0000 00B3 stay=0;
	RCALL SUBOPT_0xD
; 0000 00B4 cols=0;
	RCALL SUBOPT_0xE
; 0000 00B5 puntos1=0;
	CLR  R10
	CLR  R11
; 0000 00B6 puntos2=0;
	CLR  R12
	CLR  R13
; 0000 00B7 rapidez=99;
	LDI  R30,LOW(99)
	LDI  R31,HIGH(99)
	STS  _rapidez,R30
	STS  _rapidez+1,R31
; 0000 00B8 inst=0;
	RCALL SUBOPT_0xF
; 0000 00B9 win=0;
	LDI  R30,LOW(0)
	STS  _win,R30
	STS  _win+1,R30
; 0000 00BA 
; 0000 00BB while (1)
_0x5:
; 0000 00BC       {
; 0000 00BD       if(!win){
	LDS  R30,_win
	LDS  R31,_win+1
	SBIW R30,0
	BREQ PC+2
	RJMP _0x8
; 0000 00BE         delay_ms(1);
	RCALL SUBOPT_0x1
	RCALL SUBOPT_0x10
; 0000 00BF 
; 0000 00C0         cols++;
	LDI  R26,LOW(_cols)
	LDI  R27,HIGH(_cols)
	RCALL SUBOPT_0x11
; 0000 00C1         if(cols>4){
	RCALL SUBOPT_0x12
	SBIW R26,5
	BRLT _0x9
; 0000 00C2             cols=0;
	RCALL SUBOPT_0xE
; 0000 00C3         }
; 0000 00C4 
; 0000 00C5 
; 0000 00C6         PORTA &=0x7f;
_0x9:
	CBI  0x1B,7
; 0000 00C7         PORTC &=0x7f;
	CBI  0x15,7
; 0000 00C8         PORTB |=0x81;
	IN   R30,0x18
	ORI  R30,LOW(0x81)
	OUT  0x18,R30
; 0000 00C9         PORTC |=0x60;
	IN   R30,0x15
	ORI  R30,LOW(0x60)
	OUT  0x15,R30
; 0000 00CA 
; 0000 00CB         inst++;
	LDI  R26,LOW(_inst)
	LDI  R27,HIGH(_inst)
	RCALL SUBOPT_0x11
; 0000 00CC         if(inst>1){
	RCALL SUBOPT_0x13
	SBIW R26,2
	BRLT _0xA
; 0000 00CD             inst=0;
	RCALL SUBOPT_0xF
; 0000 00CE         }
; 0000 00CF 
; 0000 00D0         //Muestra de el puntaje
; 0000 00D1         if(inst){
_0xA:
	LDS  R30,_inst
	LDS  R31,_inst+1
	SBIW R30,0
	BREQ _0xB
; 0000 00D2             PORTA =tabla7segmentos[inst][puntos2];
	RCALL SUBOPT_0x14
	ADD  R30,R12
	ADC  R31,R13
	LD   R30,Z
	OUT  0x1B,R30
; 0000 00D3             PORTC &=0xbf;
	CBI  0x15,6
; 0000 00D4             PORTB &=0x7f;
	CBI  0x18,7
; 0000 00D5         }else{
	RJMP _0xC
_0xB:
; 0000 00D6             PORTA =tabla7segmentos[inst][puntos1];
	RCALL SUBOPT_0x14
	ADD  R30,R10
	ADC  R31,R11
	LD   R30,Z
	OUT  0x1B,R30
; 0000 00D7             PORTC |=0x80;
	SBI  0x15,7
; 0000 00D8             PORTC &=0xdf;
	CBI  0x15,5
; 0000 00D9             PORTB &=0xfe;
	CBI  0x18,0
; 0000 00DA         }
_0xC:
; 0000 00DB 
; 0000 00DC       //Movimiento de barras
; 0000 00DD       if(derecha1==0){
	SBIC 0x16,2
	RJMP _0xD
; 0000 00DE       barra1++;
	RCALL SUBOPT_0x15
	ADIW R30,1
	RCALL __EEPROMWRW
	SBIW R30,1
; 0000 00DF         if(barra1>3){
	RCALL SUBOPT_0x15
	SBIW R30,4
	BRLT _0xE
; 0000 00E0             barra1=3;
	RCALL SUBOPT_0x8
	RCALL SUBOPT_0xB
; 0000 00E1         }
; 0000 00E2         delay_ms(200);
_0xE:
	RCALL SUBOPT_0x16
; 0000 00E3       }
; 0000 00E4       if(izquierda1==0){
_0xD:
	SBIC 0x16,1
	RJMP _0xF
; 0000 00E5       barra1--;
	RCALL SUBOPT_0x15
	SBIW R30,1
	RCALL __EEPROMWRW
	ADIW R30,1
; 0000 00E6         if(barra1<0){
	LDI  R26,LOW(_barra1+1)
	LDI  R27,HIGH(_barra1+1)
	RCALL __EEPROMRDB
	TST  R30
	BRPL _0x10
; 0000 00E7             barra1=0;
	RCALL SUBOPT_0x8
	RCALL SUBOPT_0x9
	RCALL __EEPROMWRW
; 0000 00E8         }
; 0000 00E9         delay_ms(200);
_0x10:
	RCALL SUBOPT_0x16
; 0000 00EA       }
; 0000 00EB       if(derecha2==0){
_0xF:
	SBIC 0x16,4
	RJMP _0x11
; 0000 00EC       barra2++;
	RCALL SUBOPT_0x17
	ADIW R30,1
	RCALL __EEPROMWRW
	SBIW R30,1
; 0000 00ED         if(barra2>3){
	RCALL SUBOPT_0x17
	SBIW R30,4
	BRLT _0x12
; 0000 00EE             barra2=3;
	RCALL SUBOPT_0xA
	RCALL SUBOPT_0xB
; 0000 00EF         }
; 0000 00F0         delay_ms(200);
_0x12:
	RCALL SUBOPT_0x16
; 0000 00F1       }
; 0000 00F2       if(izquierda2==0){
_0x11:
	SBIC 0x16,3
	RJMP _0x13
; 0000 00F3       barra2--;
	RCALL SUBOPT_0x17
	SBIW R30,1
	RCALL __EEPROMWRW
	ADIW R30,1
; 0000 00F4         if(barra2<0){
	LDI  R26,LOW(_barra2+1)
	LDI  R27,HIGH(_barra2+1)
	RCALL __EEPROMRDB
	TST  R30
	BRPL _0x14
; 0000 00F5             barra2=0;
	RCALL SUBOPT_0xA
	RCALL SUBOPT_0x9
	RCALL __EEPROMWRW
; 0000 00F6         }
; 0000 00F7         delay_ms(200);
_0x14:
	RCALL SUBOPT_0x16
; 0000 00F8       }
; 0000 00F9 
; 0000 00FA 
; 0000 00FB       //Matriz de LEDs
; 0000 00FC       if(dsplz>rapidez){
_0x13:
	LDS  R30,_rapidez
	LDS  R31,_rapidez+1
	LDS  R26,_dsplz
	LDS  R27,_dsplz+1
	CP   R30,R26
	CPC  R31,R27
	BRLT PC+2
	RJMP _0x15
; 0000 00FD         dsplz=0;
	RCALL SUBOPT_0xC
; 0000 00FE         if(!stay){
	LDS  R30,_stay
	LDS  R31,_stay+1
	SBIW R30,0
	BRNE _0x16
; 0000 00FF             stay=1;
	RCALL SUBOPT_0x1
	STS  _stay,R30
	STS  _stay+1,R31
; 0000 0100         }else{
	RJMP _0x17
_0x16:
; 0000 0101         stay=0;
	RCALL SUBOPT_0xD
; 0000 0102 
; 0000 0103         //Validaciones y definición de nuea dirección de pelota
; 0000 0104         switch(direccion){
	RCALL SUBOPT_0x18
; 0000 0105             case 0: //noroeste
	BRNE _0x1B
; 0000 0106                 if((x-1)<0){
	RCALL SUBOPT_0x19
	TST  R27
	BRPL _0x1C
; 0000 0107                     if(y==1){
	RCALL SUBOPT_0x1A
	SBIW R26,1
	BRNE _0x1D
; 0000 0108                         if(barra2==0 || barra2==1){
	RCALL SUBOPT_0x17
	SBIW R30,0
	BREQ _0x1F
	RCALL SUBOPT_0x1B
	BRNE _0x1E
_0x1F:
; 0000 0109                             direccion=2;
	RCALL SUBOPT_0x6
	RJMP _0xAE
; 0000 010A 
; 0000 010B                         }else{
_0x1E:
; 0000 010C                             direccion=1;
	RCALL SUBOPT_0x1
_0xAE:
	STS  _direccion,R30
	STS  _direccion+1,R31
; 0000 010D                         }
; 0000 010E                     }else if(y>=2){
	RJMP _0x22
_0x1D:
	RCALL SUBOPT_0x1A
	SBIW R26,2
	BRLT _0x23
; 0000 010F                         direccion=1;
	RCALL SUBOPT_0x1C
; 0000 0110                     }
; 0000 0111                 }else{
_0x23:
_0x22:
	RJMP _0x24
_0x1C:
; 0000 0112                     if(y==1){
	RCALL SUBOPT_0x1A
	SBIW R26,1
	BRNE _0x25
; 0000 0113                         if(barra2==0){
	RCALL SUBOPT_0x17
	SBIW R30,0
	BRNE _0x26
; 0000 0114                                 if(x==1){
	RCALL SUBOPT_0x19
	BRNE _0x27
; 0000 0115                                     direccion=3;
	RCALL SUBOPT_0x1D
; 0000 0116                                 }
; 0000 0117                                 if(x==2){
_0x27:
	RCALL SUBOPT_0x1E
	BRNE _0x28
; 0000 0118                                     direccion=2;
	RCALL SUBOPT_0x1F
; 0000 0119                                 }
; 0000 011A                         }else if(barra2==1){
_0x28:
	RJMP _0x29
_0x26:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x1B
	BRNE _0x2A
; 0000 011B                                 if(x==2){
	RCALL SUBOPT_0x1E
	BRNE _0x2B
; 0000 011C                                     direccion=3;
	RCALL SUBOPT_0x1D
; 0000 011D                                 }
; 0000 011E                                 if(x==3){
_0x2B:
	RCALL SUBOPT_0x20
	BRNE _0x2C
; 0000 011F                                     direccion=2;
	RCALL SUBOPT_0x1F
; 0000 0120                                 }
; 0000 0121                         }else if(barra2==2){
_0x2C:
	RJMP _0x2D
_0x2A:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x21
	BRNE _0x2E
; 0000 0122                                 if(x==3){
	RCALL SUBOPT_0x20
	BRNE _0x2F
; 0000 0123                                     direccion=3;
	RCALL SUBOPT_0x1D
; 0000 0124                                 }
; 0000 0125                         }
_0x2F:
; 0000 0126                     }else if(y<=2){
_0x2E:
_0x2D:
_0x29:
	RJMP _0x30
_0x25:
	RCALL SUBOPT_0x1A
	SBIW R26,3
; 0000 0127                         //direccion=0;
; 0000 0128                     }
; 0000 0129                 }
_0x30:
_0x24:
; 0000 012A                 break;
	RJMP _0x1A
; 0000 012B             case 1: //noreste
_0x1B:
	RCALL SUBOPT_0x1B
	BRNE _0x32
; 0000 012C                 if((x+1)>4){
	RCALL SUBOPT_0x22
	BRLT _0x33
; 0000 012D                     if(y==1){
	RCALL SUBOPT_0x1A
	SBIW R26,1
	BRNE _0x34
; 0000 012E                         if(barra2==2 || barra2==3){
	RCALL SUBOPT_0x17
	MOVW R26,R30
	SBIW R30,2
	BREQ _0x36
	RCALL SUBOPT_0x23
	BRNE _0x35
_0x36:
; 0000 012F                             direccion=3;
	RCALL SUBOPT_0x1D
; 0000 0130 
; 0000 0131                         }else{
	RJMP _0x38
_0x35:
; 0000 0132                             direccion=0;
	RCALL SUBOPT_0x24
; 0000 0133                         }
_0x38:
; 0000 0134                     }else if(y>=2){
	RJMP _0x39
_0x34:
	RCALL SUBOPT_0x1A
	SBIW R26,2
	BRLT _0x3A
; 0000 0135                         direccion=0;
	RCALL SUBOPT_0x24
; 0000 0136                     }
; 0000 0137                 }else{
_0x3A:
_0x39:
	RJMP _0x3B
_0x33:
; 0000 0138                     if(y==1){
	RCALL SUBOPT_0x1A
	SBIW R26,1
	BRNE _0x3C
; 0000 0139                         if(barra2==1){
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x1B
	BRNE _0x3D
; 0000 013A                                 if(x==1){
	RCALL SUBOPT_0x19
	BRNE _0x3E
; 0000 013B                                     direccion=2;
	RCALL SUBOPT_0x1F
; 0000 013C                                 }
; 0000 013D                         }else if(barra2==2){
_0x3E:
	RJMP _0x3F
_0x3D:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x21
	BRNE _0x40
; 0000 013E                                 if(x==2){
	RCALL SUBOPT_0x1E
	BRNE _0x41
; 0000 013F                                     direccion=2;
	RCALL SUBOPT_0x1F
; 0000 0140                                 }
; 0000 0141                                 if(x==1){
_0x41:
	RCALL SUBOPT_0x19
	BRNE _0x42
; 0000 0142                                     direccion=3;
	RCALL SUBOPT_0x1D
; 0000 0143                                 }
; 0000 0144                         }else if (barra2==3){
_0x42:
	RJMP _0x43
_0x40:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x25
	BRNE _0x44
; 0000 0145                                 if(x==3){
	RCALL SUBOPT_0x20
	BRNE _0x45
; 0000 0146                                     direccion=2;
	RCALL SUBOPT_0x1F
; 0000 0147                                 }
; 0000 0148                                 if(x==2){
_0x45:
	RCALL SUBOPT_0x1E
	BRNE _0x46
; 0000 0149                                     direccion=3;
	RCALL SUBOPT_0x1D
; 0000 014A                                 }
; 0000 014B                         }
_0x46:
; 0000 014C                     }else if(y>=2){
_0x44:
_0x43:
_0x3F:
	RJMP _0x47
_0x3C:
	RCALL SUBOPT_0x1A
	SBIW R26,2
; 0000 014D                         //direccion=1;
; 0000 014E                     }
; 0000 014F                 }
_0x47:
_0x3B:
; 0000 0150                 break;
	RJMP _0x1A
; 0000 0151             case 2: //sureste
_0x32:
	RCALL SUBOPT_0x21
	BRNE _0x49
; 0000 0152                 if((x+1)>4){
	RCALL SUBOPT_0x22
	BRLT _0x4A
; 0000 0153                     if(y==5){
	RCALL SUBOPT_0x26
	BRNE _0x4B
; 0000 0154                         if(barra1==2 || barra1==3){
	RCALL SUBOPT_0x15
	MOVW R26,R30
	SBIW R30,2
	BREQ _0x4D
	RCALL SUBOPT_0x23
	BRNE _0x4C
_0x4D:
; 0000 0155                             direccion=0;
	RCALL SUBOPT_0x24
; 0000 0156 
; 0000 0157                         }else{
	RJMP _0x4F
_0x4C:
; 0000 0158                             direccion=3;
	RCALL SUBOPT_0x1D
; 0000 0159                         }
_0x4F:
; 0000 015A                     }else if(y<=4){
	RJMP _0x50
_0x4B:
	RCALL SUBOPT_0x26
	BRGE _0x51
; 0000 015B                         direccion=3;
	RCALL SUBOPT_0x1D
; 0000 015C                     }
; 0000 015D                 }else{
_0x51:
_0x50:
	RJMP _0x52
_0x4A:
; 0000 015E                     if(y==5){
	RCALL SUBOPT_0x26
	BRNE _0x53
; 0000 015F                         if(barra1==1){
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x1B
	BRNE _0x54
; 0000 0160                                 if(x==1){
	RCALL SUBOPT_0x19
	BRNE _0x55
; 0000 0161                                     direccion=1;
	RCALL SUBOPT_0x1C
; 0000 0162                                 }
; 0000 0163                         }else if(barra1==2){
_0x55:
	RJMP _0x56
_0x54:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x21
	BRNE _0x57
; 0000 0164                                 if(x==2){
	RCALL SUBOPT_0x1E
	BRNE _0x58
; 0000 0165                                     direccion=1;
	RCALL SUBOPT_0x1C
; 0000 0166                                 }
; 0000 0167                                 if(x==1){
_0x58:
	RCALL SUBOPT_0x19
	BRNE _0x59
; 0000 0168                                     direccion=0;
	RCALL SUBOPT_0x24
; 0000 0169                                 }
; 0000 016A                         }else if (barra1==3){
_0x59:
	RJMP _0x5A
_0x57:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x25
	BRNE _0x5B
; 0000 016B                                 if(x==3){
	RCALL SUBOPT_0x20
	BRNE _0x5C
; 0000 016C                                     direccion=1;
	RCALL SUBOPT_0x1C
; 0000 016D                                 }
; 0000 016E                                 if(x==2){
_0x5C:
	RCALL SUBOPT_0x1E
	BRNE _0x5D
; 0000 016F                                     direccion=0;
	RCALL SUBOPT_0x24
; 0000 0170                                 }
; 0000 0171                         }
_0x5D:
; 0000 0172                     }else if(y<=4){
_0x5B:
_0x5A:
_0x56:
	RJMP _0x5E
_0x53:
	RCALL SUBOPT_0x26
; 0000 0173                         //direccion=2;
; 0000 0174                     }
; 0000 0175                 }
_0x5E:
_0x52:
; 0000 0176                 break;
	RJMP _0x1A
; 0000 0177             case 3: //suroeste
_0x49:
	RCALL SUBOPT_0x25
	BRNE _0x77
; 0000 0178                 if((x-1)<0){
	RCALL SUBOPT_0x19
	TST  R27
	BRPL _0x61
; 0000 0179                     if(y==5){
	RCALL SUBOPT_0x26
	BRNE _0x62
; 0000 017A                         if(barra1==0 || barra1==1){
	RCALL SUBOPT_0x15
	SBIW R30,0
	BREQ _0x64
	RCALL SUBOPT_0x1B
	BRNE _0x63
_0x64:
; 0000 017B                             direccion=1;
	RCALL SUBOPT_0x1
	RJMP _0xAF
; 0000 017C 
; 0000 017D                         }else{
_0x63:
; 0000 017E                             direccion=2;
	RCALL SUBOPT_0x6
_0xAF:
	STS  _direccion,R30
	STS  _direccion+1,R31
; 0000 017F                         }
; 0000 0180                     }else if(y<=4){
	RJMP _0x67
_0x62:
	RCALL SUBOPT_0x26
	BRGE _0x68
; 0000 0181                         direccion=2;
	RCALL SUBOPT_0x1F
; 0000 0182                     }
; 0000 0183                 }else{
_0x68:
_0x67:
	RJMP _0x69
_0x61:
; 0000 0184                     if(y==5){
	RCALL SUBOPT_0x26
	BRNE _0x6A
; 0000 0185                         if(barra1==0){
	RCALL SUBOPT_0x15
	SBIW R30,0
	BRNE _0x6B
; 0000 0186                                 if(x==1){
	RCALL SUBOPT_0x19
	BRNE _0x6C
; 0000 0187                                     direccion=0;
	RCALL SUBOPT_0x24
; 0000 0188                                 }
; 0000 0189                                 if(x==2){
_0x6C:
	RCALL SUBOPT_0x1E
	BRNE _0x6D
; 0000 018A                                     direccion=1;
	RCALL SUBOPT_0x1C
; 0000 018B                                 }
; 0000 018C                         }else if(barra1==1){
_0x6D:
	RJMP _0x6E
_0x6B:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x1B
	BRNE _0x6F
; 0000 018D                                 if(x==2){
	RCALL SUBOPT_0x1E
	BRNE _0x70
; 0000 018E                                     direccion=0;
	RCALL SUBOPT_0x24
; 0000 018F                                 }
; 0000 0190                                 if(x==3){
_0x70:
	RCALL SUBOPT_0x20
	BRNE _0x71
; 0000 0191                                     direccion=1;
	RCALL SUBOPT_0x1C
; 0000 0192                                 }
; 0000 0193                         }else if(barra1==2){
_0x71:
	RJMP _0x72
_0x6F:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x21
	BRNE _0x73
; 0000 0194                                 if(x==3){
	RCALL SUBOPT_0x20
	BRNE _0x74
; 0000 0195                                     direccion=0;
	RCALL SUBOPT_0x24
; 0000 0196                                 }
; 0000 0197                         }
_0x74:
; 0000 0198                     }else if(y<=4){
_0x73:
_0x72:
_0x6E:
	RJMP _0x75
_0x6A:
	RCALL SUBOPT_0x26
; 0000 0199                         //direccion=3;
; 0000 019A                     }
; 0000 019B                 }
_0x75:
_0x69:
; 0000 019C                 break;
; 0000 019D             default:
_0x77:
; 0000 019E                 break;
; 0000 019F         }
_0x1A:
; 0000 01A0 
; 0000 01A1         //Redireccionamiento de pelota
; 0000 01A2         switch(direccion){
	RCALL SUBOPT_0x18
; 0000 01A3             case 0: //noroeste
	BRNE _0x7B
; 0000 01A4                 x--;
	RCALL SUBOPT_0x27
	RCALL SUBOPT_0x28
; 0000 01A5                 y--;
	LDI  R26,LOW(_y)
	LDI  R27,HIGH(_y)
	RCALL SUBOPT_0x28
; 0000 01A6                 break;
	RJMP _0x7A
; 0000 01A7             case 1: //noreste
_0x7B:
	RCALL SUBOPT_0x1B
	BRNE _0x7C
; 0000 01A8                 x++;
	RCALL SUBOPT_0x27
	RCALL SUBOPT_0x11
; 0000 01A9                 y--;
	LDI  R26,LOW(_y)
	LDI  R27,HIGH(_y)
	RCALL SUBOPT_0x28
; 0000 01AA                 break;
	RJMP _0x7A
; 0000 01AB             case 2: //sureste
_0x7C:
	RCALL SUBOPT_0x21
	BRNE _0x7D
; 0000 01AC                 x++;
	RCALL SUBOPT_0x27
	RCALL SUBOPT_0x11
; 0000 01AD                 y++;
	LDI  R26,LOW(_y)
	LDI  R27,HIGH(_y)
	RCALL SUBOPT_0x11
; 0000 01AE                 break;
	RJMP _0x7A
; 0000 01AF             case 3: //suroeste
_0x7D:
	RCALL SUBOPT_0x25
	BRNE _0x7F
; 0000 01B0                 x--;
	RCALL SUBOPT_0x27
	RCALL SUBOPT_0x28
; 0000 01B1                 y++;
	LDI  R26,LOW(_y)
	LDI  R27,HIGH(_y)
	RCALL SUBOPT_0x11
; 0000 01B2                 break;
; 0000 01B3             default:
_0x7F:
; 0000 01B4                 break;
; 0000 01B5         }
_0x7A:
; 0000 01B6       }
_0x17:
; 0000 01B7       }else{
	RJMP _0x80
_0x15:
; 0000 01B8         dsplz++;
	LDI  R26,LOW(_dsplz)
	LDI  R27,HIGH(_dsplz)
	RCALL SUBOPT_0x11
; 0000 01B9       }
_0x80:
; 0000 01BA 
; 0000 01BB       //Barrido para la pelotita
; 0000 01BC         PORTD |=0xfb;
	RCALL SUBOPT_0x29
; 0000 01BD         PORTC &=0xe0;
; 0000 01BE         if((cols%5)==x){
	RCALL SUBOPT_0x2A
	MOVW R26,R30
	LDS  R30,_x
	LDS  R31,_x+1
	CP   R30,R26
	CPC  R31,R27
	BRNE _0x81
; 0000 01BF         switch(y){
	LDS  R30,_y
	LDS  R31,_y+1
; 0000 01C0             case 0:
	SBIW R30,0
	BRNE _0x85
; 0000 01C1                 PORTD &=0x7f;
	CBI  0x12,7
; 0000 01C2                 break;
	RJMP _0x84
; 0000 01C3             case 1:
_0x85:
	RCALL SUBOPT_0x1B
	BRNE _0x86
; 0000 01C4                 PORTD &=0xbf;
	CBI  0x12,6
; 0000 01C5                 break;
	RJMP _0x84
; 0000 01C6             case 2:
_0x86:
	RCALL SUBOPT_0x21
	BRNE _0x87
; 0000 01C7                 PORTD &=0xdf;
	CBI  0x12,5
; 0000 01C8                 break;
	RJMP _0x84
; 0000 01C9             case 3:
_0x87:
	RCALL SUBOPT_0x25
	BRNE _0x88
; 0000 01CA                 PORTD &=0xef;
	CBI  0x12,4
; 0000 01CB                 break;
	RJMP _0x84
; 0000 01CC             case 4:
_0x88:
	CPI  R30,LOW(0x4)
	LDI  R26,HIGH(0x4)
	CPC  R31,R26
	BRNE _0x89
; 0000 01CD                 PORTD &=0xf7;
	CBI  0x12,3
; 0000 01CE                 break;
	RJMP _0x84
; 0000 01CF             case 5:
_0x89:
	CPI  R30,LOW(0x5)
	LDI  R26,HIGH(0x5)
	CPC  R31,R26
	BRNE _0x8A
; 0000 01D0                 PORTD &=0xfd;
	CBI  0x12,1
; 0000 01D1                 break;
	RJMP _0x84
; 0000 01D2             case 6:
_0x8A:
	CPI  R30,LOW(0x6)
	LDI  R26,HIGH(0x6)
	CPC  R31,R26
	BRNE _0x8C
; 0000 01D3                 PORTD &=0xfe;
	CBI  0x12,0
; 0000 01D4                 break;
; 0000 01D5             default:
_0x8C:
; 0000 01D6                 break;
; 0000 01D7         }
_0x84:
; 0000 01D8         }
; 0000 01D9 
; 0000 01DA         //Barrido para las barras
; 0000 01DB         switch((cols%5)){
_0x81:
	RCALL SUBOPT_0x2A
; 0000 01DC             case 0:
	SBIW R30,0
	BRNE _0x90
; 0000 01DD                 if(barra1==0){
	RCALL SUBOPT_0x15
	SBIW R30,0
	BRNE _0x91
; 0000 01DE                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 01DF                 }
; 0000 01E0                 if(barra2==0){
_0x91:
	RCALL SUBOPT_0x17
	SBIW R30,0
	BRNE _0x92
; 0000 01E1                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 01E2                 }
; 0000 01E3                 PORTC |=0x01;
_0x92:
	SBI  0x15,0
; 0000 01E4                 break;
	RJMP _0x8F
; 0000 01E5             case 1:
_0x90:
	RCALL SUBOPT_0x1B
	BRNE _0x93
; 0000 01E6                 if(barra1==0){
	RCALL SUBOPT_0x15
	SBIW R30,0
	BRNE _0x94
; 0000 01E7                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 01E8                 }
; 0000 01E9                 if(barra2==0){
_0x94:
	RCALL SUBOPT_0x17
	SBIW R30,0
	BRNE _0x95
; 0000 01EA                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 01EB                 }
; 0000 01EC                 if(barra1==1){
_0x95:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x1B
	BRNE _0x96
; 0000 01ED                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 01EE                 }
; 0000 01EF                 if(barra2==1){
_0x96:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x1B
	BRNE _0x97
; 0000 01F0                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 01F1                 }
; 0000 01F2                 PORTC |=0x02;
_0x97:
	SBI  0x15,1
; 0000 01F3                 break;
	RJMP _0x8F
; 0000 01F4             case 2:
_0x93:
	RCALL SUBOPT_0x21
	BRNE _0x98
; 0000 01F5                 if(barra1==1){
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x1B
	BRNE _0x99
; 0000 01F6                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 01F7                 }
; 0000 01F8                 if(barra2==1){
_0x99:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x1B
	BRNE _0x9A
; 0000 01F9                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 01FA                 }
; 0000 01FB                 if(barra1==2){
_0x9A:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x21
	BRNE _0x9B
; 0000 01FC                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 01FD                 }
; 0000 01FE                 if(barra2==2){
_0x9B:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x21
	BRNE _0x9C
; 0000 01FF                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 0200                 }
; 0000 0201                 PORTC |=0x04;
_0x9C:
	SBI  0x15,2
; 0000 0202                 break;
	RJMP _0x8F
; 0000 0203             case 3:
_0x98:
	RCALL SUBOPT_0x25
	BRNE _0x9D
; 0000 0204                 if(barra1==2){
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x21
	BRNE _0x9E
; 0000 0205                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 0206                 }
; 0000 0207                 if(barra2==2){
_0x9E:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x21
	BRNE _0x9F
; 0000 0208                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 0209                 }
; 0000 020A                 if(barra1==3){
_0x9F:
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x25
	BRNE _0xA0
; 0000 020B                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 020C                 }
; 0000 020D                 if(barra2==3){
_0xA0:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x25
	BRNE _0xA1
; 0000 020E                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 020F                 }
; 0000 0210                 PORTC |=0x08;
_0xA1:
	SBI  0x15,3
; 0000 0211                 break;
	RJMP _0x8F
; 0000 0212             case 4:
_0x9D:
	CPI  R30,LOW(0x4)
	LDI  R26,HIGH(0x4)
	CPC  R31,R26
	BRNE _0xA5
; 0000 0213                 if(barra1==3){
	RCALL SUBOPT_0x15
	RCALL SUBOPT_0x25
	BRNE _0xA3
; 0000 0214                     PORTD &=0xfe;
	CBI  0x12,0
; 0000 0215                 }
; 0000 0216                 if(barra2==3){
_0xA3:
	RCALL SUBOPT_0x17
	RCALL SUBOPT_0x25
	BRNE _0xA4
; 0000 0217                     PORTD &=0x7f;
	CBI  0x12,7
; 0000 0218                 }
; 0000 0219                 PORTC |=0x10;
_0xA4:
	SBI  0x15,4
; 0000 021A                 break;
; 0000 021B             default:
_0xA5:
; 0000 021C                 break;
; 0000 021D         }
_0x8F:
; 0000 021E 
; 0000 021F         //Anotación de un punto
; 0000 0220         if(y<0 || y>6){
	LDS  R26,_y+1
	TST  R26
	BRMI _0xA7
	RCALL SUBOPT_0x1A
	SBIW R26,7
	BRLT _0xA6
_0xA7:
; 0000 0221         PORTD |=0xfb;
	RCALL SUBOPT_0x29
; 0000 0222         PORTC &=0xe0;
; 0000 0223         if(y>6){
	RCALL SUBOPT_0x1A
	SBIW R26,7
	BRLT _0xA9
; 0000 0224             puntos2++;
	MOVW R30,R12
	ADIW R30,1
	MOVW R12,R30
; 0000 0225             if(puntos2>9){
	LDI  R30,LOW(9)
	LDI  R31,HIGH(9)
	CP   R30,R12
	CPC  R31,R13
	BRGE _0xAA
; 0000 0226                 win=1;
	RCALL SUBOPT_0x2B
; 0000 0227             }
; 0000 0228             //redefinir direccion
; 0000 0229             rand*=7;
_0xAA:
	MOVW R30,R4
	RCALL SUBOPT_0x2
	RCALL SUBOPT_0x4
; 0000 022A             rand=rand%11;
	RCALL SUBOPT_0x2C
; 0000 022B             direccion=rand%2;
	RCALL SUBOPT_0x6
	RCALL SUBOPT_0x5
; 0000 022C 
; 0000 022D         }
; 0000 022E         if(y<0){
_0xA9:
	LDS  R26,_y+1
	TST  R26
	BRPL _0xAB
; 0000 022F             puntos1++;
	MOVW R30,R10
	ADIW R30,1
	MOVW R10,R30
; 0000 0230             if(puntos1>9){
	LDI  R30,LOW(9)
	LDI  R31,HIGH(9)
	CP   R30,R10
	CPC  R31,R11
	BRGE _0xAC
; 0000 0231                 win=1;
	RCALL SUBOPT_0x2B
; 0000 0232             }
; 0000 0233             //redefinir direccion
; 0000 0234             rand*=7;
_0xAC:
	MOVW R30,R4
	RCALL SUBOPT_0x2
	RCALL SUBOPT_0x4
; 0000 0235             rand=rand%11;
	RCALL SUBOPT_0x2C
; 0000 0236             direccion=(rand%2)+2;
	RCALL SUBOPT_0x6
	RCALL __MODW21
	ADIW R30,2
	STS  _direccion,R30
	STS  _direccion+1,R31
; 0000 0237 
; 0000 0238         }
; 0000 0239         //redefinir x
; 0000 023A         rand*=19;
_0xAB:
	MOVW R30,R4
	LDI  R26,LOW(19)
	LDI  R27,HIGH(19)
	RCALL __MULW12
	MOVW R4,R30
; 0000 023B         rand+=7;
	MOVW R30,R4
	ADIW R30,7
	RCALL SUBOPT_0x4
; 0000 023C         x=1+(rand%3);
	LDI  R30,LOW(3)
	LDI  R31,HIGH(3)
	RCALL __MODW21
	ADIW R30,1
	RCALL SUBOPT_0x7
; 0000 023D         //redefinir y
; 0000 023E         y=3;
; 0000 023F 
; 0000 0240         delay_ms(200);
	RCALL SUBOPT_0x16
; 0000 0241         }
; 0000 0242       }
_0xA6:
; 0000 0243       }
_0x8:
	RJMP _0x5
; 0000 0244 }
_0xAD:
	RJMP _0xAD

	.ESEG
_random:
	.BYTE 0x2
_barra1:
	.BYTE 0x2
_barra2:
	.BYTE 0x2

	.DSEG
_i:
	.BYTE 0x2
_j:
	.BYTE 0x2
_x:
	.BYTE 0x2
_y:
	.BYTE 0x2
_direccion:
	.BYTE 0x2
_dsplz:
	.BYTE 0x2
_stay:
	.BYTE 0x2
_cols:
	.BYTE 0x2
_inst:
	.BYTE 0x2
_win:
	.BYTE 0x2
_rapidez:
	.BYTE 0x2
_tabla7segmentos:
	.BYTE 0x14

	.CSEG
;OPTIMIZER ADDED SUBROUTINE, CALLED 7 TIMES, CODE SIZE REDUCTION:4 WORDS
SUBOPT_0x0:
	LDI  R26,LOW(_random)
	LDI  R27,HIGH(_random)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 13 TIMES, CODE SIZE REDUCTION:10 WORDS
SUBOPT_0x1:
	LDI  R30,LOW(1)
	LDI  R31,HIGH(1)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 4 TIMES, CODE SIZE REDUCTION:4 WORDS
SUBOPT_0x2:
	LDI  R26,LOW(7)
	LDI  R27,HIGH(7)
	RCALL __MULW12
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x3:
	RCALL SUBOPT_0x0
	RCALL __EEPROMWRW
	RCALL SUBOPT_0x0
	RCALL __EEPROMRDW
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 6 TIMES, CODE SIZE REDUCTION:3 WORDS
SUBOPT_0x4:
	MOVW R4,R30
	MOVW R26,R4
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0x5:
	RCALL __MODW21
	STS  _direccion,R30
	STS  _direccion+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 11 TIMES, CODE SIZE REDUCTION:8 WORDS
SUBOPT_0x6:
	LDI  R30,LOW(2)
	LDI  R31,HIGH(2)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:7 WORDS
SUBOPT_0x7:
	STS  _x,R30
	STS  _x+1,R31
	LDI  R30,LOW(3)
	LDI  R31,HIGH(3)
	STS  _y,R30
	STS  _y+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 22 TIMES, CODE SIZE REDUCTION:19 WORDS
SUBOPT_0x8:
	LDI  R26,LOW(_barra1)
	LDI  R27,HIGH(_barra1)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 4 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x9:
	LDI  R30,LOW(0)
	LDI  R31,HIGH(0)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 22 TIMES, CODE SIZE REDUCTION:19 WORDS
SUBOPT_0xA:
	LDI  R26,LOW(_barra2)
	LDI  R27,HIGH(_barra2)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 3 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0xB:
	LDI  R30,LOW(3)
	LDI  R31,HIGH(3)
	RCALL __EEPROMWRW
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0xC:
	LDI  R30,LOW(0)
	STS  _dsplz,R30
	STS  _dsplz+1,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0xD:
	LDI  R30,LOW(0)
	STS  _stay,R30
	STS  _stay+1,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0xE:
	LDI  R30,LOW(0)
	STS  _cols,R30
	STS  _cols+1,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0xF:
	LDI  R30,LOW(0)
	STS  _inst,R30
	STS  _inst+1,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 6 TIMES, CODE SIZE REDUCTION:8 WORDS
SUBOPT_0x10:
	ST   -Y,R31
	ST   -Y,R30
	RJMP _delay_ms

;OPTIMIZER ADDED SUBROUTINE, CALLED 7 TIMES, CODE SIZE REDUCTION:22 WORDS
SUBOPT_0x11:
	LD   R30,X+
	LD   R31,X+
	ADIW R30,1
	ST   -X,R31
	ST   -X,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 3 TIMES, CODE SIZE REDUCTION:4 WORDS
SUBOPT_0x12:
	LDS  R26,_cols
	LDS  R27,_cols+1
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 3 TIMES, CODE SIZE REDUCTION:4 WORDS
SUBOPT_0x13:
	LDS  R26,_inst
	LDS  R27,_inst+1
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0x14:
	RCALL SUBOPT_0x13
	LDI  R30,LOW(10)
	RCALL __MULB1W2U
	SUBI R30,LOW(-_tabla7segmentos)
	SBCI R31,HIGH(-_tabla7segmentos)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 19 TIMES, CODE SIZE REDUCTION:16 WORDS
SUBOPT_0x15:
	RCALL SUBOPT_0x8
	RCALL __EEPROMRDW
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 5 TIMES, CODE SIZE REDUCTION:6 WORDS
SUBOPT_0x16:
	LDI  R30,LOW(200)
	LDI  R31,HIGH(200)
	RJMP SUBOPT_0x10

;OPTIMIZER ADDED SUBROUTINE, CALLED 19 TIMES, CODE SIZE REDUCTION:16 WORDS
SUBOPT_0x17:
	RCALL SUBOPT_0xA
	RCALL __EEPROMRDW
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0x18:
	LDS  R30,_direccion
	LDS  R31,_direccion+1
	SBIW R30,0
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 8 TIMES, CODE SIZE REDUCTION:26 WORDS
SUBOPT_0x19:
	LDS  R26,_x
	LDS  R27,_x+1
	SBIW R26,1
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 18 TIMES, CODE SIZE REDUCTION:49 WORDS
SUBOPT_0x1A:
	LDS  R26,_y
	LDS  R27,_y+1
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 14 TIMES, CODE SIZE REDUCTION:24 WORDS
SUBOPT_0x1B:
	CPI  R30,LOW(0x1)
	LDI  R26,HIGH(0x1)
	CPC  R31,R26
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 6 TIMES, CODE SIZE REDUCTION:18 WORDS
SUBOPT_0x1C:
	RCALL SUBOPT_0x1
	STS  _direccion,R30
	STS  _direccion+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 8 TIMES, CODE SIZE REDUCTION:33 WORDS
SUBOPT_0x1D:
	LDI  R30,LOW(3)
	LDI  R31,HIGH(3)
	STS  _direccion,R30
	STS  _direccion+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 8 TIMES, CODE SIZE REDUCTION:26 WORDS
SUBOPT_0x1E:
	LDS  R26,_x
	LDS  R27,_x+1
	SBIW R26,2
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 6 TIMES, CODE SIZE REDUCTION:18 WORDS
SUBOPT_0x1F:
	RCALL SUBOPT_0x6
	STS  _direccion,R30
	STS  _direccion+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 6 TIMES, CODE SIZE REDUCTION:18 WORDS
SUBOPT_0x20:
	LDS  R26,_x
	LDS  R27,_x+1
	SBIW R26,3
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 12 TIMES, CODE SIZE REDUCTION:20 WORDS
SUBOPT_0x21:
	CPI  R30,LOW(0x2)
	LDI  R26,HIGH(0x2)
	CPC  R31,R26
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:3 WORDS
SUBOPT_0x22:
	LDS  R26,_x
	LDS  R27,_x+1
	ADIW R26,1
	SBIW R26,5
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x23:
	MOVW R30,R26
	CPI  R30,LOW(0x3)
	LDI  R26,HIGH(0x3)
	CPC  R31,R26
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 8 TIMES, CODE SIZE REDUCTION:26 WORDS
SUBOPT_0x24:
	LDI  R30,LOW(0)
	STS  _direccion,R30
	STS  _direccion+1,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 10 TIMES, CODE SIZE REDUCTION:16 WORDS
SUBOPT_0x25:
	CPI  R30,LOW(0x3)
	LDI  R26,HIGH(0x3)
	CPC  R31,R26
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 8 TIMES, CODE SIZE REDUCTION:5 WORDS
SUBOPT_0x26:
	RCALL SUBOPT_0x1A
	SBIW R26,5
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 4 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x27:
	LDI  R26,LOW(_x)
	LDI  R27,HIGH(_x)
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 4 TIMES, CODE SIZE REDUCTION:10 WORDS
SUBOPT_0x28:
	LD   R30,X+
	LD   R31,X+
	SBIW R30,1
	ST   -X,R31
	ST   -X,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:3 WORDS
SUBOPT_0x29:
	IN   R30,0x12
	ORI  R30,LOW(0xFB)
	OUT  0x12,R30
	IN   R30,0x15
	ANDI R30,LOW(0xE0)
	OUT  0x15,R30
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x2A:
	RCALL SUBOPT_0x12
	LDI  R30,LOW(5)
	LDI  R31,HIGH(5)
	RCALL __MODW21
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:2 WORDS
SUBOPT_0x2B:
	RCALL SUBOPT_0x1
	STS  _win,R30
	STS  _win+1,R31
	RET

;OPTIMIZER ADDED SUBROUTINE, CALLED 2 TIMES, CODE SIZE REDUCTION:1 WORDS
SUBOPT_0x2C:
	LDI  R30,LOW(11)
	LDI  R31,HIGH(11)
	RCALL __MODW21
	RJMP SUBOPT_0x4


	.CSEG
_delay_ms:
	ld   r30,y+
	ld   r31,y+
	adiw r30,0
	breq __delay_ms1
__delay_ms0:
	__DELAY_USW 0xFA
	wdr
	sbiw r30,1
	brne __delay_ms0
__delay_ms1:
	ret

__ANEGW1:
	NEG  R31
	NEG  R30
	SBCI R31,0
	RET

__MULW12U:
	MUL  R31,R26
	MOV  R31,R0
	MUL  R30,R27
	ADD  R31,R0
	MUL  R30,R26
	MOV  R30,R0
	ADD  R31,R1
	RET

__MULB1W2U:
	MOV  R22,R30
	MUL  R22,R26
	MOVW R30,R0
	MUL  R22,R27
	ADD  R31,R0
	RET

__MULW12:
	RCALL __CHKSIGNW
	RCALL __MULW12U
	BRTC __MULW121
	RCALL __ANEGW1
__MULW121:
	RET

__DIVW21U:
	CLR  R0
	CLR  R1
	LDI  R25,16
__DIVW21U1:
	LSL  R26
	ROL  R27
	ROL  R0
	ROL  R1
	SUB  R0,R30
	SBC  R1,R31
	BRCC __DIVW21U2
	ADD  R0,R30
	ADC  R1,R31
	RJMP __DIVW21U3
__DIVW21U2:
	SBR  R26,1
__DIVW21U3:
	DEC  R25
	BRNE __DIVW21U1
	MOVW R30,R26
	MOVW R26,R0
	RET

__MODW21:
	CLT
	SBRS R27,7
	RJMP __MODW211
	COM  R26
	COM  R27
	ADIW R26,1
	SET
__MODW211:
	SBRC R31,7
	RCALL __ANEGW1
	RCALL __DIVW21U
	MOVW R30,R26
	BRTC __MODW212
	RCALL __ANEGW1
__MODW212:
	RET

__CHKSIGNW:
	CLT
	SBRS R31,7
	RJMP __CHKSW1
	RCALL __ANEGW1
	SET
__CHKSW1:
	SBRS R27,7
	RJMP __CHKSW2
	COM  R26
	COM  R27
	ADIW R26,1
	BLD  R0,0
	INC  R0
	BST  R0,0
__CHKSW2:
	RET

__EEPROMRDW:
	ADIW R26,1
	RCALL __EEPROMRDB
	MOV  R31,R30
	SBIW R26,1

__EEPROMRDB:
	SBIC EECR,EEWE
	RJMP __EEPROMRDB
	PUSH R31
	IN   R31,SREG
	CLI
	OUT  EEARL,R26
	OUT  EEARH,R27
	SBI  EECR,EERE
	IN   R30,EEDR
	OUT  SREG,R31
	POP  R31
	RET

__EEPROMWRW:
	RCALL __EEPROMWRB
	ADIW R26,1
	PUSH R30
	MOV  R30,R31
	RCALL __EEPROMWRB
	POP  R30
	SBIW R26,1
	RET

__EEPROMWRB:
	SBIS EECR,EEWE
	RJMP __EEPROMWRB1
	WDR
	RJMP __EEPROMWRB
__EEPROMWRB1:
	IN   R25,SREG
	CLI
	OUT  EEARL,R26
	OUT  EEARH,R27
	SBI  EECR,EERE
	IN   R24,EEDR
	CP   R30,R24
	BREQ __EEPROMWRB0
	OUT  EEDR,R30
	SBI  EECR,EEMWE
	SBI  EECR,EEWE
__EEPROMWRB0:
	OUT  SREG,R25
	RET

;END OF CODE MARKER
__END_OF_CODE:
