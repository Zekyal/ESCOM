#include<stdio.h>
#include<stdlib.h>

int main()
{
	float a, b, x;
	printf("Resoluci%cn de ecuaciones de primer grado\n\n", 162);
	printf("Inserte los valores de a y b en el orden correspondiente(ax%cb) y separados por coma (,): ", 241);
	scanf("%f, %f", &a, &b);
	
	if(a==0)
	{
		if(b>0)
		{
		printf("Soluci%cn imposible", 162);
		}
		if(b<0)
		{
		printf("Soluci%cn imposible", 162);
		}
		else
		{
		printf("Soluci%cn indeterminada", 162);
		}
	}
	else
	{
		x=-b/a+0.0;
		printf("x=%f", x);
	}
	
	return 0;
}
