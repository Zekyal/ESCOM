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
	if(cal==6)
	{
		printf("\nSuficiente(De pansazo xd)");
	}
	if(cal==7)
	{
		printf("\nRegular :|");
	}
	if(cal==8)
	{
		printf("\nBien :)");
	}
	if(cal==9)
	{
		printf("\nMuy bien :D");
	}
	if(cal==10)
	{
		printf("\nExcelente %c(^^)/", 92);
	}
	
	return 0;
}
	
