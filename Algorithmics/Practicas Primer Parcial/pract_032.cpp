#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float cm, in;
	printf("Conversor de cm a in\n\n");
	printf("Introduzca el valor en cm:");
	scanf("%f", &cm);
	in=cm*0.39737;
	printf("%fin", in);
	return 0;
}
