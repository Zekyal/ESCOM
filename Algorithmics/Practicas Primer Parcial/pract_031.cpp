#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float r, A;
	printf("%crea C%crculo", 181, 161);
	printf("\n\nIntroduzca a medida del radio del c%crculo:", 161);
	scanf("%f", &r);
	A=r*r*3.1416;
	printf("El %crea del c%crculo es: %f", 181, 161, A);
	return 0;
}
