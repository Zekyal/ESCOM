#include <stdio.h>
#include <stdlib.h>

int main()
{
	float a,b,c;
	printf("Ingresa 3 n%cmeros distintos separados por una coma (,): ", 163);
	scanf("%f, %f, %f", &a, &b, &c);
	
	if(a>b && b>c)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", a, b, c);
	}
	if(a>c && c>b)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", a, c, b);
	}
	if(b>a && a>c)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", b, a, c);
	}
	if(b>c && c>a)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", b, c, a);
	}
	if(c>b && b>a)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", c, b, a);
	}
	if(c>a && a>b)
	{
		printf("\nOrden de mayor a menor es: %f, %f , %f", c, a, b);
	}
	
	return 0;
}
