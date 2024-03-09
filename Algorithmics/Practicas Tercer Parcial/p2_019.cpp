#include<stdio.h>
#include<stdlib.h>

int main()
{
	float cal;
	printf("Inserte su calificaci%cn: ", 162);
	scanf("%f", &cal);
	
	if(cal>=0)
	{
		if(cal<5)
		{
			printf("Suspenso");
		}
		else if(cal>=5)
		{
			if(cal<6.5)
			{
				printf("Aprobado");
			}
			else if(cal>=6.5)
			{
				if(cal<8.5)
				{
					printf("Notable");
				}
				else if(cal>=8.5)
				{
					if(cal<10)
					{
			    		printf("Sobresaliente");
					}
					else if(cal==10)
					{
						printf("Matricula de honor");
					}
					else
					{
						printf("Valor de calificaci%cn no v%clido", 162, 160);
					}
				}
			}
		}
	}
	
	else
	{
		printf("Valor de calificaci%cn no v%clido", 162, 160);
	}
	
    return 0;
}
