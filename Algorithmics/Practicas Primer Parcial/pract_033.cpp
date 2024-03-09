#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float kg, lb;
	printf("Conversor de kg a lb\n\n");
	printf("Introduzca el valor en kg:");
	scanf("%f", &kg);
	lb=kg*2.2046;
	printf("%flb", lb);
	return 0;
}
