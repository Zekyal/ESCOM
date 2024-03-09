#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float peso2, peso5, peso10, centavo50, moni;
	printf("Calculadora de dinero (^^) \n\n Inserte la cantidad de monedas que posee de cada tipo: \n\n");
	printf("Monedas de $2: ");
	scanf("%f", &peso2);
	printf("Monedas de $5: ");
	scanf("%f", &peso5);
	printf("Monedas de $10: ");
	scanf("%f", &peso10);
	printf("Monedas de 50%c: ", 189);
	scanf("%f", &centavo50);
	moni=2*peso2+5*peso5+10*peso10+0.5*centavo50;
	printf("El dinero que posee es: $%f", moni);
	return 0;
}
