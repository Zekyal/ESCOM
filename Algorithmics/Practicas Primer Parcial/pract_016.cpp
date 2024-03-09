#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float h, m, s, costo;
	printf("Introduzca la cantidad de tiempo que requiere en su proceso (costo por segundo $0.25): \n\n");
	printf("Horas: ");
	scanf("%f", &h);
	printf("Minutos: ");
	scanf("%f", &m);
	printf("Segundos: ");
	scanf("%f", &s);
	costo=(h*3600+m*60+s)*0.25;
	printf("El costo ser%c de $%f", 160, costo);
	return 0;
}
