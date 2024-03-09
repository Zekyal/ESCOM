#include <stdio.h>
#include <stdlib.h>

int main()
{
	int cal;
	printf("Ingresa tu calificaci%cn: ", 162);
	scanf("%d", &cal);
	
	if(cal<=5 && cal>=0)
	{
		printf("\nReprobado :(");
	}
	else if(cal==6)
	{
		printf("\nSuficiente(De pansazo xd)");
	}
	else if(cal==7)
	{
		printf("\nRegular :|");
	}
	else if(cal==8)
	{
		printf("\nBien :)");
	}
	else if(cal==9)
	{
		printf("\nMuy bien :D");
	}
	else if(cal==10)
	{
		printf("\nExcelente %c(^^)/", 92);
	}
	else
	{
		printf("\nValor inv%clido", 160);
	}
	
	return 0;
}
