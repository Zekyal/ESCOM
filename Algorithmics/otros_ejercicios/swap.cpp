#include<stdio.h>

int main()
{
	float a,b,c;
	printf("Introduce 2 n%cmeros separados por coma(,) OwO:", 163);
	scanf("%f, %f", &a, &b);
	printf("\nAntes del swap: \n a=%f \n b=%f \n", a, b);
	c=a;
	a=b;
	b=c;
	printf("\nDespues del swap: \n a=%f \n b=%f", a, b);
}

