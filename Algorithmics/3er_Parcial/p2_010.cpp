#include<stdio.h>
#include<stdlib.h>
#include<windows.h>

int main()
{
	float tm, th;
	printf("Introduzca la temperatura m%cxima de este mes: ", 160);
	scanf("%f", &tm);
	printf("Introduzca la temperatura de hoy: ");
	scanf("%f", &th);
	
	if(tm<th)
	{
		printf("Actualizando");
		
		for(int i=0; i<10; i++)
		{
			printf(".");
			Sleep(100);
		}
		
		tm=th;
		printf("\nLa temperatura m%cxima se ha actualizado: %f", 160, tm);
	}
	else
	{
		printf("\nLa temperatura m%cxima siguen siendo %f", 160, tm);
	}
	return 0;
}
