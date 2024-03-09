#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int a, b, pr, ce, re;
	printf("Escriba 2 n%cmeros de 3 cifras sparados por comas:", 163);
	scanf("%d, %d", &a, &b);
	
	if(a>=100 && b>=100)
	{
		pr=a*b;
	    ce=a/b;
	    re=a%b;
	    printf("El producto entre los dos n%cmeros es %d, el cociente entero es %d y el residuo es %d", 163, pr, ce, re);
	}
	else if(a<=-100 && b<=-100)
	{
		pr=a*b;
	    ce=a/b;
	    re=a%b;
	    printf("El producto entre los dos n%cmeros es %d, el cociente entero es %d y el residuo es %d", 163, pr, ce, re);
	}
		else if(a>999 || b>999)
	{
		printf("No es un n%cmero de 3 cifras", 163);
	}
	else if(a<-999 || b<-999)
	{
		printf("No es un n%cmero de 3 cifras", 163);
	}
	else
	{
		printf("No es un n%cmero de 3 cifras", 163);
	}
	return 0;
}
