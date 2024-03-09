#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float pr, tasa;
	printf("Tasa de inter%cs anual (27%c) \n\n", 130, 37);
	printf("Coloque el valor monetario de su pr%cstamo:", 130);
	scanf("%f", &pr);
	tasa= (pr*27)/100.0;
	printf("La tasa de inter%cs es: %f", 130, tasa);
	return 0;
}
