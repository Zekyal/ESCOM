#include<stdio.h>
#include<stdlib.h>
#include<time.h>    

int numeros[50];

void llenar()
{
    int i;
    srand(time(NULL));

    for(i=0; i<50; i++)
	    numeros[i]= rand();
}

void imprimir()
{
    int i;
    for(i=0; i<50; i++)
		printf("(%d) %d |", i, numeros[49- i]);
	printf("\n\n");
}

void burbuja()
{
    int i, j, aux;

    for(i=0; i<50; i++)
	{
		for(j=0; j<50; j++)
		{
			if(numeros[j]<numeros[j+1])
			{
				aux= numeros[j];
				numeros[j]= numeros[j+1];
				numeros[j+1]= aux;
			}
		}
	}   
}

int main()
{
	llenar();//Generacion de numeros aleatorios
    imprimir();
    burbuja();//Algoritmo del metodo de burbuja
    imprimir();
	return 0;
}
