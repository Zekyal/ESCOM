#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float peso, dolar;
	printf("Conversor de pesos mexicanos a d%clares de Singapur \n\nIntroduzca el valor monetario en pesos mexicanos: MXN$", 162); 
	scanf("%f", &peso);
	dolar=peso/13.1883299;
	printf("El valor en d%clares de Singapur es SGD$%f", 162, dolar); //No especifico que tipo de dólar así que improvise :)
	return 0;
}
