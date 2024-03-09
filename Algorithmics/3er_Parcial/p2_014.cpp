#include<stdio.h>
#include<stdlib.h>

int main()
{
	int mes;
	printf("Introduzca el n%cmero de un mes (1 a 12): ", 163);
	scanf("%d", &mes);
	
	if(mes==1)
	{
		printf("Enero tiene 31 d%cas", 161);
	}
	else if(mes==2)
	{
		printf("Febrero tiene 28 d%cas, y 29 d%cas si es a%co bisiesto", 161, 161, 164);
	}
	else if(mes==3)
	{
		printf("Marzo tiene 31 d%cas", 161);
	}
	else if(mes==4)
	{
		printf("Abril tiene 30 d%cas", 161);
	}
	else if(mes==5)
	{
		printf("Mayo tiene 31 d%cas", 161);
	}
	else if(mes==6)
	{
		printf("Junio tiene 30 d%cas", 161);
	}
	else if(mes==7)
	{
		printf("Julio tiene 31 d%cas", 161);
	}
	else if(mes==8)
	{
		printf("Agosto tiene 31 d%cas", 161);
	}
	else if(mes==9)
	{
		printf("Septiembre tiene 30 d%cas", 161);
	}
	else if(mes==10)
	{
		printf("Octubre tiene 31 d%cas", 161);
	}
	else if(mes==11)
	{
		printf("Noviembre tiene 30 d%cas", 161);
	}
	else if(mes==12)
	{
		printf("Diciembre tiene 31 d%cas", 161);
	}
	else
	{
		printf("Ese no es un mes :/");
	}
	
    return 0;
}
