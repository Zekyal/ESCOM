#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define T 12

int main()
{
	int turno, num, a, cont;
	printf("ADIVINA EL N%cMERO :)\n\n", 233);
	srand(time(NULL));
	num=rand()%(100);
	
	do
	{
		printf("Introduzca un n%cmero entre el 0 al 100: ", 163);
		scanf("%d", &a);
			
		if(a<num)
		{
			printf("El n%cmero a acertar es mayor al introducido\t", 163);
			turno++;
			cont++;
		}	
		else if(a==num)
		{
			turno=12;
		}	
		else
		{
			printf("El n%cmero a acertar es menor al introducido\t", 163);
			turno++;
			cont++;
		}
	}while(turno<T);
	
	if (cont>=1 && cont<=3)
	{
		printf("\nSuertudo");
	}
	else if(cont>=4 && cont<=6)
	{
		printf("\nSos un genio");
	}
	else if(cont==7)
	{
		printf("\nNo est%c mal", 160);
	}
	else if(cont==8)
	{
		printf("\nSe puede mejorar");
	}
	else
	{
		printf("\nQue pasa amigo :'v'");
	}
}
