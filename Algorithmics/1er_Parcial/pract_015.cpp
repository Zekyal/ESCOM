#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, l, A, arena;
	printf("Intoduzca la medida de la altura de la pared: ");
	scanf("%f", &a);
	printf("Intoduzca la medida de el largo de la pared: ");
	scanf("%f", &l);
	A=a*l;
	arena=A*0.5;
	printf("La cantidad de arena que necesitar%c ser%c de %f metros c%cbicos", 160, 160, arena, 163);
	return 0;
}
