#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int year, meses, totalmes;
	printf("Ingrese su edad o la edad de otra persona de la forma: a%co,meses\n", 164);
	scanf("%d, %d",&year, &meses);
	totalmes=year*12+meses;
	printf("Su tiempo de vida actual es de %d mese(s)", totalmes);
	return 0;
}
