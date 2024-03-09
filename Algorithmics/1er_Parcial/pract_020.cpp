#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float cap, pagmens, total;
	printf("Introduzca su capital: $");
	scanf("%f", &cap);
	pagmens=(cap*2.5)/100.0;
	total=12*pagmens;
	printf("Por mes obtendr%C una ganancia de $%f y anualmente de $%f", 160, pagmens, total);
	return 0;
}
