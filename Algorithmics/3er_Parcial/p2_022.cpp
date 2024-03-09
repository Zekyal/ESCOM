#include<stdio.h>
#include<stdlib.h>
#include <time.h>

int main()
{
	float importe, desc, tot;
	int color;
	printf("Inserte importe a pagar del cliente: $", 164);
	scanf("%f", &importe);
	color=1+rand()%4;
	
	if(color==1)
	{
		printf("\nTe toco una bolita azul");
		desc=(importe*20)/100+0.0;
		tot=importe-desc;
		printf("\nPrecio: $%f", tot);
	}
	
	if(color==2)
	{
		printf("\nTe toco una bolita roja");
		desc=(importe*30)/100+0.0;
		tot=importe-desc;
		printf("\nPrecio: $%f", tot);
	}
	
	if(color==3)
	{
	    printf("\nTe toco una bolita blanca");
		printf("\nPrecio: $%f", importe);
	}
	
	fflush(stdin);
	
	return 0;
}
