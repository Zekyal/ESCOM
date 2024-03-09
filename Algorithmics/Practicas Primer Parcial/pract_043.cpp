#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float r, L, A;
	printf("Introduzca el radio de su circunferencia:");
	scanf("%f", &r);
	L=2*3.1416*r;
	A=3.1416*pow(r,2);
	printf("La longitud es %f y el %crea es %f", L, 181, A);
	return 0;
}
