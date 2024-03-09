#include<stdio.h>

int main()
{
	float a,b,c, d, e;
	printf("Introduce 4 n%cmeros separados por coma(,) OwO:", 163);
	scanf("%f, %f, %f, %f", &a, &b, &c, &d);
	printf("\nN%cmeros en el orden inicial: %f, %f, %f, %f ", 163, a, b, c, d);
	e=a;
	a=d;
	d=e;
	e=c;
	c=b;
	b=e;
	printf("\nN%cmeros a la inversa: %f, %f, %f, %f", 163, a, b, c, d);
	return 0;
}

