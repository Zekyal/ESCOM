#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	float a, b, c, dis, x, x1, x2;
	printf("Resoluci%cn de ecuaciones de segundo grado\n\n", 162);
	printf("Inserte los valores de a, b y c en el orden correspondiente(ax%cbx%cc) y separados por coma (,): ", 241, 241);
	scanf("%f, %f, %f", &a, &b, &c);
	dis=pow(b,2)-(4*a*c);
	
	if(dis==0)
	{
		x=-b/2*a+0.0;
		printf("\nx=%f", x);
	}
	else if(dis>0)
	{
		x1=(-b+dis)/2*a+0.0;
		x2=(-b-dis)/2*a+0.0;
		printf("\n\n x1=%f\n x2=%f", x1, x2);
	}
	else if(dis<0)
	{
		printf("La(s) solucion(es) son indeterminadas(imaginarias)");
	}
	
	return 0;
}
