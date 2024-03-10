/*****************************************************
This program was produced by the
CodeWizardAVR V2.05.0 Professional
Automatic Program Generator
© Copyright 1998-2010 Pavel Haiduc, HP InfoTech s.r.l.
http://www.hpinfotech.com

Project : 
Version : 
Date    : 24/01/2021
Author  : NeVaDa
Company : 
Comments: 


Chip type               : ATmega8535
Program type            : Application
AVR Core Clock frequency: 1.000000 MHz
Memory model            : Small
External RAM size       : 0
Data Stack size         : 128
*****************************************************/

#include <mega8535.h>
#include <delay.h>
#define izquierda1 PINB.1
#define derecha1 PINB.2
#define izquierda2 PINB.3
#define derecha2 PINB.4

eeprom short random;
eeprom short barra1;
eeprom short barra2;
int rand;
int cont1,cont2;
int puntos1,puntos2;
int i,j;
int x,y;
int direccion, dsplz, stay, cols, inst, win, rapidez;
const char tabla7segmentos[2][10]={
{0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x00,0x10},
{0xc0,0xcf,0xa4,0x86,0x8b,0x92,0x90,0xc7,0x80,0x82}
};

void main(void)
{
// Declare your local variables here

// Input/Output Ports initialization
// Port A initialization
// Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out 
// State7=0 State6=1 State5=0 State4=0 State3=0 State2=0 State1=0 State0=0 
PORTA=0x40;
DDRA=0xFF;

// Port B initialization
// Func7=Out Func6=In Func5=In Func4=In Func3=In Func2=In Func1=In Func0=Out 
// State7=1 State6=P State5=P State4=P State3=P State2=P State1=P State0=1 
PORTB=0xFF;
DDRB=0x81;

// Port C initialization
// Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out 
// State7=0 State6=1 State5=1 State4=0 State3=0 State2=0 State1=0 State0=0 
PORTC=0x60;
DDRC=0xFF;

// Port D initialization
// Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=In Func1=Out Func0=Out 
// State7=1 State6=1 State5=1 State4=1 State3=1 State2=P State1=1 State0=1 
PORTD=0xFF;
DDRD=0xFB;

// Timer/Counter 0 initialization
// Clock source: System Clock
// Clock value: Timer 0 Stopped
// Mode: Normal top=0xFF
// OC0 output: Disconnected
TCCR0=0x00;
TCNT0=0x00;
OCR0=0x00;

// Timer/Counter 1 initialization
// Clock source: System Clock
// Clock value: Timer1 Stopped
// Mode: Normal top=0xFFFF
// OC1A output: Discon.
// OC1B output: Discon.
// Noise Canceler: Off
// Input Capture on Falling Edge
// Timer1 Overflow Interrupt: Off
// Input Capture Interrupt: Off
// Compare A Match Interrupt: Off
// Compare B Match Interrupt: Off
TCCR1A=0x00;
TCCR1B=0x00;
TCNT1H=0x00;
TCNT1L=0x00;
ICR1H=0x00;
ICR1L=0x00;
OCR1AH=0x00;
OCR1AL=0x00;
OCR1BH=0x00;
OCR1BL=0x00;

// Timer/Counter 2 initialization
// Clock source: System Clock
// Clock value: Timer2 Stopped
// Mode: Normal top=0xFF
// OC2 output: Disconnected
ASSR=0x00;
TCCR2=0x00;
TCNT2=0x00;
OCR2=0x00;

// External Interrupt(s) initialization
// INT0: On
// INT0 Mode: Falling Edge
// INT1: Off
// INT2: On
// INT2 Mode: Falling Edge
GICR|=0x60;
MCUCR=0x02;
MCUCSR=0x00;
GIFR=0x60;

// Timer(s)/Counter(s) Interrupt(s) initialization
TIMSK=0x00;

// USART initialization
// USART disabled
UCSRB=0x00;

// Analog Comparator initialization
// Analog Comparator: Off
// Analog Comparator Input Capture by Timer/Counter 1: Off
ACSR=0x80;
SFIOR=0x00;

// ADC initialization
// ADC disabled
ADCSRA=0x00;

// SPI initialization
// SPI disabled
SPCR=0x00;

// TWI initialization
// TWI disabled
TWCR=0x00;

// Global enable interrupts
#asm("sei")
if(random<1){
    random=1;
}

//multiplicar por numero primo
random=(random*7)+2;
random=random%17;

//definir direccion
rand=(int)random;
rand*=7;
direccion=rand%4;

//definir x
x=2;
//definir y
y=3;

barra1=0;
barra2=3;

cont1=0;
cont2=0;
i=j=0;
dsplz=0;
stay=0;
cols=0;
puntos1=0;
puntos2=0;
rapidez=99;
inst=0;
win=0;

while (1)
      {
      if(!win){
        delay_ms(1);

        cols++;
        if(cols>4){
            cols=0;
        }
        
        
        PORTA &=0x7f;
        PORTC &=0x7f;
        PORTB |=0x81;
        PORTC |=0x60;
        
        inst++;
        if(inst>1){
            inst=0;
        }
        
        //Muestra de el puntaje
        if(inst){
            PORTA =tabla7segmentos[inst][puntos2];
            PORTC &=0xbf;
            PORTB &=0x7f;
        }else{
            PORTA =tabla7segmentos[inst][puntos1];
            PORTC |=0x80;
            PORTC &=0xdf;
            PORTB &=0xfe;
        }  
        
      //Movimiento de barras  
      if(derecha1==0){
      barra1++;
        if(barra1>3){
            barra1=3;
        }
        delay_ms(200);
      }  
      if(izquierda1==0){
      barra1--;
        if(barra1<0){
            barra1=0;
        } 
        delay_ms(200);
      }  
      if(derecha2==0){
      barra2++;
        if(barra2>3){
            barra2=3;  
        }
        delay_ms(200);
      }  
      if(izquierda2==0){
      barra2--;
        if(barra2<0){
            barra2=0;
        } 
        delay_ms(200);
      }  
      
      
      //Matriz de LEDs
      if(dsplz>rapidez){
        dsplz=0;
        if(!stay){
            stay=1;                        
        }else{
        stay=0;
        
        //Validaciones y definición de nuea dirección de pelota
        switch(direccion){
            case 0: //noroeste
                if((x-1)<0){
                    if(y==1){
                        if(barra2==0 || barra2==1){
                            direccion=2;
                            
                        }else{
                            direccion=1;
                        }
                    }else if(y>=2){
                        direccion=1;
                    }
                }else{
                    if(y==1){
                        if(barra2==0){
                                if(x==1){
                                    direccion=3;
                                }
                                if(x==2){
                                    direccion=2;
                                }
                        }else if(barra2==1){
                                if(x==2){
                                    direccion=3;
                                }
                                if(x==3){
                                    direccion=2;
                                }
                        }else if(barra2==2){
                                if(x==3){
                                    direccion=3;
                                }
                        }
                    }else if(y<=2){
                        //direccion=0;
                    }
                }
                break;
            case 1: //noreste
                if((x+1)>4){
                    if(y==1){
                        if(barra2==2 || barra2==3){
                            direccion=3;
                            
                        }else{
                            direccion=0;
                        }
                    }else if(y>=2){
                        direccion=0;
                    }
                }else{
                    if(y==1){
                        if(barra2==1){
                                if(x==1){
                                    direccion=2;
                                }
                        }else if(barra2==2){
                                if(x==2){
                                    direccion=2;
                                }
                                if(x==1){
                                    direccion=3;
                                }
                        }else if (barra2==3){
                                if(x==3){
                                    direccion=2;
                                }
                                if(x==2){
                                    direccion=3;
                                }
                        }
                    }else if(y>=2){
                        //direccion=1;
                    }
                }
                break;
            case 2: //sureste
                if((x+1)>4){
                    if(y==5){
                        if(barra1==2 || barra1==3){
                            direccion=0;
                            
                        }else{
                            direccion=3;
                        }
                    }else if(y<=4){
                        direccion=3;
                    }
                }else{
                    if(y==5){
                        if(barra1==1){
                                if(x==1){
                                    direccion=1;
                                }
                        }else if(barra1==2){
                                if(x==2){
                                    direccion=1;
                                }
                                if(x==1){
                                    direccion=0;
                                }
                        }else if (barra1==3){
                                if(x==3){
                                    direccion=1;
                                }
                                if(x==2){
                                    direccion=0;
                                }
                        }
                    }else if(y<=4){
                        //direccion=2;
                    }
                }
                break;
            case 3: //suroeste
                if((x-1)<0){
                    if(y==5){
                        if(barra1==0 || barra1==1){
                            direccion=1;
                            
                        }else{
                            direccion=2;
                        }
                    }else if(y<=4){
                        direccion=2;
                    }
                }else{
                    if(y==5){
                        if(barra1==0){
                                if(x==1){
                                    direccion=0;
                                }
                                if(x==2){
                                    direccion=1;
                                }
                        }else if(barra1==1){
                                if(x==2){
                                    direccion=0;
                                }
                                if(x==3){
                                    direccion=1;
                                }
                        }else if(barra1==2){
                                if(x==3){
                                    direccion=0;
                                }
                        }
                    }else if(y<=4){
                        //direccion=3;
                    }
                }
                break;
            default:
                break;
        }
        
        //Redireccionamiento de pelota
        switch(direccion){
            case 0: //noroeste
                x--;
                y--;
                break;
            case 1: //noreste
                x++;
                y--;
                break;
            case 2: //sureste
                x++;
                y++;
                break;
            case 3: //suroeste
                x--;
                y++;
                break;
            default:
                break;
        }
      }
      }else{
        dsplz++;
      }
      
      //Barrido para la pelotita
        PORTD |=0xfb;
        PORTC &=0xe0;
        if((cols%5)==x){
        switch(y){
            case 0:
                PORTD &=0x7f;
                break;
            case 1:
                PORTD &=0xbf;
                break;
            case 2:
                PORTD &=0xdf;
                break;
            case 3:
                PORTD &=0xef;
                break;
            case 4:
                PORTD &=0xf7;
                break;
            case 5:
                PORTD &=0xfd;
                break;
            case 6:
                PORTD &=0xfe;
                break;
            default:
                break;
        }
        }
        
        //Barrido para las barras
        switch((cols%5)){
            case 0:
                if(barra1==0){
                    PORTD &=0xfe;
                }
                if(barra2==0){
                    PORTD &=0x7f;
                }
                PORTC |=0x01;
                break;
            case 1:
                if(barra1==0){
                    PORTD &=0xfe;
                }
                if(barra2==0){
                    PORTD &=0x7f;
                }
                if(barra1==1){
                    PORTD &=0xfe;
                }
                if(barra2==1){
                    PORTD &=0x7f;
                }
                PORTC |=0x02;
                break;
            case 2:
                if(barra1==1){
                    PORTD &=0xfe;
                }
                if(barra2==1){
                    PORTD &=0x7f;
                }
                if(barra1==2){
                    PORTD &=0xfe;
                }
                if(barra2==2){
                    PORTD &=0x7f;
                }
                PORTC |=0x04;
                break;
            case 3:
                if(barra1==2){
                    PORTD &=0xfe;
                }
                if(barra2==2){
                    PORTD &=0x7f;
                }
                if(barra1==3){
                    PORTD &=0xfe;
                }
                if(barra2==3){
                    PORTD &=0x7f;
                }
                PORTC |=0x08;
                break;
            case 4:
                if(barra1==3){
                    PORTD &=0xfe;
                }
                if(barra2==3){
                    PORTD &=0x7f;
                }
                PORTC |=0x10;
                break;
            default:
                break;
        }
     
        //Anotación de un punto
        if(y<0 || y>6){
        PORTD |=0xfb;
        PORTC &=0xe0;
        if(y>6){
            puntos2++;
            if(puntos2>9){
                win=1;
            }
            //redefinir direccion
            rand*=7;
            rand=rand%11;
            direccion=rand%2;
            
        }
        if(y<0){
            puntos1++;
            if(puntos1>9){
                win=1;
            }
            //redefinir direccion
            rand*=7;
            rand=rand%11;
            direccion=(rand%2)+2;
            
        }
        //redefinir x
        rand*=19;
        rand+=7;
        x=1+(rand%3);
        //redefinir y
        y=3;
        
        delay_ms(200);
        }
      }
      }
}
