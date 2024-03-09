#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int divi;
	printf("Cambio de divisas \n\n");
	printf("Seleccione el cambio de divisa que desee relizar:\n\n 1. Peso Mexicano(MXN$) a Euro(€) \n 2. Peso Mexicano(MXN$)a D%clar Estadounidense(USD$) \n", 162);
	scanf("%d", &divi);
	
	switch(divi)
	{
		case 1:
			float euro, pesoe;
			printf("Introduzca una cantidad de dinero en Pesos Mexicanos(MXN$): MXN$");
	        scanf("%f",&pesoe);
			euro=pesoe/21.1323616;
			printf("%f€", euro);
			break;
		case 2:
			float dolar, pesod;
			printf("Introduzca una cantidad de dinero en Pesos Mexicanos(MXN$): MXN$");
	        scanf("%f",&pesod);
			dolar=pesod/17.8408949;
			printf("%f USD$", dolar);
			break;
	}
	return 0;
}
