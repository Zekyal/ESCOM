#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float C, F;
	printf("Conversor de gradors Celsius a Farenheit\n\n");
	printf("Introduzca su temperatura en Celsius:");
	scanf("%f", &C);
	F=(9/5.0)*(C+32);
	printf("La temperatura es %fF", F);
	return 0;
}
