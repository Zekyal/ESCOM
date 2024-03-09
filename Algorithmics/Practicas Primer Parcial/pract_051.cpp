#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float pre, desc, pre2;
	printf("Introduzca el precio total a pagar: $");
	scanf("%f", &pre);
	desc=(pre*15)/100.0;
	pre2=pre-desc;
	printf("El precio a pagar con el decuento del 15%c aplicado es $%f", 37, pre2);
	return 0;
}
