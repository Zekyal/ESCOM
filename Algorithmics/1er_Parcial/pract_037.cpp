#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float a, b, c, semiP, A;
	printf("Inserte las medidas de los lados de su tri%cngulo separados por coma (,):", 160);
	scanf("%f, %f, %f", &a, &b, &c);
	semiP=(a+b+c)/2;
	A=sqrt(semiP*(semiP-a)*(semiP-b)*(semiP-c));
	printf("El %crea del tri%cngulo es: %f", 181, 160, A);
	return 0;
}
