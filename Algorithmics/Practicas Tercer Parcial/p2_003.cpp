#include <stdio.h>
#include <stdlib.h>

int main()
{
	float a,b,c;
	printf("Ingresa 3 n%cmeros distintos separados por una coma (,): ", 163);
	scanf("%f, %f, %f", &a, &b, &c);
	
	if(a>b)
	{
		if(b>c)
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", a, b, c);
		}
		else if(c>a)
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", c, a, b);
		}
		else 
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", a, c, b);
		}
	}
	
	else if(b>a)
	{
		if(a>c)
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", b, a, c);
		}
		else if(b>c)
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", b, c, a);
		}
		else 
		{
			printf("\nOrden de mayor a menor es: %f, %f , %f", c, b, a);
		}
	}

	else
	{
		printf("\nDos o m%cs n%cmeros son iguales", 160, 163);
	}

    return 0;
}
