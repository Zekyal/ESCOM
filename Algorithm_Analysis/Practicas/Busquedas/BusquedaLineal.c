#include<stdio.h>
#include<stdlib.h>
//#include<pthread.h>

void busquedaLineal(int*, int, int);

int main()
{
  	int *A, n, num, i;
  	scanf("%d",&n);//Número de elementos del arreglo
  	A=malloc(sizeof(int)*n);
  	printf("\n");

	for(i=0;i<n;i++)//Ingresamos los valores de los elemntos del arreglo
    scanf("%d",&A[i]);
    printf("\n");
  
 	scanf("%d",&num);//Introducimos el elemento que se desea buscar
 	printf("\n");
 	
 	busquedaLineal(A, n, num);
}

void busquedaLineal(int *A, int n, int num)
{
	int bandera=0, i;
	
  	for(i=0;i<n;i++)
  	{
  		if(A[i]==num)
  		{
			printf("\nEl numero %d esta en la posicion %d ",A[i],i+1);
			bandera=1;
		}
	}
  
 	if(bandera!=1)
 		printf("\nEl elemento %d no se encontro",num);
}
