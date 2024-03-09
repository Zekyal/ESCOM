#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float h, m1, m2;
	int hg;
	printf("Introduzca el m%cmero de horas: ", 163);
	scanf("%f", &h);
	
	if(h<5)
	{
		m1=1.5*h;
		printf("El monto a pagar es $%f", m1);
	}
	
	else if (h>5)
	{
	    hg=h/5;
	    m2=(h-hg)*1.5;
	    printf("El monto a pagar es $%f", m2);	
	}
	return 0;
}
