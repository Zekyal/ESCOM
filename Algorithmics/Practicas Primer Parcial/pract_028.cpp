#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, b, su, mul;
	printf("Inroduzca 2 números enteros positivos separados por coma(,): ");
	scanf("%f, %f", &a, &b);
	
	if(a>=0 && b>=0)
	{
		su=a+b;
		mul=a*b;
		printf("El resultado de la suma de los dos n%cmeros es %f y la multiplicac%cn de estos es %f", 163, su, 162, mul);
	}
	else
	{
	    printf("Uno o ambos numeros son negativos :I");
	}
	return 0;
}
