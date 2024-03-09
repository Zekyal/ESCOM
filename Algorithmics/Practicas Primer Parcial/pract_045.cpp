#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, b, c, d, e, f, x, y;
	printf("Sistema de ecuaciones lineales\n\n");
	printf("ax+by=c \nIntroduzca un valor para las variables a, b y c separados por coma(,):");
	scanf("%f, %f, %f", &a, &b, &c);
	printf("dx+ey=f \nIntroduzca un valor para las variables d, e y f separados por coma(,):");
	scanf("%f, %f, %f", &d, &e, &f);
	x=(c*e-b*f)/(a*e+b*d+0.0);
	y=(a*f-c*d)/(a*e+b*d+0.0);
	printf("\nx=%f \t y=%f", x, y);
	return 0;
}
