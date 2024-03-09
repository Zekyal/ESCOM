#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, b, sum, pro;
	printf("Introduzca 2 n%cmeros separados por (,):", 163);
	scanf("%f, %f", &a, &b);
	sum=a+b;
	pro=a*b;
	printf("La suma de los dos n%cmeros es %f y el producto es %f", 163, sum, pro);
	return 0;
}
