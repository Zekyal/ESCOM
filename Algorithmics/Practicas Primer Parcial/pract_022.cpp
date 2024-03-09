#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float com, desc, total;
	printf("Introduzca el total de su compra: $");
	scanf("%f", &com);
	desc=(com*15)/100.0;
	total=com-desc;
	printf("El total con descuento aplicado es: $%f", total);
	return 0;
}
