#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float l, a, S;
	printf("Introduce la medida de la longitud:");
	scanf("%f", &l);
	printf("Introduce la medida de la anchura:");
	scanf("%f", &a);
	S=(l*a)/2.0;
	printf("La superficie es: %.4f", S);
	return 0;
}
