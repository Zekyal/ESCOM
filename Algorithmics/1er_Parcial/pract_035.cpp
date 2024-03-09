#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, b, A;
	printf("%crea tri%cngulo rect%cngulo\n\n", 181, 160, 160);
	printf("Introduzca la medida de la altura del tri%cngulo:", 160);
	scanf("%f", &a);
	printf("Introduzca la medida de la base del tri%cngulo:", 160);
	scanf("%f", &b);
	A=(b*a)/2;
	printf("El %crea del tri%cngulo es: %f", 160, 160, A);
	return 0;
}
