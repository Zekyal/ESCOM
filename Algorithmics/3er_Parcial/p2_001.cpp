#include<stdio.h>
#include<stdlib.h>

int main()
{
	int cal;
	printf("Inserte su calificaci%cn: ", 162);
	scanf("%d", &cal);
	
	if(cal<=5)
	{
		if(cal>=0)
		{
			printf("NS");	
		}
		else
		{
			printf("Calificaci%cn no v%clida", 162, 160);
		}
	}
    else if(cal==6)
	{
		printf("S");
	}
	else if(cal==7)
	{
		printf("R");
	}
	else if(cal==8)
	{
		printf("B");
	}
	else if(cal==9)
	{
		printf("MB");
	}
	else if(cal==10)
	{
		printf("E");
	}
	else
	{
		printf("Calificaci%cn no v%clida", 162, 160);
	}
	
	return 0;
}
