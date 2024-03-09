#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float a, b, c, su, mul, res;
	printf("Inroduzca 3 números enteros positivos separados por coma(,): ");
	scanf("%f, %f, %f", &a, &b, &c);
	
	if(a>=0 && b>=0 && c>=0)
	{
		su=a+b+c;
		mul=a*b*c;
		res=a-b-c;
		printf("El resultado de la suma de los tres n%cmeros es %f, la resta de los tres es %f y la multiplicac%cn de estos es %f", 163, su, res, 162, mul);
	}
	else
	{
	    printf("Uno de los numeros son negativos :I");
	}
	return 0;
}
