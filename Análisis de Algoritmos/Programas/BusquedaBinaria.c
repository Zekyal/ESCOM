#include<stdio.h>
#include<stdlib.h>
//#include<pthread.h>

void busquedaBinaria(int *A, int n, int dato);

int main()
{
	int *A, n, i, j, n_hilos, num;
	scanf("%d",&n);//Número de elementos del arreglo
	A=malloc(n*sizeof(int));
	/*printf("Numero de hilos: ");
	scanf("%d",&n_hilos);
	pthread_t *hilo;
	hilo=malloc(n_hilos*sizeof(pthread_t));*/
	printf("\n");
  
	for(i=0;i<n;i++)//Ingresamos los valores de los elemntos del arreglo
		scanf("%d",&A[i]);
	
	printf("\n");
	scanf("%d",&num);//Introducimos el elemento que se desea buscar
	
	busquedaBinaria(A,n,num);
}

void busquedaBinaria(int  *A, int n, int dato) 
{
	int centro=0,inf=0,sup=n-1, bandera=0;
	
	while(inf<=sup&&bandera!=1)
	{
		centro=((sup-inf)/2)+inf;
		
      	if(A[centro]==dato)
	  	{      
      		printf("\nEl elemento %d se encontro en la posicion %d",dato,A[centro]); 
      		bandera=1;
      	}
      	else if(dato < A[centro]) 
	 	sup=centro-1;
      	else if(dato>A[centro])                           
	  	inf=centro+1;
   }
   
   if(bandera!=1)
 		printf("\nEl elemento %d no se encontro",dato); 
}
