#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float s, sem, dia, h, m;
	printf("Introduzca su medida de tiempo en segundos:");
	scanf("%f", &s);
	m=s/60;
	h=m/60;
	dia=h/24;
	sem=dia/7;
	printf("%f segundos \n%f minutos \n%f horas \n%f dias \n%f semanas", s, m, h, dia, sem);
	return 0;
}
