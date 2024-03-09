#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float s, m;
	printf("Conversor de segundos a minutos \n\n");
	printf("Introduzca una cantidad de tiempo en segundos:");
	scanf("%f", &s);
	m=s/60;
	printf("%fseg \t %fmin", s, m);
	return 0;
}
